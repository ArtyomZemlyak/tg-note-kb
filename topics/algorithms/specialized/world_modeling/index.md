# World Modeling в обучении с подкреплением

## Общее описание

**World Modeling** — это направление в обучении с подкреплением, фокусирующееся на обучении агентов внутренним представлениям (моделям) окружающей среды. Эти модели позволяют агентам предсказывать будущие состояния, планировать действия и принимать решения без непосредственного взаимодействия со средой.

## Основные направления

### Jumpy World Models

Многомасштабные модели мира, которые обучаются предсказывать состояния на нескольких временных масштабах одновременно.

- [[jumpy_world_models.md]] — Jumpy World Models и композиционное планирование
- [[geometric_horizon_models.md]] — Geometric Horizon Models (GHM)
- [[temporal_difference_flows.md]] — TD-Flow для обучения GHM
- [[geometric_switching_policies.md]] — Geometric Switching Policies

### Latent Action Models

Модели, обучающиеся латентным действиям исключительно по видеоданным без меток действий.

- [[latent_action_models.md]] — Latent Action Models (LAMs)
- [[inverse_dynamics_models.md]] — Inverse Dynamics Models для предсказания действий
- [[vq_vs_continuous_latents.md]] — Сравнение дискретных и непрерывных латентных пространств
- [[regularization_techniques_for_latents.md]] — Методы регуляризации латентных пространств
- [[youtube_temporal_dataset.md]] — YouTube-Temporal-1B датасет для обучения

### Оценка World Models

- [[mind_benchmark.md]] — MIND Benchmark для оценки контроля действий и согласованности памяти

## Связанные темы

- [[../models_specific/world_models.md]] — Классические World Models (Ha & Schmidhuber, 2018)
- [[../models_specific/world_models_ha_schmidhuber_2018.md]] — Оригинальная работа Ha & Schmidhuber
- [[../../classical_ml/reinforcement_learning/planning/index.md]] — Планирование в RL
- [[../../classical_ml/reinforcement_learning/planning/compositional_planning.md]] — Композиционное планирование

## Применения

- **Навигация**: Долгосрочная навигация в сложных средах
- **Робототехника**: Манипуляция объектами и управление роботами
- **Автономное вождение**: Планирование маршрутов и принятие решений
- **Игры**: Планирование в играх с длинным горизонтом

## Источники

1. **Ha, D., & Schmidhuber, J. (2018).** World Models. *arXiv preprint arXiv:1803.10122*.

2. **Farebrother, J., et al. (2026).** Compositional Planning with Jumpy World Models. *arXiv preprint arXiv:2602.19634*.

3. **Farebrother, J., et al. (2025).** Temporal Difference Flows. *arXiv preprint*.

```metadata
category: reinforcement_learning
subcategory: world_modeling
tags: world_models, model_based_rl, planning, temporal_abstraction, latent_actions
```
