# jina-embeddings-v5-text: Task-Targeted Embedding Distillation

## Описание

**jina-embeddings-v5-text** — семейство компактных моделей эмбеддингов от Jina AI, использующих инновационный метод обучения, сочетающий **дистилляцию знаний** с **контрастивным обучением для конкретных задач**. Модели демонстрируют производительность на уровне или выше state-of-the-art для моделей сопоставимого размера, поддерживают длинные тексты (до 32k токенов) и множество языков.

**Модели:**
- `jina-embeddings-v5-text-small` (596M параметров, 1024 размерность эмбеддинга)
- `jina-embeddings-v5-text-nano` (212M параметров, 768 размерность эмбеддинга)

**Ключевые особенности:**
- Двухэтапное обучение: дистилляция + task-specific адаптеры
- Поддержка 15+ языков (включая русский, китайский, арабский)
- Длинные контексты до 32k токенов
- Robust к усечению и бинарной квантизации
- LoRA адаптеры для разных задач (retrieval, STS, clustering, classification)

## Архитектура модели

### Базовая архитектура

Модель основана на **трансформерной архитектуре** с **last-token pooling**:
- Использует последний токен (end-of-sequence) для генерации единого векторного представления
- Rotary positional embeddings (RoPE) для кодирования позиционной информации
- Разные значения θ для обучения и инференса для поддержки длинных контекстов

### LoRA адаптеры для задач

Модель включает **LoRA адаптеры** для поддержки различных задач, которые сложно оптимизировать совместно:

| Адаптер | Задача | Префиксы |
|---------|--------|----------|
| Retrieval | Асимметричный поиск | "Query:" / "Document:" |
| STS | Семантическая схожесть | "Document:" (симметричный) |
| Clustering | Группировка документов | "Document:" |
| Classification | Классификация | "Document:" |

Пользователи выбирают соответствующий адаптер во время инференса.

### Matryoshka Representation Learning

Модели поддерживают **усечение эмбеддингов** благодаря использованию Matryoshka Representation Learning во время обучения [[../../algorithms/neural_networks/embedders/matryoshka_representation_learning.md]]:
- Эмбеддинги можно обрезать для повышения эффективности downstream-задач
- Сохраняется производительность даже при уменьшенной размерности

## Метод обучения

### Этап 1: Дистилляция эмбеддингов

**Цель:** Передать знания от большой модели-учителя (`Qwen3-Embedding-4B`) к компактной студенческой модели.

**Подход:**
- Студент получает минимальные инструкции (только префиксы "Query:"/"Document:")
- Учитель получает общую инструкцию: *"Given a web search query, retrieve relevant passages that answer the query"*
- Линейный проекционный слой ψ: R^n → R^m проецирует эмбеддинги студента в пространство учителя
- **Distillation loss:** сумма косинусных расстояний между спроецированными эмбеддингами студента и учителя

```
L_distill = Σ cosine_distance(ψ(student_emb), teacher_emb)
```

**Фазы обучения:**

1. **General-Purpose Training:**
   - 50,000 шагов обучения
   - 300+ датасетов на 30+ языках
   - Разнообразные пары (query, document)

2. **Long Context Training** (только для small-модели):
   - Специально подобранные длинные документы (1000-4096 токенов)
   - Синтетические документы с запросами от LLM
   - Уменьшенный θ для RoPE, увеличенная максимальная длина последовательности
   - Мультиязычные пары документ-запрос

### Этап 2: Task-Specific Adapter Training

**Цель:** Обучить LoRA адаптеры для конкретных категорий задач при замороженных весах базовой модели.

#### 2.1 Asymmetric Retrieval Adapter

**Задача:** Асимметричный поиск, где запросы и документы имеют разную структуру.

**Подход:**
- Префиксы: "Query:" для запросов, "Document:" для документов
- Датасеты: триплеты (query, relevant document, hard negatives) + long-context датасеты

**Функция потерь (комбинация из трёх):**

1. **Contrastive Loss (InfoNCE)** с hard negatives:
   ```
   L_NCE = -log(exp(sim(x_i, y_i)/τ) / Σ exp(sim(x_i, y_j)/τ))
   ```

2. **Distillation Loss:** та же как в Этапе 1 для сохранения качества

3. **Spread-Out Regularizer (GOR):**
   - Стимулирует равномерное распределение эмбеддингов в пространстве
   - Улучшает робастность к квантизации и эффективность ANN-поиска

**Итоговая функция:**
```
L_retrieval = λ_NCE * L_NCE + λ_D * L_distill + λ_S * L_GOR
```

**Model averaging:** финальный адаптер усредняет веса последнего и более раннего чекпоинта.

#### 2.2 Text Matching (STS) Adapter

**Задача:** Семантическая текстовая схожесть (симметричные задачи).

**Особенности:**
- Только префикс "Document:" для симметричного кодирования
- Датасеты: STS12, SICK, мультиязычные STS датасеты
- Параллельные переводы и парафразы для дополнения данных

**CoSENT Ranking Loss:**
```
L_coSENT = -log(σ((sim(x_i,y_i) - sim(x_j,y_j)) / τ'))
```
для пар с ground-truth схожестью s_i > s_j.

**Гибридная стратегия:**
- Если есть оценки схожести → CoSENT loss
- Если нет оценок → комбинация InfoNCE + Distillation loss

#### 2.3 Clustering Adapter

**Задача:** Группировка связанных документов.

**Особенности:**
- Специальная инструкция для учителя: *"Identify the topic or theme of the given document:"*
- Дополнительная дистилляция с clustering-specific инструкцией
- Датасеты: заголовки и описания новостей и т.п.

#### 2.4 Classification Adapter

**Задача:** Классификация текстов (категоризация, sentiment analysis, intent recognition).

**Формат данных:**
- Триплеты: anchor, positive (тот же лейбл), 7 negatives (другие лейблы)

**Функция потерь:**
- **Bi-directional Contrastive Loss:** выравнивает представления anchor и positive
- **Relational Knowledge Distillation Regularizer:** предотвращает feature collapse, улучшает zero-shot способности

```
L_classification = λ_NCE * L_NCE + λ_R * L_relational_KD
```

## Оценка производительности

### Бенчмарки

Модели оценивались на:
- **MTEB** (Massive Text Embedding Benchmark) — английский и мультиязычный
- Дополнительные retrieval бенчмарки

### Сравнение с аналогами

Модели сравнивались с state-of-the-art мультиязычными моделями сопоставимого размера:
- jina-embeddings-v3
- snowflake-arctic-embed-l-v2
- multilingual-e5-large-instruct
- KaLM-embedding-multilingual-mini-instruct-v2.5
- voyage4-nano
- embeddinggemma-300m

### Ключевые результаты

- **Превосходят или соответствуют SOTA** для моделей аналогичного размера
- **Robust к усечению:** производительность сохраняется при обрезке эмбеддингов
- **Robust к бинарной квантизации:** эффективны при сжатии

## Ablation Studies

Исследования показали важность каждого компонента:

1. **Дистилляция vs. контрастивное обучение:**
   - Дистилляция превосходит naive contrastive training
   - Комбинированный подход даёт дальнейшее улучшение

2. **Проекция эмбеддингов:**
   - Проекция студента → пространство учителя эффективнее обратной

3. **Clustering instruction:**
   - Специальная инструкция для учителя критична для clustering-задач

4. **Long context training:**
   - Отдельное обучение на длинных текстах необходимо для quality на long documents

## Применение

### Рекомендации по использованию

| Задача | Адаптер | Префикс |
|--------|---------|---------|
| Поиск документов | Retrieval | "Query:" / "Document:" |
| Дубликаты/парафразы | STS | "Document:" |
| Группировка по темам | Clustering | "Document:" |
| Классификация | Classification | "Document:" |

### Примеры использования

**RAG-системы:**
- Retrieval адаптер для поиска релевантных документов
- Поддержка длинных контекстов для работы с большими документами

**Семантический поиск:**
- STS адаптер для поиска похожих документов
- Мультиязычная поддержка для международных приложений

**Классификация текстов:**
- Classification адаптер для категоризации
- Sentiment analysis, intent recognition

## Новые концепции и термины

- **Task-Targeted Embedding Distillation:** комбинированный метод обучения, сочетающий дистилляцию с task-specific contrastive loss
- **Asymmetric Retrieval:** подход к кодированию запросов и документов по-разному
- **Spread-Out Regularizer (GOR):** регуляризатор для равномерного распределения эмбеддингов
- **CoSENT Ranking Loss:** ranking-based функция потерь для STS задач
- **Relational Knowledge Distillation:** дистилляция relational structure между студентом и учителем

## Связи с другими темами

- [[../../algorithms/neural_networks/embedders/matryoshka_representation_learning.md]] — Matryoshka Representation Learning для сжатия векторного пространства
- [[../../ai/llm/knowledge_distillation/knowledge_distillation_memorization_dynamics.md]] — Дистилляция знаний и её влияние на запоминание
- [[../../ai/foundational_papers/scaling_architecture/distilling_knowledge_neural_nets.md]] — Основы дистилляции знаний (Hinton et al., 2015)
- [[./embedding_models.md]] — Обзор моделей эмбеддингов для RAG-систем
- [[../../algorithms/contrastive_learning.md]] — Контрастивное обучение и InfoNCE loss
- [[../../frameworks_and_libraries/huggingface/index.md]] — Размещение моделей на HuggingFace

## Источники

1. **Основная статья:** Akram, M.K., Sturua, S., Havriushenko, N., Herreros, Q., Günther, M., Werk, M., Xiao, H. (2026). jina-embeddings-v5-text: Task-Targeted Embedding Distillation. arXiv preprint arXiv:2602.15547. https://arxiv.org/abs/2602.15547

2. **HuggingFace Collection:** https://huggingface.co/collections/jinaai/jina-embeddings-v5-text

3. **Qwen3-Embedding-4B (teacher model):** https://huggingface.co/Qwen/Qwen3-Embedding-4B

4. **Базовые модели:**
   - Qwen3-0.6B-Base: https://qwen.ai/blog?id=qwen3
   - EuroBERT-210M: Boizard et al., 2025

## Дополнительные материалы

- **MTEB Benchmark:** https://huggingface.co/spaces/mteb/leaderboard
- **LoRA Adapters:** Sturua et al., 2025 — Task-specific adaptations для embedding моделей
- **InfoNCE Loss:** Oord et al., 2018 — Contrastive Predictive Coding
