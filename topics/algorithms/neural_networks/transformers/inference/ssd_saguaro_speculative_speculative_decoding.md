# Speculative Speculative Decoding (SSD) и Saguaro

## Описание

**Speculative Speculative Decoding (SSD)** — это инновационный алгоритм ускорения инференса больших языковых моделей, разработанный Tanishq Kumar, Tri Dao и Avner May из Stanford University, Princeton University и Together AI. SSD устраняет последовательную зависимость между спекуляцией и верификацией в традиционном спекулятивном декодировании, позволяя этим операциям выполняться параллельно на разном оборудовании.

**Saguaro** — оптимизированная реализация SSD, достигающая ускорения до **2x быстрее оптимизированного спекулятивного декодирования** (vLLM/SGLang + SpecDec) и до **5x быстрее авторегрессивного декодирования**.

## Ключевая проблема традиционного Speculative Decoding

В обычном спекулятивном декодировании существует последовательная зависимость:
- Draft-модель генерирует токены → Верификатор проверяет → Draft-модель ждет → Повтор

**SSD устраняет эту зависимость**: пока верификатор проверяет токены из раунда T, draft-модель уже предсказывает исходы верификации и заранее готовит спекуляции для раунда T+1.

## Принцип работы SSD

### Основная идея
1. **Параллелизация**: Speculator и Verifier работают параллельно на разном оборудовании
2. **Предварительное предсказание**: Draft-модель предсказывает наиболее вероятные исходы верификации (включая бонус-токен)
3. **Кэширование спекуляций**: Для каждого предсказанного исхода заранее готовится спекуляция и сохраняется в "speculation cache"
4. **Мгновенная выдача**: Если фактический исход верификации совпадает с предсказанным, спекуляция возвращается немедленно без overhead

### Алгоритм SSD
```
Function speculator(prompt, primary_draft, backup_draft):
    primary_draft.prefill(prompt)
    spec_tokens ← primary_draft.speculate(prompt)
    
    while True do:
        SEND spec_tokens to verifier
        
        # Предсказание исходов верификации (Section 4.1)
        verification_outcomes ← predict_verify_outcomes(spec_tokens, primary_draft)
        
        # Подготовка спекуляций для всех исходов (Section 4.2)
        cache ← speculate_for_outcomes(outcomes, primary_draft)
        
        WAIT TO RECEIVE verify_outcome from verifier
        
        if verify_outcome ∈ cache then:
            spec_tokens ← cache[verify_outcome]  # Cache hit!
        else:
            spec_tokens ← fallback_speculate(verify_outcome, primary_spec, backup_spec)  # Section 4.3
```

## Три ключевые проблемы SSD и решения Saguaro

### 1. Предсказание исходов верификации (Saguaro Cache)

**Проблема**: Пространство возможных исходов верификации огромно — примерно (K+1) × V, где K — длина спекуляции, V — размер словаря.

**Решение Saguaro**: Формулировка как задача ограниченной оптимизации + **геометрический fan-out**.

#### Геометрический fan-out (Theorem 12)
Оптимальное распределение бюджета кэша B по позициям следует геометрической прогрессии:

```
F_k = min(B, F_0 × a^k)
```

где:
- `F_k` — количество предсказаний бонус-токена на позиции k
- `a` — acceptance rate draft-модели
- `F_0` выбирается так, чтобы Σ F_k = B

**Интуиция**: Вероятность принятия k токенов убывает геометрически, поэтому не стоит тратить вычисления на предсказание бонус-токена на позициях с низкой вероятностью принятия.

**Точность предсказания**: До **90%** для бонус-токена.

### 2. Баланс между Acceptance Rate и Cache Hit Rate (Saguaro Sampling)

**Проблема**: Бонус-токен выбирается из residual distribution `r(·) ∝ max(p_target(·) - p_draft(·), 0)`, которую трудно предсказать, особенно при высоких температурах.

**Решение Saguaro**: **Cache-aware sampling scheme** — модификация схемы сэмплирования draft-модели для упрощения предсказания residual distribution.

#### Принцип работы
- Уменьшаем вероятность наиболее вероятных токенов draft при сэмплировании
- Это увеличивает вероятность этих токенов в residual distribution
- Бонус-токен становится легче предсказать

**Trade-off**: Смещение draft distribution может снизить acceptance rate, но увеличивает cache hit rate. Saguaro находит оптимальный баланс.

### 3. Стратегия Fallback (Saguaro Fallback)

**Проблема**: При cache miss необходимо быстро подготовить спекуляцию, иначе теряются преимущества асинхронности.

**Решение Saguaro**: **Адаптивная стратегия по batch size**:

| Batch Size | Fallback Strategy |
|------------|-------------------|
| Малый (b < b*) | Primary speculator = Backup speculator |
| Большой (b > b*) | Low-latency speculator (быстрый, но менее точный) |

**Критический размер batch b***: Выводится теоретически (Corollary 16), определяет точку переключения стратегии.

## Теоретические результаты

### Theorem 7: Speedup относительно авторегрессивного декодирования
```
Speedup_AR = (p_hit × E_hit + (1 - p_hit) × E_miss) / (p_hit × T_p + (1 - p_hit) × T_b)
```

где:
- `E_hit`, `E_miss` — ожидаемое количество сгенерированных токенов
- `T_p`, `T_b` — время primary и backup speculator относительно verifier

### Corollary 8: Строго быстрее SD
SSD с primary и backup = M работает не хуже SD (строго лучше если p_hit > 0, T_SD > 0).

### Corollary 9: Bounds speedup над SD
```
(1 + T_SD) / (1 + T_SD × (1 - p_hit)) × (E_hit / E_SD) ≤ Speedup_SD ≤ (1 + T_SD) × (E_hit / E_SD)
```

**Интуиция**: Максимальное ускорение пропорционально:
1. Сокращению latency от скрытия draft latency `(1 + T_SD)`
2. Увеличению ожидаемого количества токенов `(E_hit / E_SD)`

## Экспериментальные результаты

### Setup
- **Модели**: Llama-3 (основной текст), Qwen-3 (Appendix F)
- **Датасеты**: Alpaca, GSM8k, UltraFeedback, HumanEval
- **Hardware**: 
  - Target: 4×H100
  - Draft (SSD): 1×H100 (отдельное устройство)
  - Draft (SD): collocated на том же hardware

### Ключевые метрики
| Метрика | Значение |
|---------|----------|
| Speedup vs SD | до 2x |
| Speedup vs AR | до 5x |
| Cache hit rate | до 90% (prediction accuracy) |
| Улучшение Pareto frontier | Latency-Throughput |

### Влияние температуры
Геометрический fan-out показывает преимущество над uniform strategy особенно при высоких температурах, где SD и uniform начинают деградировать.

## Сравнение с другими методами

| Метод | Параллелизм | Верификатор compute | Fallback | Batch size |
|-------|-------------|---------------------|----------|------------|
| **SSD (Saguaro)** | Полный (асинхронный) | Без изменений | Адаптивный | Любой |
| Speculative Decoding | Нет (последовательный) | Без изменений | N/A | Любой |
| AMUSD/PEARL | Частичный (только all-accept) | Без изменений | N/A | Малый |
| SwiftSpec | Частичный (tree cache) | Без изменений | Just-in-time | Малый/Средний |
| SpecBranch | Частичный (single branch) | Без изменений | Static | Малый/Средний |
| Tree-based SD | Нет (последовательный) | Высокий | N/A | Любой |

### Преимущества SSD над tree-based методами
1. **Нет дополнительного verifier compute** — весь tree должен быть проверен в target forward pass
2. **Масштабирование speculation compute** — pre-speculation для многих исходов параллельно
3. **Комбинируемость** — SSD можно комбинировать с tree-based подходами

## Интеграция с улучшенными draft архитектурами

SSD совместим с современными архитектурами draft-моделей:

- **EAGLE-3**: Draft использует representations target model
- **GliDe/LongSpec**: Cross-attention на KV cache target
- **Diffusion LLMs**: Параллельная генерация токенов
- **SSM (State Space Models)**: Быстрая последовательная обработка

## Практическое применение

### Когда использовать SSD
- Latency-critical приложения (real-time inference)
- Доступно отдельное hardware для draft model
- Batch size ≤ критического порога

### Ограничения
- **Throughput-bound workloads**: RL в большом масштабе, offline генерация — SSD добавляет verification overhead
- **Hardware требования**: Нужно отдельное устройство для draft model (в SSD конфигурации)

## Связанные темы
- [[speculative_decoding.md]] — основы спекулятивного декодирования, базовый алгоритм, который SSD делает асинхронным
- [[eagle_speculative_decoding.md]] — продвинутая draft архитектура с tree-based спекуляцией, совместимая с SSD для дополнительной оптимизации
- [[vllm_inference_optimization.md]] — оптимизация vLLM, сравнивается с SSD по производительности (SSD до 2x быстрее vLLM + SpecDec)
- [[speculative_diffusion_decoding.md]] — использование диффузионных моделей как draft, альтернативная архитектура для SSD
- [[lk_losses_speculative_decoding.md]] — оптимизация acceptance rate через LK losses, ортогональна оптимизациям SSD
- [[radar_rl_dynamic_draft_trees.md]] — RL для динамических деревьев спекуляций, может комбинироваться с SSD
- [[block_verification_speculative_decoding.md]] — проверка целых блоков токенов, комплементарный подход к верификации

## Источники
- **Kumar T., Dao T., May A.** "Speculative Speculative Decoding" — arXiv:2603.03251, март 2026
- GitHub: https://github.com/tanishqkumar/ssd
- arXiv: https://arxiv.org/abs/2603.03251

## Дополнительные материалы
- Leviathan Y. et al. "Fast Inference from Transformers via Speculative Decoding" (2023)
- Chen Z. et al. "Speculative Decoding for Large Language Models" (2023)
- Appendix A-F оригинальной статьи содержат детальные доказательства и дополнительные эксперименты
