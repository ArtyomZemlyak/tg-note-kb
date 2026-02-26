# Temporal Difference Flows (TD-Flow)

## Общее описание

**Temporal Difference Flows (TD-Flow)** — это фреймворк для обучения моделей мира (world models) с использованием техник flow matching в контексте обучения с подкреплением. TD-Flow был предложен Farebrother et al. (2025) для решения проблемы систематической ошибки (bias) на длинных горизонтах предсказаний, которая возникает в традиционных temporal-difference подходах из-за бутстраппинга.

Ключевая инновация TD-Flow — конструирование probability paths, которые плавно эволюционируют от исходного распределения к целевому, используя структуру temporal difference target distribution для контроля bootstrapping bias.

## Мотивация

### Проблема bootstrapping bias

В традиционных temporal-difference методах для обучения successor measure, предсказания на длинных горизонтах страдают от накопления ошибок из-за рекурсивной природы бутстраппинга. Каждый шаг вносит ошибку, которая умножается на последующих шагах.

### Flow matching как решение

Flow matching (Lipman et al., 2023; Albergo & Vanden-Eijnden, 2023) предлагает альтернативный подход к генеративному моделированию через конструирование continuous-time probability flows между распределениями. Это позволяет:
- Избежать дискретного бутстраппинга
- Контролировать bias через дизайн probability paths
- Обучать стабильные модели на длинных горизонтах

## Математическая основа

### ODE formulation

TD-Flow моделирует d-мерное пространство состояний через Ordinary Differential Equation (ODE):

```
dψ_t/dt = v_t(ψ_t | S, A),  ψ_0 = X_0
```

где:
- ψ_t: R^d × S × A → R^d — flow во времени t ∈ [0,1]
- v_t — time-dependent vector field, параметризованная нейросетью
- X_0 ~ p_0 — initial noise из prior distribution

### Probability path

Решение OVP определяет probability path:

```
p_t := ψ_t(·|S,A)_♯ p_0(·)
```

т.е. распределение ψ_t(X_0|S,A) где X_0 ~ p_0(·).

Цель: обеспечить p_1 = m^γ_π (successor measure).

### Bellman уравнение для Successor Measure

Successor measure m^γ_π является фиксированной точкой:

```
m^γ_π(·|s,a) = (1-γ) * P(·|s,a) + γ * E[m^γ_π(·|S',A')]
```

Это уравнение определяет mixture distribution с весами (1-γ) и γ.

## TD-Flow Loss

### Основная формула

TD-Flow loss отражает структуру Беллман уравнения:

```
L_td-flow(θ) = E[(1-γ) * L_flow(θ; X_0, s, a, s') + γ * L_flow(θ; X_1, s', a')]
```

где:
- **Первый term** (weight (1-γ)): Conditional flow-matching loss, target'ящий одношаговую переходную динамику P(·|s,a)
- **Второй term** (weight γ): Marginal flow-matching loss, target'ящий bootstrapped successor measure m^γ_π(·|s',a')

### Conditional Flow Matching Loss

Для conditional flow matching:

```
L_flow(θ; X_t, s, a, s') = ||v_t(X_t|s,a; θ) - u_t(X_t|s,a,s')||^2
```

где u_t — conditional vector field, derived из target distribution.

### Joint optimization

Farebrother et al. (2025) показывают, что joint optimization этих компонентов с mixture weighting recover'ит successor measure при сходимости:

```
lim_{θ→θ*} p_1(·|s,a; θ) = m^γ_π(·|s,a)
```

## Обобщение: TD-HC Loss

### Temporal Difference Horizon Consistency

Для обучения на множественных горизонтах одновременно, TD-Flow обобщается через **Temporal Difference Horizon Consistency (TD-HC)** loss:

```
L_td-hc(θ) = L_td-flow(θ) + λ * L_consistency(θ,θ̄)
```

### Consistency Loss

Consistency loss использует Беллман-подобное соотношение между successor measure на двух дисконт-факторах β ≤ γ:

```
m^γ_π(·|s,a) = (1 - β/γ) * P(·|s,a) + (β/γ) * m^γ_π(·|s',a')
```

Это позволяет бутстраппить предсказания длинного горизонта из предсказаний короткого горизонта.

### Практическая реализация

На практике:
- γ сэмплируется равномерно из [γ_min, γ_max]
- β сэмплируется равномерно из [γ_min, γ]
- Consistency term применяется только к небольшой пропорции мини-батча (β < γ)
- Большинство обновлений происходит через TD-Flow (β = γ)

Это мотивировано тем, что consistency term требует сэмплирования из собственных предсказаний модели на горизонте β и использования этих сэмплов как conditioning для более длинного горизонта γ. Ошибки в текущих предсказаниях могут накапливаться и вносить bias.

## Алгоритм обучения

### Входные данные
- Датасет переходов D = {(s, a, s', ...)}
- Диапазон горизонтов [γ_min, γ_max]
- Proportion p_consistency для consistency term

### Шаги обучения

1. **Сэмплирование мини-батча** из D

2. **Для каждого перехода (s, a, s')**:
   - Сэмплировать γ ~ Uniform[γ_min, γ_max]
   - Сэмплировать β ~ Uniform[γ_min, γ]
   - С вероятностью p_consistency: β < γ (consistency)
   - С вероятностью (1 - p_consistency): β = γ (TD-Flow)

3. **Вычисление loss**:
   - Если β = γ: L = L_td-flow(θ)
   - Если β < γ: L = L_td-flow(θ) + λ * L_consistency(θ,θ̄)

4. **Градиентный шаг**: θ ← θ - η * ∇_θ L

5. **Повторять** до сходимости

## Преимущества TD-Flow

1. **Контроль bias**: Flow matching позволяет контролировать bootstrapping bias через дизайн probability paths.

2. **Стабильность на длинных горизонтах**: Значительно уменьшает накопление ошибок по сравнению с традиционными TD методами.

3. **Continuous-time представление**: ODE formulation даёт гладкое представление эволюции распределения во времени.

4. **Гибкость**: Может быть обобщён на множественные горизонты через TD-HC.

5. **Off-policy обучение**: Обучается из offline датасетов без дополнительного взаимодействия.

## Ограничения

1. **Вычислительная сложность**: Решение ODE требует численного интегрирования (например, методы Runge-Kutta).

2. **Чувствительность к гиперпараметрам**: Выбор p_consistency и λ требует настройки.

3. **Bias-variance tradeoff**: Хотя bias контролируется, variance всё ещё может быть высокой на очень длинных горизонтах.

4. **Зависимость от качества данных**: Off-policy обучение требует репрезентативных датасетов.

## Применения

### Geometric Horizon Models

TD-Flow является основным методом обучения для Geometric Horizon Models (GHM), которые используются в:
- Композиционном планировании
- Zero-shot планировании
- Оценке последовательностей политик

### Jumpy World Models

TD-Flow с TD-HC loss является ключевым компонентом Jumpy World Models для:
- Обучения на множественных временных масштабах
- Обеспечения согласованности предсказаний
- Улучшения long-horizon predictive accuracy

### Model-Based RL

TD-Flow может быть применён в:
- Dreamer-like архитектурах
- World Model-based планировании
- Offline RL с моделями мира

## Связи с другими темами

- [[jumpy_world_models.md]] — Jumpy World Models и композиционное планирование
- [[geometric_horizon_models.md]] — Geometric Horizon Models
- [[world_models.md]] — Общие концепции World Models
- [[flow_matching.md]] — Flow matching для генеративного моделирования
- [[latent_action_models.md]] — Модели латентных действий
- [[mind_benchmark.md]] — Бенчмарк для оценки контроля действий
- [[vq_vs_continuous_latents.md]] — Дискретные vs непрерывные латентные пространства

## Источники

1. **Farebrother, J., et al. (2025).** Temporal Difference Flows. *arXiv preprint*.

2. **Lipman, Y., et al. (2023).** Flow Matching for Generative Modeling. *arXiv preprint*.

3. **Albergo, M., & Vanden-Eijnden, E. (2023).** Building Normalizing Flows with Stochastic Interpolants. *arXiv preprint*.

4. **Farebrother, J., Pirotta, M., Tirinzoni, A., Bellemare, M.G., Lazaric, A., & Touati, A. (2026).** Compositional Planning with Jumpy World Models. *arXiv preprint arXiv:2602.19634*.

5. **Petrik, M., & Schaffer, B. (2008).** Bias-Variance Tradeoff in Temporal Difference Learning.

## Дополнительные материалы

- **Оригинальная статья о Compositional Planning**: https://arxiv.org/abs/2602.19634
- **PDF документа**: [[../../../../../media/doc_1772074411_b39e3662_arxiv_2602.19634.pdf|doc_1772074411_b39e3662_arxiv_2602.19634.pdf]]

```metadata
category: reinforcement_learning
subcategory: world_models
tags: temporal_difference_flows, flow_matching, world_models, off_policy_learning, bias_reduction
```
