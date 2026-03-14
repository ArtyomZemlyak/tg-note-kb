# Пост-обучение LLM (Post-Training)

Этот раздел посвящен методам и подходам к пост-обучению больших языковых моделей после этапа предобучения (pretraining).

## Основные методы

### Безградиентные методы

- [[neural_thickets_randopt.md]] - **Neural Thickets и RandOpt**: Концепция плотности task-specific экспертов в окрестности весов предобученных моделей и метод случайной оптимизации через ансамблирование

### Reinforcement Learning

- **PPO (Proximal Policy Optimization)**: Классический метод RL с critic model
- **GRPO (Group Relative Policy Optimization)**: Group-relative advantages без critic
- **ES (Evolutionary Strategies)**: Эволюционные стратегии оптимизации

### Parameter-Efficient Methods

- **LoRA (Low-Rank Adaptation)**: Низкоранговые адаптеры для эффективного дообучения
- **Адаптеры**: Вставка дополнительных слоёв между основными

## Связанные разделы

- [[../../model_merging/index.md]] - Слияние моделей: альтернативный подход к комбинированию экспертиз
- [[../training/frontier_model_training_methodologies.md]] - Методологии обучения frontier моделей
- [[../../safety/online_dpo.md]] - Direct Preference Optimization для alignment
- [[../../../algorithms/neural_networks/universal_weight_subspace_hypothesis.md]] - Гипотеза универсального весового подпространства

## Ключевые концепции

1. **Solution Density**: Плотность решений в окрестности весов
2. **Scaling Laws**: Зависимость эффективности методов от размера модели
3. **Ensemble Methods**: Ансамблирование предсказаний нескольких моделей
4. **Weight Space Exploration**: Исследование пространства весов для поиска решений

```metadata
category: ai
subcategory: llm
tags: пост-обучение, дообучение, alignment, rlhf, parameter_efficient, ансамблирование
```
