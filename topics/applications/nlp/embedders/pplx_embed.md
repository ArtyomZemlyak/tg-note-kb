# pplx-embed: SOTA эмбеддинг-модели от Perplexity AI

## Обзор

**pplx-embed** — это семейство многоязычных эмбеддинг-моделей от Perplexity AI, построенных на архитектуре Qwen3 и оптимизированных для масштабируемого веб-поиска. Модели используют **двустороннее внимание (bidirectional attention)** и **диффузионное предобучение** для извлечения чистых семантических сигналов из зашумленных веб-данных.

**Ключевые особенности:**
- Построены на базе Qwen3 (0.6B и 4B параметры)
- Двустороннее внимание через диффузионное предобучение
- Нативная INT8-квантизация и Matryoshka Representation Learning
- Два типа моделей: для запросов и для контекстных эмбеддингов документов
- Лицензия: MIT

![Training pipeline of pplx-embed-v1 and pplx-embed-context-v1](../../../../media/img_1772189964_aqadmbnrg585cel_figure_1_training_pipeline_of.jpg)

**Изображение показывает:** Обучение pplx-embed-v1 и pplx-embed-context-v1. Многоэтапный конвейер включает: (1) продолженное диффузионное предобучение для конвертации каузального LLM в двусторонний энкодер, (2) попарное обучение на парах запрос-документ, (3) контекстное обучение для chunk-level эмбеддингов, (4) триплетное обучение с hard negative mining, и (5) слияние моделей через SLERP.

---

## Архитектура

### Базовая архитектура

| Компонент | Описание |
|-----------|----------|
| **Базовая модель** | Qwen3-0.6B и Qwen3-4B (decoder-only трансформеры) |
| **Внимание** | Двустороннее (bidirectional) — конвертировано из каузального |
| **Пуллинг** | Mean pooling с tanh-операцией |
| **Размерность эмбеддингов** | 1024 (0.6B), 2560 (4B) |
| **Контекстное окно** | 32K токенов |
| **Квантизация** | Нативная INT8 и бинарная |

### Конвертация в двусторонний энкодер

Модели используют **диффузионное предобучение** для конвертации каузального decoder-only трансформера в двусторонний энкодер:

1. **Отключение каузального маскирования** — позволяет использовать полное контекстное внимание
2. **Диффузионная цель** — обучение восстановлению замаскированных токенов из полного контекста
3. **Процесс поглощающего состояния** — каждый токен с вероятностью `t` заменяется на [MASK]
4. **Обучение через evidence lower bound** — сумма token-wise cross-entropy на замаскированных позициях

**Преимущества двустороннего внимания для retrieval:**
- Захват глобального контекста документа
- Более точное семантическое представление
- Возможность использования mean pooling вместо last-token pooling

---

## Варианты моделей

### pplx-embed-v1

**Назначение:** Стандартный плотный retrieval (dense retrieval)

| Модель | Параметры | Размерность | Квантизация | MTEB (Multilingual, v2) |
|--------|-----------|-------------|-------------|-------------------------|
| pplx-embed-v1-0.6B | 0.6B | 1024 | INT8 / Binary | 65.41% (INT8) |
| pplx-embed-v1-4B | 4B | 2560 | INT8 / Binary | 69.66% (INT8) |

**Особенности:**
- Оптимизированы для поиска запрос-документ
- Поддерживают 30+ языков
- Не требуют instruction префиксов

### pplx-embed-context-v1

**Назначение:** Контекстные эмбеддинги для chunk-level retrieval

| Модель | Параметры | Размерность | Квантизация | ConTEB |
|--------|-----------|-------------|-------------|--------|
| pplx-embed-context-v1-0.6B | 0.6B | 1024 | INT8 / Binary | 76.53% |
| pplx-embed-context-v1-4B | 4B | 2560 | INT8 / Binary | **81.96%** (SOTA) |

**Особенности:**
- Встраивают глобальный контекст документа в представление каждого чанка
- Используют **late chunking** стратегию
- Превосходят SOTA модели (voyage-context-3: 79.45%, Anthropic Contextual: 72.4%)

---

## Методология обучения

### Многоэтапный конвейер обучения

```
1. Диффузионное предобучение
   ↓
2. Попарное обучение (Pair Training)
   ↓
3. Контекстное обучение (Contextual Training) → pplx-embed-context-v1
   ↓
4. Триплетное обучение (Triplet Training)
   ↓
5. Слияние через SLERP → pplx-embed-v1
```

### Этап 1: Продолженное диффузионное предобучение

**Цель:** Конвертация каузального LLM в двусторонний энкодер

- **Данные:** 250B токенов на 30 языках
  - 50%: FineWebEdu (английские образовательные веб-страницы)
  - 50%: FineWeb2 и FineWeb2-HQ (29 других языков)
- **Параметры обучения:**
  - 60,000 шагов
  - Global batch size: 1024
  - Длина последовательности: 4096
  - Optimizer: AdamW с warmup-stable-decay расписанием
- **Результат:** ~1 процентный пункт улучшения над каузальной базой

### Этап 2: Попарное обучение (Pair Training)

**Цель:** Базовое семантическое выравнивание запросов и документов

- **Функция потерь:** InfoNCE contrastive loss
- **Маскирование ложных негативов:** Вдохновлено Zhang et al. (2025b)
  - Сравнивает схожесть негативных примеров с позитивной парой
  - Маскирует вклад, если негатив похож на позитив (возможно ложный негатив)
- **Три фазы:**
  1. Только английские данные
  2. Английские + кросс-лингвальные данные
  3. Полный мультиязычный датасет

### Этап 3: Контекстное обучение (Contextual Training)

**Цель:** Обучение chunk-level эмбеддингов с глобальным контекстом документа

**Двойная функция потерь:**

1. **Local loss** — захват локальной семантики чанка:
   - In-sequence contrastive loss (позитив: gold chunk, негативы: другие чанки документа)
   - In-batch contrastive loss (позитив: gold chunk, негативы: все чанки в батче)
   - Комбинация: `local_loss = α * in_sequence + (1-α) * in_batch`, где α = 0.2

2. **Global loss** — моделирование схожести запрос-документ:
   - InfoNCE objective
   - Маскирование дубликатов документов через hash-сравнение (MD5)
   - Similarity threshold masking + query-query negatives

**Расписание веса β:** Косинусное расписание от 0.2 до 0.5
- Сначала фокус на локальной семантике чанков
- Постепенное включение обучения на уровне документа

**Результат:** `pplx-embed-context-v1`

### Этап 4: Триплетное обучение (Triplet Training)

**Цель:** Обучение более дискриминативным эмбеддингам через hard negative mining

- **Вход:** N триплетов (query, позитивный документ, K hard негативов)
- **Функция потерь:** Triplet contrastive InfoNCE loss
- **Данные:** Высококачественные данные (12 датасетов)
  - 92% английские, 7% мультиязычные (15 языков), 1% код

### Этап 5: Слияние моделей

**Метод:** Spherical Linear Interpolation (SLERP)

- Слияние contextual модели и triplet checkpoint'ов
- Результат: `pplx-embed-v1`

---

## Квантизация

### Нативная INT8-квантизация

**Инновация:** Квантизация встроена в процесс обучения, а не применяется post-hoc

**Формула pooling с квантизацией:**

```
embedding = round(tanh(mean_pool(token_embeddings)) * 127)
```

- Результат: целые числа в диапазоне {-127, ..., 127}
- Backpropagation: Straight-Through Gradient Estimation (Bengio et al., 2013)
- Сравнение: Cosine similarity между квантизованными векторами

**Преимущества:**
- **4x уменьшение размера** vs FP32
- **Без потери качества** — модель обучается работать с квантизованными эмбеддингами
- Совместимость с INT8-ускорителями

### Бинарная квантизация

**Формула:**
```
binary_embedding = sign(mean_pool(token_embeddings))
```

- Результат: значения {-1, 1}
- **32x уменьшение размера** vs FP32
- **Минимальная потеря качества** при 4B масштабе (<1.6 пункта)

**Эффективность хранения:**

| Модель | Docs/MB (INT8) | Docs/MB (Binary) |
|--------|----------------|------------------|
| pplx-embed-v1-4B | 390 | 3,125 |
| pplx-embed-v1-0.6B | 976 | 7,812 |
| Qwen3-Embedding-4B | 97 | - |
| Gemini-Embedding-001 | 81 | - |

---

## Производительность

### MTEB (Multilingual, v2)

131 задача, 18 retrieval задач, 146 языков

| Модель | Параметры | MTEB (nDCG@10) |
|--------|-----------|----------------|
| **pplx-embed-v1-4B (INT8)** | 4B | **69.66%** |
| Qwen3-Embedding-4B | 4B | 69.60% |
| Gemini-Embedding-001 | - | 67.71% |
| **pplx-embed-v1-0.6B (INT8)** | 0.6B | **65.41%** |
| Qwen3-Embedding-0.6B | 0.6B | 64.65% |
| Embed-Gemma-0.3B | 0.3B | 62.58% |

**Выводы:**
- pplx-embed-v1-4B превосходит Gemini и не уступает Qwen3-4B при 4x лучшей эффективности хранения
- pplx-embed-v1-0.6B превосходит Qwen3-0.6B на всех языковых подмножествах

### MIRACL (Multilingual Information Retrieval Across Languages)

18 языков, различные скрипты

| Модель | Avg | ar | bn | de | en | es | ru | zh | ... |
|--------|-----|----|----|----|----|----|----|----|-----|
| **pplx-embed-v1-0.6B (INT8)** | **68.6** | 77.9 | 75.6 | 60.7 | 57.5 | 60.1 | 74.3 | 65.2 | ... |
| pplx-embed-v1-4B (INT8) | 66.2 | 74.5 | 74.7 | 58.9 | 55.8 | 55.2 | 71.4 | 61.3 | ... |
| Qwen3-Embedding-0.6B | 61.2 | 70.5 | 66.9 | 54.2 | 51.8 | 55.5 | 49.0 | 59.2 | ... |
| Qwen3-Embedding-4B | 69.5 | 78.6 | 78.3 | 63.0 | 59.6 | 58.9 | 68.9 | 65.1 | ... |

**Примечательно:** 0.6B модель превосходит 4B модель в среднем по MIRACL

### ConTEB (Contextual Text Embedding Benchmark)

Chunk-level retrieval с контекстом документа

| Модель | Тип | Avg | Covid | ESG | FB | Geo | Ins | MLDR | NQA | SQ |
|--------|-----|-----|-------|-----|----|----|----|----|----|----|
| **pplx-embed-context-v1-4B (INT8)** | Contextual | **81.96%** | 62.16 | 62.40 | 78.13 | 93.04 | 100 | 89.50 | 86.71 | 83.73 |
| voyage-context-3 | Contextual | 79.45% | 55.43 | 54.00 | 79.56 | 92.85 | 100 | 89.24 | 81.79 | 82.70 |
| Anthropic Contextual | Contextual | 72.40% | 60.70 | 34.80 | 53.90 | 89.40 | 100 | 85.40 | 77.70 | 77.10 |
| pplx-embed-v1-4B (INT8) | Non-contextual | 58.83% | 63.81 | 47.23 | 34.26 | 73.57 | 14.96 | 79.76 | 81.66 | 75.38 |

**Вывод:** pplx-embed-context-v1-4B устанавливает новый SOTA на ConTEB

### BERGEN (RAG Benchmark)

5 QA задач на реальных данных

- **pplx-embed-v1-4B** превосходит Qwen3-4B на 4/5 задачах
- **pplx-embed-v1-0.6B** превосходит Qwen3-4B на 3/5 задачах

**Примечательно:** 0.6B модель превосходит 4B модель конкурента

### Внутренние бенчмарки Perplexity

**PPLXQuery2Query:** Поиск похожих запросов (1B production веб-страниц)

| Модель | Recall@10 |
|--------|-----------|
| pplx-embed-v1-4B | 73.5% |
| pplx-embed-v1-0.6B | 71.1% |

**PPLXQuery2Doc:** Поиск релевантных документов

| Модель | Recall@1000 |
|--------|-------------|
| pplx-embed-v1-4B | 91.7% |

---

## Уникальные инновации

### 1. Диффузионное предобучение для энкодеров

**Первая работа**, использующая диффузионное обучение для конвертации каузальных LLM в двусторонние энкодеры для retrieval задач.

**Преимущества:**
- Захват полного_bidirectional контекста
- Улучшенное моделирование глобального контекста документа
- ~1 процентный пункт улучшения над каузальной базой

### 2. Нативная квантизация-aware тренировка

В отличие от post-hoc квантизации, pplx-embed обучается с INT8-квантизацией на всех этапах.

**Преимущества:**
- Отсутствие деградации качества
- Модель адаптируется к квантизации во время обучения
- Прямая генерация INT8 эмбеддингов на инференсе

### 3. Late Chunking для контекстных эмбеддингов

**Проблема:** Традиционные подходы разбивают документ на чанки до кодирования, теряя глобальный контекст.

**Решение pplx-embed:**
1. Кодирование полного документа целиком
2. Извлечение chunk-level эмбеддингов из закодированного документа
3. Каждый чанк сохраняет контекст всего документа

**Результат:** +23.53 пункта на ConTEB vs non-contextual версия

### 4. Branched Curriculum Training

Четыре различных парадигмы обучения в ветвящейся структуре:

```
Диффузионное предобучение
    ↓
Попарное обучение
    ├─→ Контекстное обучение → pplx-embed-context-v1
    └─→ Триплетное обучение ──┘
              ↓
        SLERP слияние → pplx-embed-v1
```

### 5. Robust бинарная квантизация на 4B масштабе

Большая размерность эмбеддингов (2560) сохраняет информацию после бинаризации:

- **4B модель:** <1.6 пункта падение (69.66% → 68.22%)
- **0.6B модель:** 2-4 пункта падение (65.41% → 61.44%)

---

## Практическое применение

### Интеграция

**Поддерживаемые фреймворки:**
- Transformers
- Sentence Transformers
- Text Embeddings Inference (TEI)
- ONNX
- Transformers.js

**Пример использования (Python):**

```python
from sentence_transformers import SentenceTransformer

# Загрузка модели
model = SentenceTransformer('perplexity-ai/pplx-embed-v1-4B')

# Кодирование запросов и документов
query_embedding = model.encode('Как работает двустороннее внимание?')
doc_embeddings = model.encode(['Документ 1', 'Документ 2', ...])

# Поиск ближайших соседей (cosine similarity)
```

### Рекомендации по выбору модели

| Сценарий | Рекомендуемая модель |
|----------|---------------------|
| **Production RAG с ограниченными ресурсами** | pplx-embed-v1-0.6B (INT8) |
| **Максимальное качество retrieval** | pplx-embed-v1-4B (INT8) |
| **Контекстный поиск по длинным документам** | pplx-embed-context-v1-4B |
| **Экстремальная эффективность хранения** | pplx-embed-v1-4B (Binary) |
| **Мультиязычные приложения** | pplx-embed-v1-4B (INT8) |

### Оптимизация для production

**Эффективность хранения:**
- INT8: 4x уменьшение vs FP32
- Binary: 32x уменьшение vs FP32
- 3,125 документов на MB (4B, binary)

**Производительность:**
- Поддержка аппаратных INT8-ускорителей
- Matryoshka Representation Learning для гибкой размерности
- Отсутствие необходимости в instruction префиксах

---

## Сравнение с аналогами

### pplx-embed vs Qwen3-Embedding

| Характеристика | pplx-embed-v1-4B | Qwen3-Embedding-4B |
|----------------|------------------|---------------------|
| MTEB (Multilingual) | 69.66% | 69.60% |
| MTEB (Code) | 78.73% | 80.07% |
| ConTEB (contextual) | 81.96%* | N/A |
| Docs/MB (INT8) | 390 | 97 |
| Квантизация | Нативная INT8 | Post-hoc |
| Instruction префиксы | Не требуются | Требуются |

*pplx-embed-context-v1-4B

**Преимущества pplx-embed:**
- 4x лучшая эффективность хранения
- Нативная квантизация без потери качества
- Контекстная версия для chunk-level retrieval
- Не требует instruction префиксов

### pplx-embed vs Gemini-Embedding-001

| Характеристика | pplx-embed-v1-4B | Gemini-Embedding-001 |
|----------------|------------------|----------------------|
| MTEB (Multilingual) | 69.66% | 67.71% |
| MTEB (Code) | 78.73% | 76.00% |
| Docs/MB (INT8) | 390 | 81 |
| Лицензия | MIT (open) | Proprietary |

---

## Связи с другими темами

- [[../embedding_models.md]] - Обзор моделей эмбеддингов для RAG
- [[../../../algorithms/neural_networks/embedders/matryoshka_representation_learning.md]] - Matryoshka Representation Learning
- [[../rag/index.md]] - Retrieval-Augmented Generation системы
- [[../rag/best_practices/embedding_models.md]] - Лучшие практики выбора эмбеддинг-моделей
- [[../../../algorithms/neural_networks/transformers/bidirectional_attention.md]] - Двустороннее внимание в трансформерах
- [[../../../algorithms/neural_networks/diffusion_models.md]] - Диффузионные модели для текста

---

## Источники

1. **Perplexity AI Research.** "pplx-embed: State-of-the-art Embedding Models for Web-Scale Retrieval." https://research.perplexity.ai/articles/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval
2. **Eslami, S., Gaiduk, M., Krimmel, M., Milliken, L., Wang, B., & Bykov, D.** "Diffusion-Pretrained Dense and Contextual Embeddings." arXiv preprint arXiv:2602.11151, 2026. https://arxiv.org/abs/2602.11151
3. **Hugging Face Collection.** "pplx-embed by Perplexity AI." https://huggingface.co/collections/perplexity-ai/pplx-embed
4. **MarkTechPost.** "Perplexity Just Released pplx-embed: New SOTA Qwen3 Bidirectional Embedding Models for Web-Scale Retrieval Tasks." https://www.marktechpost.com/2026/02/26/perplexity-just-released-pplx-embed-new-sota-qwen3-bidirectional-embedding-models-for-web-scale-retrieval-tasks/
5. **RecSys Substack.** "Semantic Search At LinkedIn, LLM-Driven Autonomous Optimization." https://recsys.substack.com/p/semantic-search-at-linkedin-llm-driven

---

## Метаданные

```metadata
category: algorithms
subcategory: neural_networks/embedders
tags: pplx-embed, embedding models, bidirectional attention, diffusion pretraining, retrieval, RAG, Qwen3, Perplexity AI, quantization, Matryoshka Representation Learning
```
