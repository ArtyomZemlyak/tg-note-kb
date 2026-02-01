# Безопасность и выравнивание языковых моделей

## Описание

Этот раздел посвящен темам безопасности, выравнивания и этики в контексте языковых моделей и искусственного интеллекта. Здесь рассматриваются методы обеспечения безопасности, предотвращения вредоносного использования и правильного выравнивания моделей с человеческими ценностями.

## Темы

- [[./token_level_filtering/shaping_capability_with_token_level_filtering.md|Формирование возможностей с использованием фильтрации данных на уровне токенов]] - Исследование методов удаления нежелательных возможностей из языковых моделей путем фильтрации данных на уровне токенов во время предварительного обучения
- [[./token_level_filtering/methodology_for_token_classification.md|Методология для классификации токенов с использованием разреженных автоэнкодеров]] - Описание подхода к созданию классификаторов токенов на основе разреженных автоэнкодеров
- [[./token_level_filtering/token_level_vs_document_level_filtering.md|Сравнение фильтрации на уровне токенов и на уровне документов]] - Подробное сравнение между двумя подходами к фильтрации нежелательных возможностей
- [[./token_level_filtering/scaling_experiments_and_results.md|Масштабирование фильтрации токенов: результаты экспериментов]] - Описание экспериментальных результатов, касающихся масштабирования фильтрации токенов
- [[../algorithms/neural_networks/transformers/mechanistic_interpretability/activation_oracles.md|Activation Oracles]] - Activation Oracles: метод интерпретации внутренних активаций для аудита и выявления мисалайнмента моделей

## Связанные темы

- [[../models/llm_alignment.md|Выравнивание языковых моделей]]
- [[./data_quality_impact_assessment.md|Влияние качества данных на безопасность]]

## Источники

- Rathi, N., & Radford, A. (2026). Shaping capabilities with token-level data filtering. arXiv preprint arXiv:2601.21571.
- Other relevant research on AI safety and alignment

## Метаданные

category: artificial_intelligence
subcategory: model_safety
tags: ai_safety, capability_shaping, token_filtering, data_filtering, model_alignment