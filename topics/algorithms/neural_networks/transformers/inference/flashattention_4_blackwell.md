# FlashAttention-4: Алгоритм и Co-Design для Blackwell GPU

## Общее описание

**FlashAttention-4** — это оптимизированная версия алгоритма внимания для архитектуры NVIDIA Blackwell (B200, GB200), представленная в 2026 году. Алгоритм решает проблему **асимметричного масштабирования hardware**, при котором пропускная способность tensor cores удваивается, а другие функциональные единицы (shared memory bandwidth, exponential units) масштабируются медленнее или остаются неизменными.

## Авторы и источник

- **Авторы:** Ted Zadouri, Markus Hoehnerbach, Jay Shah, Timmy Liu, Vijay Thakkar, Tri Dao
- **Организации:** Princeton University, Meta, Colfax Research, NVIDIA, Georgia Tech, Together AI
- **Публикация:** arXiv:2603.05451, 2026
- **Код:** https://github.com/Dao-AILab/flash-attention/tree/main/flash_attn/cute

## Проблема: Асимметричное масштабирование hardware

### Контекст
Архитектура Blackwell представляет новое поколение GPU с фундаментально отличными характеристиками по сравнению с Hopper (H100):

| Компонент | Hopper H100 | Blackwell B200 | Изменение |
|-----------|-------------|----------------|-----------|
| Tensor core throughput (FP16/BF16) | 1 PFLOPS | 2.25 PFLOPS | **2.25×** |
| Shared memory bandwidth | 128 bytes/clock/SM | 128 bytes/clock/SM | **1×** (без изменений) |
| Exponential unit throughput | 16 ops/clock/SM | 16 ops/clock/SM | **1×** (без изменений) |
| MMA tile size | 64×128 | 128×128 | **2×** |
| Tensor memory (TMEM) | Нет | 256 KB/SM | **Новое** |

### Roofline анализ
Для типичных рабочих нагрузок attention на Blackwell **shared memory traffic и exponential operations доминируют** над MMA compute на 25-60%:

| Ресурс | Tile 128³ (cycles) | Tile 256×128² (cycles) |
|--------|-------------------|------------------------|
| MMA compute | 1024 | 2048 |
| Shared memory | 768 | 1536 |
| Exponential unit | 1024 | 2048 |

Это означает, что простое портирование существующих алгоритмов (FlashAttention-3) на Blackwell оставляет значительную производительность нереализованной.

## Ключевые инновации FlashAttention-4

### 1. Переработанный pipeline для максимального overlap

**Forward pass:**
- Использует ping-pong schedule с двумя tiles на thread block
- Пока tensor core операции выполняются для одного tile, softmax вычисляется для другого
- Blackwell tensor cores записывают аккумуляторы напрямую в **tensor memory (TMEM)** асинхронно
- Каждый thread обрабатывает целую строку (128 элементов), устраняя необходимость в inter-warp shuffles
- Два softmax warpgroups синхронизированы для предотвращения overlap в критической секции (exponential computation)
- Rescaling output вынесен в отдельный 'correction' warpgroup вне critical path

**Backward pass:**
- Использует **2-CTA MMA mode** для уменьшения shared memory traffic
- Каждый CTA stages и loads половину operand B, уменьшая redundant shared memory capacity и bandwidth
- Реструктурированный dQ step уменьшает количество atomic reductions вдвое
- Поддержка **детерминированного режима** с минимальным overhead для reproducible training (RL applications)

### 2. Software-эмуляция экспоненты (Exponential Unit Bottleneck Mitigation)

**Проблема:** MUFU (multi-function unit) имеет пропускную способность 16 ops/clock/SM vs 8192 ops/clock/SM для tensor cores.

**Решение:** Эмуляция 2^x через полиномиальную аппроксимацию на FMA units, работающих параллельно с MUFU.

**Алгоритм (Cody-Waite range reduction):**
```
2^x = 2^⌊x⌋ × 2^(x-⌊x⌋)
```

1. **Целая часть** 2^⌊x⌋ вычисляется через битовые манипуляции IEEE 754 (shift exponent bits)
2. **Дробная часть** 2^(x_frac) аппроксимируется полиномом:
   ```
   p(x) = p₀ + p₁x + p₂x² + ... + pₙxⁿ
   ```
   где коэффициенты минимизируют относительную ошибку на [0, 1)

**Точность (BF16 vs FP64):**
| Метод | Max rel err | Mean rel err |
|-------|-------------|--------------|
| Ideal (FP64→BF16) | 3.89×10⁻³ | 1.41×10⁻³ |
| Hardware MUFU.EX2 | 3.89×10⁻³ | 1.41×10⁻³ |
| Degree 3 polynomial | 3.90×10⁻³ | 1.41×10⁻³ |
| Degree 4 polynomial | 3.89×10⁻³ | 1.41×10⁻³ |
| Degree 5 polynomial | 3.89×10⁻³ | 1.41×10⁻³ |

**Результат:** Полином степени 3-4 достигает точности hardware MUFU при значительном увеличении throughput.

### 3. Conditional Softmax Rescaling

**Идея:** Пропускать ненужные операции rescaling, когда они не влияют на результат.

**Реализация:**
- Анализ статистики row max и sum перед выполнением rescaling
- Skip rescaling если изменение незначительно
- Уменьшение количества non-matmul операций

### 4. Использование Tensor Memory (TMEM) и 2-CTA MMA Mode

**Tensor Memory (TMEM):**
- 256 KB on-chip памяти на SM
- Warp-synchronous, tightly coupled с tensor cores
- MMA units записывают напрямую в TMEM без потребления registers
- Альтернатива register file для alleviating register pressure

**2-CTA MMA Mode:**
- Два CTA в одном thread block cluster cooperatively execute single MMA
- Поддержка M = 128 или 256 (vs M = 128 для single CTA)
- Каждый CTA stages только половину B в своём shared memory
- Уменьшение redundant shared memory capacity и bandwidth
- Требует запуска CTAs фиксированными парами

### 5. Улучшенное scheduling и resource allocation

- Новые CTA scheduling strategies для Blackwell
- Register allocation schemes для больших tile sizes (128×128)
- Оптимизация partitioning tensor memory для S, P, и accumulator tiles

## Производительность

### Benchmark результаты на B200 GPU (BF16)

| Метрика | Значение |
|---------|----------|
| **Speedup над cuDNN 9.13** | до **1.3×** |
| **Speedup над Triton** | до **2.7×** |
| **Пиковая производительность** | до **1613 TFLOPs/s** |
| **Utilization** | до **71%** (теоретический максимум) |

### Сравнение с другими реализациями

| Реализация | Производительность (TFLOPs/s) | Utilization |
|------------|-------------------------------|-------------|
| FlashAttention-4 (B200) | 1613 | 71% |
| FlashInfer MoE FP4 (B200) | 1225 | ~54% |
| SGLang MoE FP4 (B200) | 1262 | ~56% |
| vLLM MoE FP4 (B200) | 1117 | ~50% |

## Реализация на CuTe-DSL

**CuTe-DSL** (CUDA Template DSL) — domain-specific language embedded в Python для написания CUDA kernels.

### Преимущества CuTe-DSL для FlashAttention-4:

| Характеристика | CuTe-DSL (Python) | C++ Templates |
|----------------|-------------------|---------------|
| **Время компиляции** | 20-30× быстрее | Медленно |
| **Expressivity** | Полная | Полная |
| **Developer productivity** | Высокая | Низкая |
| **Barrier to entry** | Низкий | Высокий (требуется expertise в C++ template metaprogramming) |

**Возможности:**
- Rapid prototyping новых attention variants
- Полная выразительность для сложных kernel optimizations
- Значительное улучшение developer productivity

## Архитектурные особенности Blackwell

### Memory Hierarchy
```
Global Memory (GMEM/HBM) → L2 Cache → Shared Memory (SMEM) → Register File (RMEM)
                                    ↓
                              Tensor Memory (TMEM) — 256 KB/SM
```

### Thread Hierarchy
```
Threads → Warps (32 threads) → Warpgroups (4 warps) → CTAs → Clusters → Grid
```

### Tensor Cores (5th Generation)
- Tile size: **128×N** (N = 128 или 256)
- Асинхронная запись в TMEM
- 2-CTA mode для cooperative MMA execution

## Сравнение с предыдущими версиями

| Версия | Год | Целевая архитектура | Ключевые особенности |
|--------|-----|---------------------|----------------------|
| FlashAttention-1 | 2022 | General GPU | Тайлинг и kernel fusion |
| FlashAttention-2 | 2023 | General GPU | Параллелизация по sequence length |
| FlashAttention-3 | 2024 | Hopper (H100) | Warp specialization, FP8, async execution |
| FlashAttention-4 | 2026 | Blackwell (B200/GB200) | Co-design для asymmetric scaling, TMEM, 2-CTA MMA, software emulated exp |

## Применение и интеграция

### Текущее состояние
- **Open source:** Да, permissive license
- **Интеграция:** В процессе интеграции с популярными библиотеками
- **Фреймворки:** Реализация в CuTe-DSL (Python)

### Потенциальные применения
- Обучение LLM на Blackwell GPUs
- Инференс с длинными контекстами
- Reinforcement learning (детерминированный режим)
- High-performance computing для attention-based моделей

## Связи с другими темами

- [[flash_attention_and_grouped_mechanisms.md]] — Общее описание FlashAttention и групповых механизмов (GQA, MQA)
- [[specialized_attention_mechanisms.md]] — Обзор специализированных механизмов внимания
- [[inference/blackwell_fp4_moe_optimization.md]] — Оптимизация FP4 кернелов для MoE на Blackwell
- [[llm_tools/flashinfer.md]] — FlashInfer библиотека с поддержкой Blackwell
- [[llm_tools/nvfp4_format.md]] — NVFP4 формат квантования для Blackwell
- [[gpu_memory_management.md]] — Управление GPU памятью
- [[inference_optimization/index.md]] — Оптимизация инференса LLM

## Источники

- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling** – arXiv:2603.05451, 2026. URL: https://www.arxiv.org/abs/2603.05451
- **FlashAttention** – Dao et al., NeurIPS 2022.
- **FlashAttention-2** – Dao, ICML 2023.
- **FlashAttention-3** – Shah et al., 2024.
- **NVIDIA Blackwell Architecture** – NVIDIA technical documentation, 2024.

## Медиа

![FlashAttention-4 Forward Pipeline](../../../../../media/doc_1773068117_7c053b2b_arxiv_2603.05451.pdf)

**Описание:** Схема pipeline forward pass FlashAttention-4, показывающая overlap между MMA операциями, softmax computation, и memory operations. Верхний индекс H обозначает матрицы для 'high' Q tile, L — для 'low' Q tile. Каждый Q tile соответствует 128 query tokens.
