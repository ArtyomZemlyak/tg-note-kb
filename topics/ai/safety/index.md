# Безопасность и выравнивание языковых моделей

## Описание

Этот раздел посвящен темам безопасности, выравнивания и этики в контексте языковых моделей и искусственного интеллекта. Здесь рассматриваются методы обеспечения безопасности, предотвращения вредоносного использования и правильного выравнивания моделей с человеческими ценностями.

## Темы

- [[./token_level_filtering/shaping_capability_with_token_level_filtering.md|Формирование возможностей с использованием фильтрации данных на уровне токенов]] - Исследование методов удаления нежелательных возможностей из языковых моделей путем фильтрации данных на уровне токенов во время предварительного обучения
- [[./token_level_filtering/methodology_for_token_classification.md|Методология для классификации токенов с использованием разреженных автоэнкодеров]] - Описание подхода к созданию классификаторов токенов на основе разреженных автоэнкодеров
- [[./token_level_filtering/token_level_vs_document_level_filtering.md|Сравнение фильтрации на уровне токенов и на уровне документов]] - Подробное сравнение между двумя подходами к фильтрации нежелательных возможностей
- [[./token_level_filtering/scaling_experiments_and_results.md|Масштабирование фильтрации токенов: результаты экспериментов]] - Описание экспериментальных результатов, касающихся масштабирования фильтрации токенов
- [[./token_level_filtering/limitations_and_challenges.md|Ограничения и проблемы фильтрации на уровне токенов]] - Описание основных ограничений и проблем, связанных с методом фильтрации данных на уровне токенов
- [[./token_level_filtering/machine_unlearning_comparison.md|Сравнение с методами машинного "забвения"]] - Сравнение фильтрации на уровне токенов с традиционными методами машинного "забвения"
- [[./machine_unlearning_methods.md|Методы машинного "забвения"]] - Подробное описание различных методов машинного "забвения" и их сравнение с фильтрацией данных
- [[../algorithms/neural_networks/transformers/mechanistic_interpretability/activation_oracles.md|Activation Oracles]] - Activation Oracles: метод интерпретации внутренних активаций для аудита и выявления мисалайнмента моделей

## Связанные темы

- [[../models/llm_alignment.md|Выравнивание языковых моделей]]
- [[./data_quality_impact_assessment.md|Влияние качества данных на безопасность]]
- [[./self_improving_pretraining.md|Self-Improving Pretraining]]
- [[./online_dpo.md|Online Direct Preference Optimization]]
- [[./pretraining_with_human_preferences.md|Pretraining with Human Preferences]]

## Источники

- Rathi, N., & Radford, A. (2026). Shaping capabilities with token-level data filtering. arXiv preprint arXiv:2601.21571.
- Tan, E. X., Dhuliawala, S., Xu, J., Yu, P., Sukhbaatar, S., Weston, J., & Golovneva, O. (2026). Self-Improving Pretraining: using post-trained models to pretrain better models.
- Qi, B., Li, P., Li, F., Gao, J., Zhang, K., & Zhou, B. (2024). Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing.
- Korbak, T., Shi, K., Chen, A., Bhalerao, R., Buckley, C. L., Phang, J., ... & Perez, E. (2023). Pretraining Language Models with Human Preferences.
- Other relevant research on AI safety and alignment

## Метаданные

category: artificial_intelligence
subcategory: model_safety
tags: ai_safety, capability_shaping, token_filtering, data_filtering, model_alignment