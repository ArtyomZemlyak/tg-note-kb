# Галерея архитектур LLM

## Общее описание

Галерея архитектур больших языковых моделей (LLM) представляет собой систематизированный обзор различных архитектурных подходов, используемых в современных языковых моделях. Данная галерея объединяет ключевые архитектуры, их эволюцию и взаимосвязи.

## Классификация архитектур

### 1. Базовые архитектуры трансформеров

#### Encoder-only архитектуры
Модели, использующие только энкодерную часть трансформера.

**Применение:** Задачи понимания языка, классификация, извлечение признаков

**Примеры:**
- [[bert_model.md|BERT]] - Bidirectional Encoder Representations from Transformers
- RoBERTa - оптимизированная версия BERT
- DistilBERT - дистиллированная версия для эффективности

**Ключевые характеристики:**
- Двустороннее внимание (все токены видят все токены)
- Маскированное языковое моделирование
- Отлично подходят для задач понимания контекста

**Связи:** [[../../../algorithms/neural_networks/transformers/transformer_architecture.md|Базовая архитектура трансформеров]], [[../../../algorithms/neural_networks/transformers/encoder_decoder_vs_decoder_only.md|Сравнение архитектур]]

---

#### Decoder-only архитектуры
Модели, использующие только декодерную часть трансформера.

**Применение:** Генерация текста, авторегрессивные задачи

**Примеры:**
- GPT系列 (GPT, GPT-2, GPT-3, GPT-4)
- LLaMA系列
- Mistral
- Qwen系列

**Ключевые характеристики:**
- Каузальное внимание (токены видят только предыдущие токены)
- Авторегрессивное языковое моделирование
- Идеальны для генерации текста

**Связи:** [[../autoregressive_models.md|Авторегрессивные модели]], [[../../../algorithms/neural_networks/transformers/transformer_architecture.md|Архитектура трансформеров]]

---

#### Encoder-Decoder архитектуры
Полная архитектура трансформера с энкодером и декодером.

**Применение:** Задачи преобразования текста в текст (перевод, суммаризация)

**Примеры:**
- [[../../../algorithms/neural_networks/transformers/t5.md|T5]] - Text-to-Text Transfer Transformer
- BART - Denoising Autoencoder Transformer
- [[../../../algorithms/neural_networks/transformers/t5gemma_2.md|T5Gemma 2]] - современная энкодер-декодер модель

**Ключевые характеристики:**
- Энкодер для понимания входа
- Декодер для генерации выхода
- Cross-attention между энкодером и декодером

**Связи:** [[../../../algorithms/neural_networks/transformers/encoder_decoder_vs_decoder_only.md|Сравнение архитектур]], [[../../../algorithms/neural_networks/transformers/t5.md|T5 модель]]

---

### 2. Гибридные архитектуры

#### OLMo Hybrid
Гибридная архитектура от Allen Institute for AI, комбинирующая полные слои внимания со слоями Gated DeltaNet.

**Архитектура:** Соотношение 3:1 (75% Gated DeltaNet, 25% Full Attention)

**Ключевые преимущества:**
- 2x эффективность данных (достигает тех же результатов с 49% меньше токенов)
- Линейная сложность большинства слоёв
- Превосходство на длинных контекстах (RULER @ 64k: 85,0 против 70,9)

**Связи:** [[olmo_hybrid.md|OLMo Hybrid - подробное описание]], [[../../../algorithms/neural_networks/transformers/gated_deltanet.md|Gated DeltaNet]], [[../../../algorithms/neural_networks/transformers/hybrid_architectures.md|Гибридные архитектуры]]

---

#### Гибридные архитектуры с линейным вниманием
Комбинация традиционного внимания с линейными рекуррентными моделями.

**Примеры:**
- Kimi-Linear (соотношение 3:1 KDA:MLA)
- Jamba (чередование Mamba и трансформерных слоёв)
- Qwen3-Next (гибридный подход)

**Связи:** [[../../../algorithms/neural_networks/transformers/linear_sequence_modeling.md|Линейное моделирование последовательностей]], [[../../../algorithms/neural_networks/transformers/kimi_delta_attention.md|Kimi Delta Attention]]

---

### 3. Архитектуры с иерархическим моделированием

#### ConceptLM
Фреймворк, дополняющий стандартное предсказание следующего токена задачей предсказания следующего концепта (Next Concept Prediction, NCP).

**Ключевые инновации:**
- Двухуровневая иерархия: концепты + токены
- Векторная квантизация (VQ) для дискретизации концептов
- Product Quantization для комбинаторного пространства концептов
- 37% меньше параметров или 24% меньше токенов для того же качества

**Архитектура:**
- Token-level Encoder → Concept Module → Token-level Decoder
- Фактор сжатия k=4 (один концепт на 4 токена)
- SimVQ для предотвращения коллапса кодовой книги (~100% утилизация)

**Связи:** [[conceptlm.md|ConceptLM - подробное описание]], [[../multi_token_prediction.md|Multi-Token Prediction]], [[../../world_models/jepa.md|JEPA - предсказание в латентном пространстве]]

---

### 4. Архитектуры с разреженными вычислениями

#### Mixture of Experts (MoE)
Архитектура с разреженными слоями экспертов для повышения эффективности параметров.

**Принцип работы:**
- Несколько "экспертов" (FFN слоёв)
- Сеть-шлюз для маршрутизации токенов к экспертам
- Только часть параметров активируется для каждого входа

**Примеры:**
- Switch Transformers
- GLaM
- Mixtral 8x7B

**Связи:** [[../mixture_of_experts_architecture.md|MoE архитектура - подробное описание]], [[../../../algorithms/neural_networks/transformers/transformer_architecture.md|Базовая архитектура]]

---

#### Разреженное внимание (Sparse Attention)
Механизмы внимания с разреженными матрицами для работы с длинными контекстами.

**Варианты:**
- **Mixture of Sparse Attention (MoSA)** - обучаемая маршрутизация к разреженным подмножествам токенов
- **Star Attention** - блочное разреженное внимание с ускорением
- **Log-Linear Attention** - сложность O(n log n)

**Связи:** [[../specialized_attention_mechanisms.md|Специализированные механизмы внимания]], [[../../../algorithms/neural_networks/transformers/inference_efficiency_comparison.md|Сравнение эффективности]]

---

### 5. Специализированные механизмы внимания

#### Multi-Query и Grouped-Query Attention (MQA/GQA)
Оптимизации KV-кэша для ускорения инференса.

**MQA:** Все головы используют одни и те же K и V
**GQA:** Головы разделены на группы, каждая группа имеет свои K и V

**Связи:** [[../specialized_attention_mechanisms.md|Специализированные механизмы внимания]]

---

#### Multihead Latent Attention (MLA)
Низкоранговое приближение стандартного Multihead Attention.

**Преимущества:**
- Минимизация KV-кэша
- Повышение эффективности при сохранении качества

**Связи:** [[../specialized_attention_mechanisms.md|Специализированные механизмы внимания]]

---

### 6. Инновационные архитектуры

#### Диффузионные трансформеры
Использование принципов диффузии с архитектурой трансформера для генерации.

**Принцип работы:**
- Многократное маскирование и восстановление
- Encoder-only архитектура для генерации текста

**Связи:** [[../../../ai/diffusion_models/llm_diffusion_integration.md|Диффузионные модели в LLM]], [[../../../ai/diffusion_models/architectures/text_diffusion_models.md|Текстовые диффузионные модели]]

---

#### Условные VAE-трансформеры
Интеграция вероятностного вывода через латентные переменные.

**Пример:** Free Transformer

**Связи:** [[../../../algorithms/neural_networks/transformers/free_transformer.md|Free Transformer]]

---

#### Дифференциальные трансформеры
Механизм внимания на основе разницы между представлениями токенов.

**Преимущества:**
- Улучшенное понимание относительных позиций
- Лучшее моделирование отношений между токенами

**Связи:** [[../../../algorithms/neural_networks/transformers/differential_transformer.md|Дифференциальные трансформеры]]

---

#### Дополненные памятью трансформеры (MATs)
Расширенные механизмы памяти для преодоления ограничений фиксированного контекста.

**Связи:** [[../../../algorithms/neural_networks/transformers/memory_augmented_transformers.md|MAT - систематический обзор]], [[../../../algorithms/neural_networks/transformers/mat_taxonomy.md|Таксономия MAT]]

---

## Сравнительная таблица архитектур

| Архитектура | Тип | Основные задачи | Преимущества | Примеры |
|-------------|-----|-----------------|--------------|---------|
| Encoder-only | Базовая | Понимание текста | Полный контекст | BERT, RoBERTa |
| Decoder-only | Базовая | Генерация текста | Простота, эффективность | GPT, LLaMA |
| Encoder-Decoder | Базовая | Текст-в-текст | Гибкость | T5, BART |
| OLMo Hybrid | Гибридная | Эффективность | 2x data efficiency | OLMo Hybrid 7B |
| ConceptLM | Иерархическая | Семантическое планирование | 37% меньше параметров | ConceptLM-1.5B |
| MoE | Разреженная | Масштабирование | Эффективность параметров | Mixtral, Switch Transformer |
| Sparse Attention | Разреженная | Длинные контексты | O(n log n) сложность | MoSA, Star Attention |
| Diffusion Transformer | Инновационная | Генерация | Альтернативный подход | LLM Diffusion |

---

## Визуализация эволюции архитектур

```
2017: Transformer (Attention is All You Need)
    │
    ├──→ 2018: BERT (Encoder-only)
    ├──→ 2018: GPT (Decoder-only)
    │       └──→ GPT-2, GPT-3, GPT-4, LLaMA...
    │
    ├──→ 2019: T5 (Encoder-Decoder)
    │
    ├──→ 2020-2022: Специализированные архитектуры
    │       ├──→ MoE (Switch Transformer)
    │       ├──→ Sparse Attention
    │       └──→ Efficient Attention (MQA, GQA)
    │
    └──→ 2023-2026: Гибридные и инновационные
            ├──→ OLMo Hybrid (Attention + Gated DeltaNet)
            ├──→ ConceptLM (NCP + NTP)
            ├──→ Diffusion Transformers
            └──→ Memory-Augmented Transformers
```

---

## Ключевые тренды развития

### 1. Эффективность
- Переход от плотных к разреженным вычислениям
- Гибридные архитектуры для баланса качества и скорости
- Оптимизация KV-кэша и памяти

### 2. Длинные контексты
- Разреженное внимание для работы с длинными последовательностями
- Иерархическое моделирование
- Дополненные памятью архитектуры

### 3. Иерархичность
- Предсказание на уровне концептов (ConceptLM)
- Многоуровневые представления
- Разделение семантики и синтаксиса

### 4. Универсальность
- Мультимодальные архитектуры
- Единые архитектуры для разных задач
- Адаптивные механизмы

---

## Связи с другими темами

- [[../../../algorithms/neural_networks/transformers/transformer_architecture.md|Архитектура трансформеров]] - базовое описание архитектуры трансформеров
- [[../../../algorithms/neural_networks/transformers/evolution_and_connection_of_transformer_architectures.md|Эволюция архитектур трансформеров]] - подробный обзор эволюции и взаимосвязей
- [[../../../algorithms/neural_networks/transformers/encoder_decoder_vs_decoder_only.md|Сравнение encoder-decoder и decoder-only]] - детальное сравнение архитектур
- [[../llm_architectures_comparison.md|Сравнение архитектур LLM]] - общее сравнение различных архитектур
- [[../specialized_attention_mechanisms.md|Специализированные механизмы внимания]] - подробное описание оптимизаций внимания
- [[../mixture_of_experts_architecture.md|Mixture of Experts]] - архитектура с разреженными экспертами
- [[../../../algorithms/neural_networks/transformers/hybrid_architectures.md|Гибридные архитектуры]] - общее описание гибридных подходов
- [[../../../algorithms/neural_networks/transformers/next_gen_transformer_architectures.md|Архитектуры следующего поколения]] - перспективные разработки 2024-2025
- [[../../computer_vision/vision_transformer.md|Vision Transformer]] - применение трансформеров в компьютерном зрении

---

## Источники

1. **Входящая заметка:** "Галерея архитектуры разных LLM-моделей" - пользовательское сообщение, 2026

2. **Vaswani, A., et al. (2017).** Attention is All You Need. *arXiv preprint arXiv:1706.03762*. [URL](https://arxiv.org/abs/1706.03762)

3. **Devlin, J., et al. (2018).** BERT: Pre-training of Deep Bidirectional Transformers. *arXiv preprint arXiv:1810.04805*. [URL](https://arxiv.org/abs/1810.04805)

4. **Brown, T., et al. (2020).** Language Models are Few-Shot Learners (GPT-3). *arXiv preprint arXiv:2005.14165*. [URL](https://arxiv.org/abs/2005.14165)

5. **Raffel, C., et al. (2019).** Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5). *arXiv preprint arXiv:1910.10683*. [URL](https://arxiv.org/abs/1910.10683)

6. **AllenAI (2025).** OLMo Hybrid: Combining transformers and linear RNNs. [URL](https://allenai.org/blog/olmohybrid)

7. **Liu, Y., et al. (2026).** Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models (ConceptLM). *arXiv preprint arXiv:2602.08984*. [URL](https://arxiv.org/abs/2602.08984)

8. **Fedus, W., et al. (2021).** Switch Transformers: Scaling to Trillion Parameter Models. *arXiv preprint arXiv:2101.03961*. [URL](https://arxiv.org/abs/2101.03961)

---

## Дополнительные материалы

- [[../../../algorithms/neural_networks/transformers/interactive_visualization_tools.md|Инструменты визуализации трансформеров]] - интерактивные визуализации архитектур
- [[../../../algorithms/neural_networks/transformers/speed_always_wins_survey.md|Speed Always Wins Survey]] - обзор эффективных архитектур
- [[../../../algorithms/neural_networks/transformers/state_space_models.md|State Space Models]] - альтернативный подход к моделированию последовательностей

```metadata
category: искусственный_интеллект
subcategory: языковые_модели
tags: LLM, архитектуры, галерея, трансформеры, encoder-decoder, гибридные модели, эффективность, сравнение, классификация
```
