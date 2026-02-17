# CoPE-VideoLM: Codec Primitives For Efficient Video Language Models

## Краткое описание

**CoPE-VideoLM** (Codec-aware Primitives for Efficient Video Language Models) — это фреймворк токенизации для видео-языковых моделей (VideoLMs), который заменяет плотное RGB-кодирование на легковесные структурированные представления, полученные из примитивов видеокодеков. Подход использует нативную структуру видеокодеков (MPEG-4, H.264, HEVC) для эффективной обработки видео без необходимости полного декодирования каждого кадра.

**Ключевые преимущества:**
- **Сокращение токенов на 93%** по сравнению со стандартными VideoLMs
- **Сокращение time-to-first-token (TTFT) на 86%**
- Сохранение или превышение производительности на 14 бенчмарках видео-понимания
- Возможность масштабирования на длинные видео без превышения лимитов контекста

## Архитектура

### GOP-based Токенизация

CoPE-VideoLM использует структуру **Group of Pictures (GOP)** для эффективной кодек-ориентированной токенизации:

| Тип кадра | Обработка | Выход |
|-----------|-----------|-------|
| **I-frames** (intra-coded) | Стандартный замороженный vision encoder (φ_RGB) | Плотные RGB-токены (M токенов) |
| **P-frames** (predictive) | Легковесный Δ-Encoder (φ_Δ) получает motion vectors и residuals | Компактные Δ-токены (N ≪ M токенов) |
| **B-frames** (bi-directional) | Не используются (требуют будущих кадров, не подходят для causal processing) | — |

### Δ-Encoder (Delta Encoder)

Δ-Encoder обрабатывает примитивы кодеков через две специализированные ветви:

1. **Ветвь motion vectors (τ)**:
   - Motion vectors τ(t) ∈ ℤ^(H×W×2) описывают блочные перемещения между кадрами
   - Обрабатываются через multi-layer MLP для извлечения локальных признаков
   - Сжимаются через motion transformer (θ_motion) с K_τ learnable query токенами
   - Выход: K_τ сжатых motion токенов (τ_tok ∈ ℝ^(K_τ×d))

2. **Ветвь residuals (δ)**:
   - Residuals δ(t) ∈ ℝ^(H×W×C) capture блочные пиксельные коррекции после motion compensation
   - Встраиваются через lightweight ResNet-18 модуль
   - Сжимаются через residual transformer (θ_residual) с K_δ learnable query токенами
   - Выход: K_δ сжатых residual токенов (δ_tok ∈ ℝ^(K_δ×d))

**На практике:** K_τ = K_δ = 4, следовательно N = 8 токенов на P-frame (против M ≈ 576-1024 токенов на I-frame)

### P-frame Fusion

Для дополнительного сокращения токенов можно объединять s последовательных P-frames:

- **Пример:** 30 FPS видео с GOP size 240 кадров (8 секунд)
  - Полная обработка: M + 239×N токенов на GOP
  - С fusion s=30 (эффективно 1 FPS): M + 7×N токенов на GOP
  - Для сравнения: 8×M токенов при RGB-кодировании на 1 FPS

### Interleaved Token Stream

Финальная визуальная последовательность для LLM — упорядоченная конкатенация I-frame и P-frame токенов:

```
X = [X_I(1), X_P(2), X_P(3), ..., X_I(T), ...]
```

LLM потребляет эти токены вместе с текстовыми инструкциями без каких-либо архитектурных модификаций.

## Обучение

### Этап 1: Pre-training Δ-Encoder

Цель: выровнять Δ-токены с пространством image encoder через patch-wise регрессию.

**Дополнительные модули для pre-training:**
1. **Reference transformer (θ_ref)**: Использует image токены из I(t-1) и compressed motion vector токены τ_tok для понимания движения информации в изображении
2. **Warped transformer (θ_warped)**: Принимает enriched токены и residual токены δ_emb для добавления residual информации

**Функция потерь:**
```
L_align = Σ ||X_I(t) - ˆX_P(t)||²
```
где X_I(t) = φ_RGB(Î(t)) — токены ground-truth target frame.

Этот fine-grained objective обеспечивает пространственно-согласованное выравнивание across patches.

### Этап 2: Fine-tuning VideoLM

После pre-training:
- Δ-encoder интегрируется в VideoLM pipeline
- Reference-conditioned ветви (Reference/Warped) **не используются** (не требуется обработка RGB reference frames для P-frames)
- Стандартное instruction tuning с next-token prediction loss
- Значительное сокращение compute и memory

## Результаты

### Эффективность

| Метрика | Улучшение |
|---------|-----------|
| Сокращение токенов | До **93%** |
| Сокращение TTFT | До **86%** |
| Производительность | Сохраняется или превышает baseline |

### Бенчмарки (14 total)

CoPE-VideoLM валидирован на 14 разнообразных бенчмарках видео-понимания:

| Категория | Бенчмарки |
|-----------|-----------|
| **General Video QA** | PerceptionTest, NExT-QA, ActNet-QA, VideoMME, MVBench |
| **Temporal Reasoning & Motion** | TempCompass, Tomato, CVRR-ES, Video-TT |
| **Long-form & Instruction-Following** | Video-MMMU, LVBench, LongVideoBench |
| **Spatial Scene Understanding** | (включено в вышеперечисленные) |

**Base Model для сравнения:** LLaVA-Video-7B (evaluations via lmms-eval)

## Сравнение с другими подходами

### Token Compression Methods

| Метод | Подход | Ограничения |
|-------|--------|-------------|
| **Heuristic** (uniform downsampling, pooling) | Rule-based feature reduction | Игнорируют temporal redundancy |
| **Learnable** (Q-Former, Perceiver Resampler) | Compact latent representations | Требуют dense RGB frame encodings |
| **Attention-based** (FastV, PyramidDrop, SparseVLM) | Token pruning via attention sparsity | Post-hoc удаление информации |
| **CoPE-VideoLM** | Native codec representation | **Inherently encodes only meaningful temporal changes** |

### Compressed Video Representation

| Метод | Подход | Отличие от CoPE-VideoLM |
|-------|--------|-------------------------|
| **CoViAR, TEAM-Net** | Separate 2D CNNs на I/P-frames | Игнорируют inter-modal dependencies |
| **CV-C3D, DMCNet** | 3D CNNs, optical-flow-guided distillation | Higher inference latency |
| **CompressedVideoMAE** | Masked autoencoding в compressed domain | Pre-training только |
| **Video-LaVIT** | Discretizes motion vectors into language-like tokens | Только motion vectors, нет residuals |
| **EMA** | Aggregates I-frames + motion vectors в fixed-length summary | Discards residuals, fixed summary |
| **CoPE-VideoLM** | **Unified codec-native representation** | **Variable-length, temporally ordered, сохраняет motion + appearance signals** |

## Применение

CoPE-VideoLM подходит для:

- **Длинных видео:** Масштабирование на часы видео без превышения контекстных лимитов
- **Real-time приложений:** Низкий TTFT критичен для user experience и robotics
- **Video question-answering:** Понимание макро-событий и микро-деталей
- **Temporal reasoning:** Точное локализование событий во времени
- **Video retrieval:** Эффективный поиск по видеоконтенту
- **Action recognition:** Распознавание действий по motion patterns

## Ограничения

- **Зависимость от codec format:** Требует доступа к compressed video stream (motion vectors, residuals)
- **P-frame dependency:** P-frames определены относительно предыдущих кадров, пропуск кадров invalidates зависимости
- **GOP structure:** Максимальное fusion bounded by GOP size (обычно 5-10 секунд)

## Связи с другими темами

- [[../../vlm_models.md]] — Общая информация о визуально-языковых моделях (VLM)
- [[../../../algorithms/neural_networks/transformers/inference/token_level_scheduling.md]] — Токен-уровневое планирование в трансформерах
- [[../../generative_models/video_generation.md]] — Генерация видео, альтернативный подход к обработке видео
- [[../../../algorithms/specialized/computer_vision/feature_adaptation/efficient_visual_encoder_adaptation.md]] — Эффективная адаптация визуальных энкодеров

## Источники

1. **CoPE-VideoLM Paper** — arXiv:2602.13191, "CoPE-VideoLM: Codec Primitives For Efficient Video Language Models", Sayan Deb Sarkar et al., Stanford University, Microsoft Spatial AI Lab, ETH Zurich, 2026
   - URL: https://arxiv.org/pdf/2602.13191
   - Project page: https://sayands.github.io/cope/

2. **CoPE-VideoLM Project Page** — Официальная страница проекта с визуализацией архитектуры и результатов
   - URL: https://sayands.github.io/cope/

3. **Media file** — doc_1771315587_fb5daf86_arxiv_2602.13191.pdf (OCR extracted text)
   - [[../../../../media/doc_1771315587_fb5daf86_arxiv_2602.13191.md]] — Исходный PDF с OCR-распознанным текстом статьи

## Дополнительные материалы

- **Code:** TBA (announced)
- **Demo:** TBA
- **Related work:** Video-LaVIT, EMA, CompressedVideoMAE, CoViAR
