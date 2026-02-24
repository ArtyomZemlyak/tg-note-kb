# Методы слияния моделей (Model Merging Methods)

## Общее описание

Методы слияния моделей (model merging) представляют собой техники **безградиентного объединения** параметров нескольких предобученных моделей с одинаковой архитектурой в единую модель, сохраняющую преимущества исходных моделей.

## Классификация методов

### 0. Методы перед слиянием (Pre-Merging Methods)

#### Улучшенный файн-тюнинг (Better Fine-tuning)

**Линеаризация (Linearization Fine-tuning):**
- **Описание:** Файн-тюнинг в касательном пространстве параметров
- **Методы:**
  - Task Arithmetic in the Tangent Space (NeurIPS 2023)
  - Parameter Efficient Multi-task Model Fusion with Partial Linearization (ICLR 2024)
- **Преимущества:** Уменьшает интерференцию при последующем слиянии

**Subspace Fine-tuning:**
- **Описание:** Файн-тюнинг в ортогональных подпространствах
- **Методы:**
  - Unraveling LoRA Interference: Orthogonal Subspaces (ArXiv 2025)
  - Efficient Model Editing With Task-Localized Sparse Fine-tuning (ICLR 2025)
- **Преимущества:** Снижает интерференцию между задачами

**Sharpness-aware Fine-tuning:**
- **Описание:** Файн-тюнинг с учетом остроты минимума
- **Методы:** Mitigating Parameter Interference via Sharpness-Aware Fine-Tuning (ICLR 2025)
- **Преимущества:** Улучшает обобщающую способность слитой модели

#### Выравнивание весов (Weight Alignment / Permutation Symmetry)
- **Описание:** Учет инвариантности перестановки нейронов перед слиянием
- **Методы:**
  - Git Re-Basin: Merging Models modulo Permutation Symmetries (ICLR 2023)
  - Equivariant Deep Weight Space Alignment (ICML 2024)
  - Transformer fusion with optimal transport (ICLR 2024)
  - ZipIt! Merging Models from Different Tasks without Training (ICLR 2024)
  - REPAIR: REnormalizing Permuted Activations for Interpolation Repair (ICLR 2023)
- **Применение:** Слияние моделей с разной инициализацией

### 1. Методы на основе линейной связности (Linear Mode Connectivity)

#### Линейное усреднение (Linear Averaging / Model Soups)
- **Описание:** Простое взвешенное арифметическое усреднение параметров моделей
- **Формула:** `θ_merged = α₁θ₁ + α₂θ₂ + ... + αₙθₙ`
- **Преимущества:** 
  - Не требует гиперпараметров
  - Высокая эффективность на практике
  - Вычислительная простота
- **Ограничения:** Требует идентичных архитектур и инициализаций
- **Источник:** Wortsman et al., 2022 (Model Soups)

#### SLERP (Spherical Linear Interpolation)
- **Описание:** Сферическая линейная интерполяция, сохраняющая нормы параметров
- **Применение:** Многоуровневое слияние (Multi-SLERP) для нескольких моделей
- **Преимущества:** Сохраняет геометрические свойства пространства параметров

### 2. Методы во время слияния (During Merging Methods)

#### Взвешенные методы (Weighted-based Merging Methods)

**Souper-Model:**
- **Описание:** Простая арифметика весов для достижения SOTA производительности
- **Источник:** Souper-Model: How Simple Arithmetic Unlocks SOTA LLM Performance (2025)
- **Модели:** xLAM-2-70b, CoALM-70B

**Weight Weaving:**
- **Описание:** Объединение параметров через пул параметров
- **Особенность:** Работает без доступа к данным
- **Источник:** Weight Weaving: Parameter Pooling for Data-Free Model Merging (2025)

**Fisher-weighted Averaging:**
- **Описание:** Использование информации Фишера для взвешивания параметров
- **Источник:** Merging models with fisher-weighted averaging (NeurIPS 2022)
- **Преимущества:** Учитывает важность параметров для каждой задачи

#### Subspace-based Merging (Sparse/Low-rank)

**Orthogonal Model Merging:**
- **Описание:** Слияние в ортогональных подпространствах
- **Источник:** Orthogonal Model Merging (2026)
- **Преимущества:** Минимальная интерференция

**Language Models are Super Mario:**
- **Описание:** Поглощение способностей через разреженные маски
- **Источник:** Language Models are Super Mario (ICML 2024)

**DELLA-Merging:**
- **Описание:** Magnitude-Based Sampling для снижения интерференции
- **Источник:** DELLA-Merging: Magnitude-Based Sampling (2024)

**EMR-Merging:**
- **Описание:** Tuning-Free высокопроизводительное слияние
- **Источник:** EMR-Merging: Tuning-Free High-Performance (NeurIPS 2024)

#### Routing-based Merging (Dynamic)

**Fine-Grained Model Merging via Modular Expert Recombination:**
- **Описание:** Рекомбинация экспертных модулей
- **Источник:** Fine-Grained Model Merging via Modular Expert Recombination (2026)

**MASS: MoErging through Adaptive Subspace Selection:**
- **Описание:** Адаптивный выбор подпространства для слияния
- **Источник:** MASS: MoErging through Adaptive Subspace Selection (2025)

**Twin-Merging:**
- **Описание:** Динамическая интеграция модульной экспертизы
- **Источник:** Twin-Merging: Dynamic Integration of Modular Expertise (NeurIPS 2024)

**Merge, Then Compress:**
- **Описание:** Сжатие MoE моделей после слияния
- **Источник:** Merge, Then Compress: Demystify Efficient SMoE (ICLR 2024)

#### Post-calibration based Methods

**MAGIC:**
- **Описание:** Magnitude Calibration для улучшенного слияния
- **Источник:** MAGIC: Superior Model Merging via Magnitude Calibration (2025)

**Representation Surgery:**
- **Описание:** Глубокая хирургия представлений для multi-task слияния
- **Источники:**
  - Representation Surgery for Multi-Task Model Merging (ICML 2024)
  - SurgeryV2: Bridging Model Merging and Multi-Task Learning (2024)

### 3. Методы на основе редактирования параметров

#### Task Arithmetic
- **Описание:** Операции с векторами задач в пространстве параметров
- **Механизм:** Вычисление "векторов задач" как разницы между fine-tuned и базовой моделью
- **Формула:** `θ_merged = θ_base + λ₁(θ₁ - θ_base) + λ₂(θ₂ - θ_base) + ...`
- **Применение:** Комбинирование различных способностей моделей
- **Источник:** Ilharco et al., 2022/2023

#### TIES (Task Incremental Ensemble Selection)
- **Описание:** Решает проблему интерференции при слиянии моделей
- **Механизм:** 
  - Маскирование незначимых параметров
  - Масштабирование важных параметров
  - Разрешение конфликтов знаков
- **Требования:** Настройка гиперпараметров
- **Источник:** Yadav et al., 2023

#### DARE (Dataset Adaptive Representation Editing)
- **Описание:** Оставляет только наиболее значимые изменения параметров
- **Механизм:** 
  - Идентификация важных параметров через статистический анализ
  - Прореживание менее значимых изменений
  - Масштабирование оставшихся параметров
- **Преимущества:** 
  - Работает без дополнительного обучения или данных
  - Позволяет контролировать степень слияния
- **Требования:** Настройка гиперпараметров
- **Источник:** Yu et al., 2023

### 3. Методы на основе перестановок (Permutation-based)

#### Linear Mode Connectivity с перестановками
- **Описание:** Применение перестановок к нейронам для выравнивания моделей перед слиянием
- **Механизм:** 
  - Поиск оптимальных перестановок нейронов
  - Выравнивание моделей в пространстве потерь
  - Последующее линейное слияние
- **Источники:** 
  - Ainsworth et al., 2022
  - Entezari et al., 2021
  - Stoica et al., 2023

### 4. Разреженные методы (Sparse Methods)

#### Breadcrumbs
- **Описание:** Использование разреженных масок для масштабирования слияния
- **Механизм:** 
  - Создание разреженных масок для каждого компонента
  - Комбинирование через неперекрывающиеся маски
- **Преимущества:** 
  - Гиперпараметр-свободный метод
  - Позволяет масштабировать слияние многих задач
- **Применение:** Слияние нескольких специализированных моделей

### 5. Адаптивные методы

#### AdaMerge
- **Описание:** Адаптивное слияние с автоматическим выбором весов
- **Механизм:** Использование небольшого набора данных для калибровки весов слияния

#### RegMix
- **Описание:** Регуляризованное слияние для оптимизации смешивания данных
- **Применение:** Оптимизация состава тренировочных данных

## Сравнение методов

| Метод | Гиперпараметры | Требует данных | Масштабируемость | Основное применение |
|-------|---------------|----------------|------------------|---------------------|
| **Pre-Merging** |||||
| Linearization Fine-tuning | Да | Нет | Средняя | Уменьшение интерференции |
| Subspace Fine-tuning | Да | Нет | Средняя | Ортогональные задачи |
| Sharpness-aware FT | Да | Нет | Средняя | Улучшение обобщения |
| Weight Alignment | Нет | Нет | Низкая | Выравнивание моделей |
| **During Merging** |||||
| Linear Averaging | Нет | Нет | Высокая | Базовое слияние |
| SLERP | Нет | Нет | Средняя | Сохранение норм |
| Fisher-weighted | Нет | Нет | Средняя | С учетом важности |
| Souper-Model | Нет | Нет | Высокая | SOTA производительность |
| Weight Weaving | Нет | Нет | Высокая | Без данных |
| Orthogonal Merging | Нет | Нет | Высокая | Минимальная интерференция |
| EMR-Merging | Нет | Нет | Высокая | Tuning-free |
| **Editing/Adaptive** |||||
| Task Arithmetic | Да (λ) | Нет | Высокая | Комбинирование задач |
| TIES | Да | Нет | Средняя | Решение интерференции |
| DARE | Да | Нет | Высокая | Селективное слияние |
| MAGIC | Да | Нет | Средняя | Magnitude calibration |
| **Routing/Dynamic** |||||
| MASS | Да | Нет | Средняя | Adaptive subspace |
| Twin-Merging | Да | Нет | Средняя | Dynamic integration |
| **Sparse** |||||
| Breadcrumbs | Нет | Нет | Очень высокая | Многосоставное слияние |
| **Permutation** |||||
| Git Re-Basin | Нет | Нет | Низкая | Выравнивание моделей |
| **Adaptive** |||||
| AdaMerge | Да | Да | Средняя | Автоматические веса |
| RegMix | Да | Да | Средняя | Оптимизация данных |

## Критерии выбора метода

1. **Идентичность архитектур:** Если модели имеют одинаковую архитектуру и инициализацию — подходят все методы
2. **Наличие данных:** Если есть доступ к данным — можно использовать адаптивные методы
3. **Количество моделей:** Для слияния многих моделей предпочтительны разреженные методы
4. **Интерференция:** При конфликтах между задачами — TIES или DARE
5. **Вычислительные ресурсы:** При ограничениях — линейное усреднение

## Связанные темы

[[model_merging_in_llm_pretraining.md]] - Применение слияния моделей в предобучении LLM
[[awesome_repository.md]] - Коллекция методов слияния моделей
[[demix_framework.md]] - Фреймворк DeMix для оптимизации смешивания данных
[[../../foundations/moco_model_collaboration_research.md]] - Библиотека MOCO для коллаборации моделей
[[../../frameworks_and_libraries/mergekit.md]] - Инструментарий mergekit для слияния LLM

## Источники

- Yang, E., et al. (2026). Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities. ACM Computing Surveys. https://dl.acm.org/doi/10.1145/3787849 - Основной обзор методов слияния моделей
- Wortsman, M., et al. (2022). Model soups: averaging weights of multiple fine-tuned models improves accuracy. https://arxiv.org/abs/2203.05482 - Классическая работа о линейном усреднении
- Ilharco, G., et al. (2023). Editing models with task arithmetic. https://arxiv.org/abs/2212.04089 - Task Arithmetic для редактирования моделей
- Yadav, P., et al. (2023). TIES-Merging: Resolving Interference When Merging Models. https://arxiv.org/abs/2306.01708 - Метод TIES
- Yu, L., et al. (2023). DARE: Dataset Adaptive Representation Editing. https://arxiv.org/abs/2311.03099 - Метод DARE
- Ainsworth, S., et al. (2022). Git Re-Basin: Merging Models without Retaining. https://arxiv.org/abs/2209.08721 - Перестановки для слияния
- Entezari, R., et al. (2021). The Role of Permutation Invariance in Linear Mode Connectivity. https://arxiv.org/abs/2111.09852 - Теоретические основы LMC
- Goddard, C., et al. (2024). Arcee's mergekit: A toolkit for merging large language models. https://arxiv.org/abs/2403.13257 - Инструментарий для слияния
- Souper-Model: How Simple Arithmetic Unlocks SOTA LLM Performance. https://arxiv.org/abs/2501.06326 - Простая арифметика для SOTA
- Weight Weaving: Parameter Pooling for Data-Free Model Merging. https://arxiv.org/abs/2502.10517 - Parameter Pooling
- Orthogonal Model Merging. https://arxiv.org/abs/2601.05230 - Ортогональное слияние
- EMR-Merging: Tuning-Free High-Performance. https://arxiv.org/abs/2410.11042 - Tuning-free слияние
- MAGIC: Superior Model Merging via Magnitude Calibration. https://arxiv.org/abs/2508.01332 - Magnitude Calibration
- Representation Surgery for Multi-Task Model Merging. https://arxiv.org/abs/2404.05405 - Deep representation surgery
- MASS: MoErging through Adaptive Subspace Selection. https://arxiv.org/abs/2505.14146 - Adaptive subspace selection
- Twin-Merging: Dynamic Integration of Modular Expertise. https://arxiv.org/abs/2407.20311 - Dynamic integration
