# Слияние моделей (Model Merging)

Этот раздел посвящен различным аспектам слияния моделей в контексте обучения и оптимизации языковых моделей.

## Основные темы

### Обзорные материалы
- [[awesome_repository.md]] - **Awesome-Model-Merging-Methods-Theories-Applications**: Коллекция методов, теорий и приложений слияния моделей (Enneng Yang, ACM Computing Surveys 2026)

### Методы и теории
- [[methods.md]] - **Методы слияния моделей**: Классификация и описание методов (Linear Averaging, SLERP, Task Arithmetic, TIES, DARE, Breadcrumbs)
- [[theories.md]] - **Теоретические основы**: Linear Mode Connectivity, перестановочная эквивариантность, теория интерференции параметров

### Применение
- [[applications.md]] - **Приложения слияния моделей**: Оптимизация смешивания данных, объединение экспертизы, регуляризация, непрерывное обучение
- [[model_merging_in_llm_pretraining.md]] - **Слияние моделей в предобучении LLM**: Общие принципы и методы использования слияния моделей в предобучении
- [[demix_framework.md]] - **DeMix**: Фреймворк для масштабирования смешивания данных через слияние моделей

## Связанные разделы

- [[../../foundations/moco_model_collaboration_research.md]] - MOCO: Библиотека для коллаборации моделей (26 алгоритмов)
- [[../../frameworks_and_libraries/mergekit.md]] - MergeKit: Инструментарий для слияния больших языковых моделей
- [[../llm/data_mixing/model_merging_for_data_mixing.md]] - Слияние моделей для оптимизации смешивания данных