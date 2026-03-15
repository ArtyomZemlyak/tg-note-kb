# AutoResearch-RL: Автономное исследование архитектур с обучением с подкреплением

## Краткое описание

**AutoResearch-RL** — фреймворк, в котором агент на основе обучения с подкреплением (RL) проводит открытое исследование нейронных архитектур и гиперпараметров без человеческого надзора, работая перпетуально до сигнала о сходимости или исчерпания ресурсов.

**Ключевая идея:** Формализация «петли автоисследования» как MDP (Markov Decision Process), где агент на базе трансформера с PPO предлагает диффы к коду, запускает обучение на фиксированное время, получает награду в виде улучшения val-bpb и обновляет политику.

**Основное преимущество:** Модуль самооценки, который каждые 30 секунд фитит степенной закон на кривую лосса и предсказывает финальный bpb, позволяя прерывать бесперспективные обучения досрочно — это даёт **2.4× больше экспериментов** за то же время.

---

## Основная информация

### Формулировка задачи как MDP

Исследовательский MDP определяется как **M = (S, A, T, R, γ)**:

- **Состояние s_t ∈ S**: конкатенация (i) текущего исходного кода c_t, (ii) истории экспериментов h_t = {(c_i, r_i)}_{i<t}, (iii) системных диагностик d_t (память GPU, elapsed wall time)
- **Действие a_t ∈ A**: структурированный diff (insert/replace/delete), применяемый к c_t, yielding c_{t+1}
- **Переход T(s_{t+1}|s_t, a_t)**: детерминистическое обновление кода с последующей стохастической динамикой обучения
- **Награда r_t = R(s_t, a_t) = -∆bpb_t + λ_eff * η_t**, где ∆bpb_t = bpb_{t-1} - bpb_t — улучшение validation bits-per-byte, η_t — бонус за эффективность вычислений
- **Дисконт-фактор γ ∈ [0, 1)**: контролирует trade-off между краткосрочными выгодами и долгосрочной оптимизацией

### Метрика Bits-Per-Byte (bpb)

Валидация bits-per-byte (**val-bpb**) используется как основной сигнал награды:

```
bpb = L_CE / (log(2) * |x_i|_bytes)
```

где |x_i|_bytes — длина токена в байтах UTF-8. Эта метрика **токенизаторно-агностическая**, что делает её справедливой для экспериментов с разным размером словаря.

### Фиксированный бюджет времени

Критический дизайн: фиксированный wall-clock бюджет **T_max = 300s** на эксперимент (исключая JIT compilation и data loading). Это гарантирует, что все конфигурации получают идентичные вычисления и напрямую сравнимы по val-bpb.

---

## Архитектура агента

### Политика на основе PPO

Агент π_θ параметризован как transformer-based языковая модель, дообученная с **PPO** (Proximal Policy Optimisation):

**PPO objective с clipped surrogate:**
```
L_PPO(θ) = E_t[min(ρ_t * Â_t, clip(ρ_t, 1-ε, 1+ε) * Â_t)]
```

где ρ_t = π_θ(a_t|s_t) / π_θ_old(a_t|s_t) — importance sampling ratio, Â_t — advantage estimate через GAE.

**Полный objective:**
```
L(θ) = L_PPO(θ) - c₁ * L_value(θ) + c₂ * H[π_θ]
```

с entropy regularisation для exploration.

### Рабочая память: история экспериментов

Состояние s_t растёт монотонно, но для tractability используется **скользящее окно K=32** последних экспериментов + сжатое best-ever summary:

```
s_t = (c*, h_t)
```

где c* = argmax_i r_i — лучшая конфигурация на данный момент.

---

## Модуль самооценки (Self-Evaluation)

### Онлайн-прогнозирование кривой

Каждые **∆t = 30s** SE-модуль фитит степенную модель к наблюдаемой траектории лосса:

```
L(t) = a * t^(-b) + c
```

через нелинейный МНК. Экстраполирует предсказанный финальный bpb при T_max и сравнивает с **пессимистическим порогом**:

```
τ_t = bpb* + α * σ_h
```

где bpb* — лучший val-bpb в истории, σ_h — стандартное отклонение исторических финальных bpb, α — tolerance.

### Self-Evaluation как бандит

SE-модуль — это **best-arm identification problem**: на каждом checkpoint t_k агент решает продолжать или остановить. Используется **Sequential Probability Ratio Test (SPRT)** на гауссово-аппроксимированном распределении улучшений для bounding false-positive rate (β = 0.05).

**Throughput gain:**
```
G = 1 / (1 - p_bad * (1 - µ_abort))
```

В экспериментах: p_bad ≈ 0.55, µ_abort ≈ 0.38 → **G ≈ 1.35** (35% больше экспериментов/час), компounding до **2.4×** за ночь.

---

## Теоретические результаты

### Теорема о монотонном улучшении

**Theorem 2 (Monotone Improvement):** Пусть B_t = bpb* после t экспериментов. Если каждый эксперимент — независимая выборка из распределения bpb со строго положительной вероятностью p_min > 0 улучшения B_t, то:

```
E[B_{t+1}] ≤ B_t ∀t, и B_t → B*_min почти наверное при t → ∞
```

**Proof sketch:** B_{t+1} = min(B_t, bpb_{t+1}) ⇒ B_t не возрастает. Ограниченность + монотонность ⇒ a.s. сходимость.

### Sample Complexity Bound

**Proposition 3:** Число экспериментов T для Pr[B_T > B*_min + ε] ≤ δ:

```
T ≥ (1/p_min) * log(1/δ) * log(1/ε)
```

### Exploration vs Exploitation

PPO policy решает trade-off через:
- **Entropy regularisation** c₂ * H[π_θ] — поощряет diverse edits рано, смещается к exploitation с накоплением evidence
- **ε-novelty bonus**: r_novelty = ξ / (1 + d_edit) — бонус за edits, отличающиеся от ранее пробованных

---

## Экспериментальные результаты

### Benchmark: Single-GPU Nanochat

- **Dataset:** FineWeb subset, 10B токенов, BPE vocabulary 4096
- **Evaluation:** 5M token validation set, val-bpb
- **Hardware:** NVIDIA H100 80GB SXM
- **T_max:** 300s per experiment

### Основные результаты

| Метод                    | val-bpb ↓ | Экспериментов |
|--------------------------|-----------|---------------|
| Human Expert (baseline)  | 2.847     | 1             |
| Random Search            | 2.791     | 93            |
| Greedy LLM (no RL)       | 2.734     | 88            |
| **AutoResearch-RL (ours)** | **2.681** | **101**       |

### Что обнаружил агент за 101 эксперимент

1. **Muon optimiser scaling:** LR увеличен с 2×10⁻³ до 2.8×10⁻³, AdamW weight decay снижен с 0.1 до 0.04
2. **QK-norm:** Вставлена per-head ℓ² нормализация на queries/keys — стабилизация attention entropy, +20% batch size
3. **Gradient clipping schedule:** Warm-up schedule — линейное расслабление clip norm с 0.5 до 1.0 за первые 10% обучения
4. **Depth increase:** Число слоёв трансформера увеличено с 12 до 14

### Масштабирование по времени

| Длительность         | Экспериментов | val-bpb ↓ |
|----------------------|---------------|-----------|
| Overnight (~8h)      | 101           | 2.681     |
| Two nights (~16h)    | 205           | 2.661     |
| Weekend (~48h)       | 618           | 2.634     |
| One week (~168h)     | 2147          | 2.608     |

---

## Система AutoResearch-RL

![AutoResearch-RL система overview](../../../media/img_1773560755_aqadbrnrg3suiel8_figure_1_autoresearch_rl_system_overview.jpg)

**Figure 1:** AutoResearch-RL system overview. RL agent proposes code edits, training environment executes them under fixed time budget, self-evaluator monitors progress and can abort early, resulting reward updates both policy and experiment history buffer. Loop runs indefinitely.

---

## Алгоритм работы

```
Algorithm 1: AutoResearch-RL Main Loop
Require: Initial code c₀, policy π_θ, budget T_max, tolerance α
1: c* ← c₀, bpb* ← ∞, h ← []
2: while not Terminate(h) do  ▷ run forever by default
3:   s_t ← (c*, h)
4:   a_t ∼ π_θ(·|s_t)  ▷ propose code edit
5:   c_{t+1} ← Apply(c_t, a_t)
6:   if not Compile(c_{t+1}) then
7:     r_t ← -p_syntax; continue
8:   end if
9:   spawn training process for c_{t+1}, budget T_max
10:  for k = 1, 2, ... every ∆t seconds do
11:    (L̂_k, σ_k) ← ForecastBpb(loss curve)
12:    if L̂_k > τ_t with SPRT confidence then
13:      abort training; r_t ← -p_waste; break
14:    end if
15:  end for
16:  bpb_{t+1} ← Evaluate(c_{t+1})
17:  r_t ← bpb* - bpb_{t+1}
18:  if bpb_{t+1} < bpb* then
19:    c* ← c_{t+1}; bpb* ← bpb_{t+1}
20:  else
21:    c_{t+1} ← c_t  ▷ revert to best known
22:  end if
23:  h ← h ∪ {(c_{t+1}, r_t)}
24:  update π_θ via PPO on (s_t, a_t, r_t, s_{t+1})
25: end while
26: return c*, bpb*
```

---

## Связи с другими темами

### Почему RL, а не in-context learning?

Greedy LLM baseline (GPT-4o без RL fine-tuning) показывает respectable результаты, но RL objective позволяет агенту **internalize research heuristics**:
- Какие классы edits помогают/вредят
- Когда pursue bold vs conservative modifications
- In-context learning требует re-derive heuristics на каждом шаге — compute-intensive + prone to forgetting

### Безопасность и воспроизводимость

Митигации:
1. Изоляция mutable scope до одного файла (train.py)
2. Никакого сетевого доступа
3. Строгий time budget против runaway processes
4. Логирование каждого diff + evaluation result

### Ограничения

- Single GPU, fixed dataset
- Multi-GPU/multi-node требует координации — engineering challenge
- BPE vocabulary + data pipeline зафиксированы

---

## Источники

1. **AutoResearch-RL: Perpetual Self-Evaluating Reinforcement Learning Agents for Autonomous Neural Architecture Discovery** — Nilesh Jain et al., arXiv:2603.07300, 2026. [https://arxiv.org/abs/2603.07300](https://arxiv.org/abs/2603.07300)

## Дополнительные материалы

- **Karpathy's autoresearch prototype** — оригинальный прототип, вдохновивший работу: [https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- **Muon optimizer** — Keller Jordan: [https://github.com/KellerJordan/modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)
- **Query-Key Normalisation** — A. Henry et al., arXiv:2010.04245, 2020
