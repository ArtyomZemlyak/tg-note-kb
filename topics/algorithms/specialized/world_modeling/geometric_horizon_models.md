# Geometric Horizon Models (GHM)

## Общее описание

**Geometric Horizon Models (GHM)** — это класс моделей мира в обучении с подкреплением, которые instantiate "jumpy" world models как генеративные модели successor measure (меры наследования). GHM могут быть обучены off-policy через temporal-difference learning и позволяют предсказывать состояния на геометрически распределённых горизонтах.

GHM были введены в работах Janner et al. (2020) и Thakoor et al. (2022), и значительно развиты в фреймворке Temporal Difference Flows (Farebrother et al., 2025).

## Математическая основа

### Successor Measure

Для политики π и начальной пары состояние-действие (s, a), **successor measure** m^γ_π(·|s,a) определяется как:

```
m^γ_π(X|s,a) = (1-γ) * Σ_{k=0}^{∞} γ^k * Pr(S_k ∈ X | S_0=s, A_0=a, π)
```

для любого подмножества X ⊆ S.

Нормализационный фактор (1-γ) обеспечивает, что m^γ_π является вероятностным распределением.

### Интерпретация через геометрическое время жизни

γ можно интерпретировать как вероятность продолжения эпизода, а (1-γ) — как вероятность остановки. Под этим взглядом, m^γ_π(X|s,a) характеризует вероятность того, что состояние в момент остановки лежит в X.

### Bellman уравнение для Successor Measure

Successor measure является фиксированной точкой Беллман уравнения:

```
m^γ_π(·|s,a) = (1-γ) * P(·|s,a) + γ * E[m^γ_π(·|S',A') | S'=s', A'~π(·|s')]
```

где P(·|s,a) — одношаговая переходная динамика.

## Архитектура GHM

### ODE-based представление

GHM моделирует d-мерное непрерывное пространство состояний как обыкновенное дифференциальное уравнение (ODE), параметризованное зависящим от времени векторным полем v_t: R^d × S × A → R^d.

Сэмплирование из GHM:
1. Сэмплируем начальный шум X_0 ∈ R^d из prior distribution p_0
2. Следуем потоку ψ_t, определяемому Initial Value Problem (IVP):
   ```
   dψ_t/dt = v_t(ψ_t | S, A),  ψ_0 = X_0
   ```
3. Решаем IVP используя численные методы интегрирования (Butcher, 2016)

### ODE-induced probability path

Решение IVP определяет probability path p_t := ψ_t(·|S,A)_♯ p_0(·), т.е. распределение ψ_t(X_0|S,A) где X_0 ~ p_0(·).

Для обеспечения, что p_1 совпадает с successor measure m^γ_π, обучается параметризованное векторное поле v_t(·; θ).

## Обучение GHM

### TD-Flow Loss

Farebrother et al. (2025) предложили обучать векторное поле через минимизацию **td-flow loss**:

```
L_td-flow(θ) = E[(1-γ) * L_flow(θ; X_0, s, a, s') + γ * L_flow(θ; X_1, s', a')]
```

где:
- L_flow — conditional flow-matching loss (Lipman et al., 2023)
- Первый term target'ит одношаговую переходную динамику P(·|s,a)
- Второй term target'ит bootstrapped successor measure m^γ_π(·|s',a')

### Flow Matching

Flow matching конструирует probability paths, которые плавно эволюционируют от source distribution к target distribution. Путём дизайна этих путей для использования структуры в temporal difference target distribution, bootstrapping bias может быть контролирован.

### Проблема bootstrapping bias

Предыдущие подходы страдали от систематической ошибки на длинных горизонтах из-за бутстраппинга предсказаний. TD-Flow решает эту проблему через:
- Conditional flow matching для одношаговых переходов
- Marginal flow matching для bootstrapped successor measure
- Joint optimization с mixture weighting для recovery successor measure при сходимости

## Обобщение на множественные горизонты

### Policy и Horizon conditioning

Для композиционного планирования необходимо предсказывать поведение многих политик на нескольких временных масштабах. Естественное расширение TD-Flow objective condition'ит векторное поле v на:
- Policy encoding z
- Discount factor γ

Это даёт единую модель across policies и горизонтов.

### Вызовы generalization

Generalization across многих горизонтов сложен:
- Variance увеличивается с длиной горизонта
- Per-horizon accuracy уменьшается
- Training дестабилизируется (Petrik & Schaffer, 2008)

### Решение: Horizon Consistency

Для решения этой проблемы предлагается **Temporal Difference Horizon Consistency (TD-HC)** loss, который enforces coherence между горизонтами через Беллман-подобное соотношение:

```
m^γ_π(·|s,a) = (1 - β/γ) * P(·|s,a) + (β/γ) * m^γ_π(·|s',a')
```

где β ≤ γ.

## Применение в композиционном планировании

### Оценка Geometric Switching Policies

GHM позволяют оценивать ценность выполнения произвольных последовательностей политик через разложение successor measure GSP как смеси распределений.

### Monte Carlo estimator

Для GSP ν := π_{z_1} →^{α_1} ... →^{α_{n-1}} π_{z_n}, single-sample monte-carlo estimator:

```
Q̂^γ_ν = Σ_{k=1}^{n} w_k * r(S^+_k)
```

где S^+_k сэмплируются последовательно через композицию GHM предсказаний.

### Random shooting optimization

Планирование сводится к оптимизации через random shooting:
1. Сэмплирование кандидатных последовательностей из proposal distribution
2. Оценка Q-value для каждой кандидатной switching policy
3. Выбор последовательности с наивысшей ценностью

## Преимущества GHM

1. **Off-policy обучение**: Могут быть обучены из offline датасетов без дополнительного взаимодействия со средой.

2. **Непрерывные горизонты**: Моделируют континуум геометрически затухающих временных горизонтов.

3. **Генеративная природа**: Позволяют сэмплировать будущие состояния, а не только предсказывать ожидания.

4. **Flow-based стабильность**: Использование flow-matching уменьшает bootstrapping bias на длинных горизонтах.

5. **Композиционность**: Предсказания могут быть скомпозированы для оценки последовательностей политик.

## Ограничения

1. **Вычислительная сложность**: Решение ODE требует численного интегрирования.

2. **Bias-variance tradeoff**: Длинные горизонты имеют высокую variance предсказаний.

3. **Зависимость от качества данных**: Off-policy обучение требует репрезентативных датасетов.

4. **Continuous state assumption**: Хотя подход расширяется на не-Euclidean и дискретные пространства, базовая формулировка предполагает S ⊆ R^d.

## Связи с другими темами

- [[jumpy_world_models.md]] — Jumpy World Models и композиционное планирование
- [[temporal_difference_flows.md]] — TD-Flow и методы flow-matching
- [[world_models.md]] — Общие концепции World Models
- [[world_models_ha_schmidhuber_2018.md]] — Классическая архитектура World Models
- [[latent_action_models.md]] — Модели латентных действий
- [[geometric_switching_policies.md]] — Geometric Switching Policies
- [[mind_benchmark.md]] — Бенчмарк для оценки контроля действий
- [[vq_vs_continuous_latents.md]] — Дискретные vs непрерывные латентные пространства

## Источники

1. **Janner, M., et al. (2020).** Gamma-Discounted Off-Policy Temporal Difference Learning. *arXiv preprint*.

2. **Thakoor, S., et al. (2022).** Geometric Policy Composition. *arXiv preprint*.

3. **Farebrother, J., et al. (2025).** Temporal Difference Flows. *arXiv preprint*.

4. **Lipman, Y., et al. (2023).** Flow Matching for Generative Modeling. *arXiv preprint*.

5. **Farebrother, J., Pirotta, M., Tirinzoni, A., Bellemare, M.G., Lazaric, A., & Touati, A. (2026).** Compositional Planning with Jumpy World Models. *arXiv preprint arXiv:2602.19634*.

## Дополнительные материалы

- **Оригинальная статья о Compositional Planning**: https://arxiv.org/abs/2602.19634
- **PDF документа**: [[../../../../../media/doc_1772074411_b39e3662_arxiv_2602.19634.pdf|doc_1772074411_b39e3662_arxiv_2602.19634.pdf]]

```metadata
category: reinforcement_learning
subcategory: world_models
tags: geometric_horizon_models, successor_measure, flow_matching, off_policy_learning, temporal_difference
```
