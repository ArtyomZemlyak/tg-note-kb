# Планирование в обучении с подкреплением

## Общее описание

**Планирование в обучении с подкреплением** — это класс методов, которые используют модель среды (world model) для предсказания будущих состояний и оценки последовательностей действий или политик перед их выполнением в реальной среде.

## Основные подходы

### Model-Predictive Control (MPC)

Планирование на уровне примитивных действий с использованием модели среды для предсказания последствий действий на конечном горизонте.

### Композиционное планирование

Планирование через композицию предобученных политик как временно расширенных действий. Позволяет решать сложные long-horizon задачи через комбинирование навыков.

Подробнее: [[compositional_planning.md]]

### Планирование с World Models

Использование обученных моделей мира для:
- Предсказания будущих состояний
- Оценки ценности последовательностей действий
- Zero-shot планирования для новых задач

## Методы

### Action-Level Planning

Планирование на уровне примитивных действий:
- Model-Predictive Control (MPC)
- Tree search методы
- Trajectory optimization

### Policy-Level Planning

Планирование на уровне политик/навыков:
- Generalized Policy Improvement (GPI)
- Geometric GPI (GGPI)
- Compositional Planning (CompPlan)

### Иерархическое планирование

Планирование с временными абстракциями:
- Options framework
- Hierarchical RL
- Skill chaining

## Связанные темы

- [[../../specialized/world_modeling/jumpy_world_models.md]] — Jumpy World Models для планирования
- [[../../specialized/world_modeling/geometric_horizon_models.md]] — Geometric Horizon Models
- [[../../specialized/world_modeling/geometric_switching_policies.md]] — Geometric Switching Policies
- [[../../specialized/world_modeling/temporal_difference_flows.md]] — TD-Flow
- [[../fundamentals/tabular_rl_methods.md]] — Табличные методы RL
- [[../policy_optimization/ppo_algorithm.md]] — PPO алгоритм

## Источники

1. **Farebrother, J., et al. (2026).** Compositional Planning with Jumpy World Models. *arXiv preprint arXiv:2602.19634*.

2. **Sutton, R.S., & Barto, A.G. (2018).** Reinforcement Learning: An Introduction. *MIT Press*.

3. **Moerland, T.M., et al. (2023).** Model-Based Reinforcement Learning: A Survey. *Foundations and Trends in Machine Learning*.

```metadata
category: reinforcement_learning
subcategory: planning
tags: planning, mpc, model_based_rl, temporal_abstraction, hierarchical_rl
```
