# VLANeXt: Рецепты для создания сильных VLA моделей

## Общее описание

**VLANeXt** — это эффективная Vision-Language-Action (VLA) модель, разработанная на основе систематического исследования пространства VLA дизайна. Модель превосходит предыдущие SOTA методы на бенчмарках LIBERO и LIBERO-plus, демонстрируя сильную генерализацию в реальных экспериментах [^1].

Ключевая особенность VLANeXt — модель не полагается на агрессивное масштабирование или специфичную для задач инженерию. Вместо этого, сильные показатели достигаются через принципиальный дизайн на основе 12 ключевых находок, полученных в результате систематического анализа [^1].

## Архитектура VLANeXt

![VLANeXt архитектура](../../../media/doc_1772000469_5313b60e_arxiv_2602.18532.pdf)

*Рисунок 1: Архитектура VLANeXt: многовидовые визуальные входы (third-person + wrist camera), языковые инструкции и проприоцепция токенизируются и обрабатываются мультимодальным LLM (Qwen3-VL-2B), мета-запросы обеспечивают мягкое взаимодействие с policy модулем. Action chunks предсказываются через flow matching и дополнительно регуляризуются частотно-доменным objective.*

Архитектура VLANeXt включает следующие компоненты:

- **Мультимодальные входы**: многовидовые визуальные входы (third-person + wrist camera), языковые инструкции и проприоцепция
- **Мультимодальный LLM**: Qwen3-VL-2B как эффективный выбор backbone
- **Мягкое соединение VLM-Policy**: learnable queries как латентный буфер между модулями
- **Action chunking**: предсказание 8 будущих действий совместно
- **Flow matching objective**: непрерывная оптимизация для генерации действий
- **Frequency-domain loss**: вспомогательная функция потерь в частотной области для улучшения предсказания действий [^1]

## 12 Ключевых Находок (Recipes)

Исследование организовано по трём измерениям:

### 1. Foundational Components (Базовые Компоненты)

#### 1.1 Policy Module Design
- **Находка**: Явный policy head работает лучше, чем повторное использование текстовых токенов
- **Находка**: Увеличенный policy модуль (12 слоёв, 16 токенов) даёт значительное улучшение
- **Решение VLANeXt**: Dedicated policy head с enlarged policy module [^1]

#### 1.2 Action Chunking
- **Находка**: Более длинный chunk horizon (8 шагов) улучшает производительность
- **Обоснование**: Моделирование более длинного временного окна обеспечивает более когерентное view action sequence
- **Решение VLANeXt**: Chunk size = 8 [^1]

#### 1.3 Action Learning Objective
- **Находка**: Regression и diffusion-based objectives работают лучше classification
- **Находка**: Flow matching предлагает сильную производительность и подходит для сложных multimodal distributions
- **Решение VLANeXt**: Flow matching objective [^1]

#### 1.4 VLM Backbone Capacity
- **Находка**: Сильные VLM backbones дают лучший VLA performance
- **Находка**: Qwen3-VL-2B — эффективный выбор (balance performance/efficiency)
- **Решение VLANeXt**: Qwen3-VL-2B backbone [^1]

#### 1.5 VLM-Policy Connection
- **Находка**: Soft connection (с learnable queries) работает лучше loose и tight connections
- **Обоснование**: Learnable query buffer помогает лучше передавать репрезентации от VLM к policy module
- **Решение VLANeXt**: Soft connection с meta queries [^1]

### 2. Perception Essentials (Восприятие)

#### 2.1 Temporal Observation History
- **Находка**: Добавление temporal history не улучшает performance и слегка ухудшает
- **Обоснование**: Redundant temporal inputs вводят noise или отвлекают модель
- **Решение VLANeXt**: Только текущий фрейм [^1]

#### 2.2 Camera View Horizon
- **Находка**: Комбинация third-person + wrist camera значительно улучшает performance
- **Обоснование**: Multi-view observations предоставляют комплементарные геометрические cues
- **Решение VLANeXt**: Multi-view inputs (third-person + wrist) [^1]

#### 2.3 Proprioception Conditioning
- **Находка**: Conditioning proprioception в VLM работает лучше, чем в policy module
- **Обоснование**: Интеграция на уровне VLM позволяет лучшую fusion с visual и language inputs
- **Решение VLANeXt**: Proprioception conditioning в VLM через linear projector [^1]

### 3. Action Modelling Perspectives (Моделирование Действий)

#### 3.1 World Modelling
- **Находка**: World modelling улучшает action generation, но утраивает training time
- **Решение VLANeXt**: Исключено из финального recipe из-за computational cost [^1]

#### 3.2 Time Series Forecasting / Frequency Domain Loss
- **Находка**: Frequency-domain loss улучшает performance с negligible training overhead
- **Метод**: Discrete cosine transform (DCT) для конвертации action sequences в frequency domain, MSE loss между predicted и ground-truth в frequency space
- **Обоснование**: Роботические action sequences структурированы и low-rank, amendable к frequency-domain modeling
- **Решение VLANeXt**: Auxiliary frequency-domain loss (MSE между predicted и ground-truth actions в frequency domain через discrete cosine transform) [^1]

#### 3.3 Proprioception Integration Mechanism
- **Находка**: Transformer-based projector работает слегка лучше linear projector
- **Решение VLANeXt**: Linear projector для простоты (minimal performance difference) [^1]

## Производительность

### LIBERO Benchmark

| Модель | Spatial | Object | Goal | Long | Average |
|--------|---------|--------|------|------|---------|
| OpenVLA-OFT | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |
| **VLANeXt** | **99.0** | **99.2** | **96.6** | **94.6** | **97.4** |

VLANeXt достигает state-of-the-art производительности на LIBERO benchmark [^1].

### LIBERO-plus Benchmark (Generalization)

| Модель | Average Success Rate |
|--------|---------------------|
| OpenVLA | 15.6 |
| WorldVLA | 25.0 |
| NORA | 39.0 |
| UniVLA | 42.9 |
| π0-Fast | 61.6 |
| OpenVLA-OFT | 69.6 |
| **VLANeXt** | **80.1** |

VLANeXt демонстрирует сильную generalization ability с 10% улучшением над SOTA OpenVLA-OFT [^1].

### Real-World Experiments

| Задача | OpenVLA-OFT | π0 | **VLANeXt** |
|--------|-------------|-----|-------------|
| Clean Table (single-arm) | 7/20 | 10/20 | **14/20** |
| Drawer Manipulation (single-arm) | 7/20 | 8/20 | **11/20** |
| Bimanual Clean Table | 5/20 | 10/20 | **11/20** |
| Basket Lifting (bimanual) | 9/20 | 13/20 | **15/20** |

VLANeXt показывает сильную производительность в реальных экспериментах, включая cross-embodiment adaptability для bimanual задач [^1].

## Сравнение с Другими VLA Моделями

### Базовые Подходы
- **RT-2 / OpenVLA**: Базовый pipeline с token reuse для action prediction
- **VLANeXt**: Dedicated policy module, flow matching, frequency-domain loss

### Ключевые Отличия
1. **Policy Module**: VLANeXt использует отдельный policy head вместо reuse text tokens
2. **Action Objective**: Flow matching вместо classification
3. **Perception**: Multi-view + proprioception в VLM
4. **Efficiency**: Frequency-domain loss вместо computationally expensive world modelling

## Обучение и Оценка

### Training Setup
- **Dataset**: LIBERO dataset (10,000 training steps, batch size 256)
- **Learning rate**: 1×10⁻⁴ для моделей < 3B, 5×10⁻⁵ для больших
- **Pretraining**: DROID dataset для real-world экспериментов
- **Action tokens**: Subset of rarely used text tokens repurposed для action prediction
- **Discretization**: Binning strategy (256 bins) для classification baseline, continuous representation для regression/flow matching

### Benchmarks
- **LIBERO**: 4 suites (Spatial, Object, Goal, Long) с 500 expert demonstrations each
- **LIBERO-plus**: 10,030 demonstrations с perturbations (visual, physical, semantic)
- **Evaluation metric**: Success rate (%) на each suite и average

### Ablation Study Design
- Все эксперименты conducted on LIBERO spatial suite как primary testbed
- Findings generalize across другие suites (Object, Goal, Long)
- LIBERO-plus используется для final evaluation robustness/generalization

## Код и Ресурсы

Авторы планируют выпустить unified, easy-to-use codebase для:
- Воспроизведения находок
- Исследования VLA design space
- Создания новых VLA вариантов на общей основе

**Проект**: https://dravenalg.github.io/VLANeXt/

## Связи с Другими Темами

- [[../../applications/agents/vision_language_action_models.md|VLA Модели]] - общий класс Vision-Language-Action моделей
- [[../../algorithms/neural_networks/architectures/flow_matching.md|Flow Matching]] - метод оптимизации для генерации действий, используемый в VLANeXt
- [[../../algorithms/time_series/frequency_domain_analysis.md|Frequency Domain Analysis]] - частотно-доменный анализ для time series, применяемый в frequency-domain loss
- [[../../algorithms/specialized/models_specific/world_models.md|World Models]] - связанные концепции моделирования мира (world modelling исследовался но исключён из финального дизайна)
- [[../../foundations/deep_learning/transformer_architectures.md|Transformer Architectures]] - базовая архитектура для policy module и VLM backbone
- [[../../ai/imitation_learning/behavioral_cloning.md|Behavioral Cloning]] - подход к обучению с демонстраций, используемый в LIBERO benchmark

## Источники

1. **VLANeXt: Recipes for Building Strong VLA Models** - Wu et al., arXiv:2602.18532v1, 2026
   - URL: https://arxiv.org/abs/2602.18532v1
   - Проект: https://dravenalg.github.io/VLANeXt/
   - Авторы: Xiao-Ming Wu (S-Lab, NTU), Bin Fan (Sun Yat-sen University), Kang Liao (S-Lab, NTU), Jian-jian Jiang (Sun Yat-sen University), Runze Yang (Shanghai Jiao Tong University), Yihang Luo (S-Lab, NTU), Zhonghua Wu (SenseTime Research), Wei-Shi Zheng (Sun Yat-sen University), Chen Change Loy (S-Lab, NTU & ACE Robotics)
   - Дата: Февраль 2026
   - Ключевые результаты: SOTA на LIBERO (97.4% avg) и LIBERO-plus (80.1%) бенчмарках

2. **LIBERO Benchmark** - Liu et al., 2023
   - Стандартный бенчмарк для VLA моделей с 4 suites: Spatial, Object, Goal, Long
   - 500 expert demonstrations на каждый suite

3. **LIBERO-plus Benchmark** - Fei et al., 2025b
   - Расширенный бенчмарк для оценки robustness и generalization
   - 10,030 demonstrations с контролируемыми и неконтролируемыми пертурбациями

## Дополнительные Материалы

- **Awesome-VLA Repository**: https://github.com/DravenALG/awesome-vla - коллекция ресурсов по VLA литературе от авторов VLANeXt
- **LIBERO Benchmark**: https://libero-project.github.io - официальный сайт бенчмарка
- **LIBERO-plus**: Расширенный бенчмарк для оценки generalization способности VLA моделей

[^1]: Основная информация из статьи "VLANeXt: Recipes for Building Strong VLA Models", arXiv:2602.18532v1
