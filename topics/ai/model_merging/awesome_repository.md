# Awesome-Model-Merging-Methods-Theories-Applications

## Общее описание

**Awesome-Model-Merging-Methods-Theories-Applications** — это комплексная коллекция (awesome list) методов, теорий, приложений и возможностей слияния моделей в области машинного обучения, особенно для больших языковых моделей (LLM) и мультимодальных моделей (MLLM).

Репозиторий создан и поддерживается **Enneng Yang** и представляет собой систематизированный каталог исследований в области слияния моделей.

**Статистика репозитория:**
- **Звёзды:** 677+
- **Форки:** 36+
- **arXiv:** 2408.07666
- **ACM Computing Surveys:** 2026

## Основная публикация

Материалы репозитория легли в основу обзорной статьи:

- **Название:** Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities
- **Авторы:** Enneng Yang и коллеги
- **Издание:** ACM Computing Surveys, 2026
- **Тип:** Комплексный обзор (survey paper)
- **DOI:** https://dl.acm.org/doi/10.1145/3787849

## Полная структура коллекции

```
├── SURVEY (Обзорные статьи)
├── BENCHMARK/EVALUATION (Бенчмарки и оценка)
├── ADVANCED METHODS (Продвинутые методы)
│   ├── Pre-Merging Methods (Методы перед слиянием)
│   │   ├── Better Fine-tuning (Улучшенный файн-тюнинг)
│   │   │   ├── Linearization Fine-tuning
│   │   │   ├── Subspace Fine-tuning
│   │   │   └── Sharpness-aware Fine-tuning
│   │   ├── Architecture Transformation
│   │   └── Weight Alignment
│   ├── During Merging Methods (Методы во время слияния)
│   │   ├── Basic Merging Methods
│   │   ├── Weighted-based Merging Methods
│   │   ├── Subspace-based Merging Method
│   │   ├── Routing-based Merging Methods (Dynamic Merging)
│   │   └── Post-calibration based Methods
│   ├── Other Merging Methods
│   └── Theories or Analysis of Model Merging
├── APPLICATION IN FOUNDATION MODELS
│   ├── Large Language Models (LLMs)
│   ├── Multimodal LLMs (MLLMs)
│   ├── Image Generative Models
│   └── Video Generative Models
├── APPLICATION IN ML SUBFIELDS
│   ├── Continual Learning
│   ├── Multi-Task/Multi-Objective/Multi-Domain Learning
│   ├── Out-of-Distribution/Domain Generalization
│   ├── Federated Learning
│   ├── Zero-shot/Few-shot Learning
│   └── Adversarial Learning
└── OTHER APPLICATIONS
```

## Обзорные статьи (Survey Papers)

| Название | Год | Издание |
|----------|-----|---------|
| Scaling Intelligence Through Model Merging: A Comprehensive Survey | 2025 | ArXiv |
| Democratizing AI Through Model Fusion: A Comprehensive Review | 2025 | ArXiv |
| From Task-Specific Models to Unified Systems: A Review | 2025 | ArXiv |
| SoK: On Finding Common Ground in Loss Landscapes | 2024 | ArXiv |
| **Model Merging in LLMs, MLLMs, and Beyond** | 2024 | ArXiv |
| A Survey on Model MoErging | 2024 | ArXiv |
| Merge, Ensemble, and Cooperate! | 2024 | ArXiv |
| Learn From Model Beyond Fine-Tuning: A Survey | 2023 | ArXiv |
| Deep Model Fusion: A Survey | 2023 | ArXiv |

## Продвинутые методы (Advanced Methods)

### 1. Методы перед слиянием (Pre-Merging Methods)

#### Улучшенный файн-тюнинг (Better Fine-tuning)

**Линеаризация (Linearization Fine-tuning):**
- Task Arithmetic in the Tangent Space (NeurIPS 2023)
- Parameter Efficient Multi-task Model Fusion with Partial Linearization (ICLR 2024)
- Tangent Transformers for Composition, Privacy and Removal (ICLR 2024)

**Subspace Fine-tuning:**
- Unraveling LoRA Interference: Orthogonal Subspaces (ArXiv 2025)
- Efficient Model Editing With Task-Localized Sparse Fine-tuning (ICLR 2025)

**Sharpness-aware Fine-tuning:**
- Mitigating Parameter Interference via Sharpness-Aware Fine-Tuning (ICLR 2025)

#### Трансформация архитектуры (Architecture Transformation)
- Knowledge Fusion of Large Language Models (ICLR 2024)
- Training-free Heterogeneous Model Merging (ArXiv 2025)
- GAN Cocktail: mixing GANs without dataset access (ECCV 2022)

#### Выравнивание весов (Weight Alignment / Permutation Symmetry)
- Git Re-Basin: Merging Models modulo Permutation Symmetries (ICLR 2023)
- Equivariant Deep Weight Space Alignment (ICML 2024)
- Transformer fusion with optimal transport (ICLR 2024)
- ZipIt! Merging Models from Different Tasks without Training (ICLR 2024)
- REPAIR: REnormalizing Permuted Activations for Interpolation Repair (ICLR 2023)
- Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs (NeurIPS 2018)

### 2. Методы во время слияния (During Merging Methods)

#### Базовые методы слияния (Basic Merging Methods)
| Статья | Год | Ключевая концепция |
|--------|-----|-------------------|
| Editing models with task arithmetic | 2023 ICLR | Task vectors |
| Composing parameter-efficient modules with arithmetic operation | 2023 NeurIPS | Arithmetic composition |
| Model fusion via optimal transport | 2020 NeurIPS | Optimal transport |
| Weight averaging for neural networks | 1996 AAAI | Weight averaging |

#### Взвешенные методы (Weighted-based Merging Methods)
| Статья | Год | Модели |
|--------|-----|--------|
| Souper-Model: How Simple Arithmetic Unlocks SOTA LLM Performance | 2025 ArXiv | xLAM-2-70b, CoALM-70B |
| Weight Weaving: Parameter Pooling for Data-Free Model Merging | 2025 ArXiv | - |
| Arcee's MergeKit: A Toolkit for Merging LLMs | 2024 ArXiv | Llama2-7B-Chat, Meditron-7B |
| Evolutionary optimization of model merging recipes | 2024 ArXiv | Multiple 7B models |
| Merging models with fisher-weighted averaging | 2022 NeurIPS | - |

#### Subspace-based Merging (Sparse/Low-rank)
| Статья | Год | Инновация |
|--------|-----|-----------|
| Beyond Parameter Arithmetic: Sparse Complementary Fusion | 2026 ArXiv | Distribution-aware |
| Orthogonal Model Merging | 2026 ArXiv | Orthogonal subspaces |
| Language Models are Super Mario | 2024 ICML | Absorbing abilities |
| Model breadcrumbs: Scaling multi-task merging with sparse masks | 2023 ArXiv | Sparse masks |
| DELLA-Merging: Magnitude-Based Sampling | 2024 ArXiv | Reduce interference |
| EMR-Merging: Tuning-Free High-Performance | 2024 NeurIPS | Tuning-free |

#### Routing-based Merging (Dynamic)
| Статья | Год | Подход |
|--------|-----|--------|
| Fine-Grained Model Merging via Modular Expert Recombination | 2026 ArXiv | Expert recombination |
| MASS: MoErging through Adaptive Subspace Selection | 2025 ArXiv | Adaptive subspace |
| Twin-Merging: Dynamic Integration of Modular Expertise | 2024 NeurIPS | Dynamic integration |
| Merge, Then Compress: Demystify Efficient SMoE | 2024 ICLR | MoE compression |
| Sparse Upcycling: Training MoE from Dense Checkpoints | 2023 ICLR | Dense-to-MoE |

#### Post-calibration based Methods
| Статья | Год | Техника |
|--------|-----|---------|
| MAGIC: Superior Model Merging via Magnitude Calibration | 2025 ArXiv | Magnitude calibration |
| Representation Surgery for Multi-Task Model Merging | 2024 ICML | Deep representation surgery |
| SurgeryV2: Bridging Model Merging and Multi-Task Learning | 2024 ArXiv | Representation surgery |

### 3. Теории и анализ (Theories & Analysis)

| Статья | Год | Ключевой вклад |
|--------|-----|----------------|
| Demystifying Mergeability: Interpretable Properties to Predict Success | 2026 ArXiv | Predicting mergeability |
| Understanding Model Merging: A Unified Generalization Framework | 2026 ArXiv | Generalization framework |
| Why Do More Experts Fail? Theoretical Analysis | 2025 ArXiv | Failure analysis |
| When is Task Vector Provably Effective? | 2025 ICLR | Task vector theory |
| Linear Mode Connectivity and the Lottery Ticket Hypothesis | 2020 ICML | Mode connectivity |
| Model soups: averaging weights improves accuracy | 2022 ICML | Model soups theory |

## Приложения в Foundation Models

### Большие языковые модели (LLMs)

| Область применения | Ключевые статьи |
|-------------------|-----------------|
| **Выравнивание по предпочтениям человека** | • Navigating the Alignment-Calibration Trade-off (2025)<br>• SafeMERGE: Preserving Safety Alignment (2025)<br>• Rewarded soups: pareto-optimal alignment (NeurIPS 2023) |
| **Детоксикация** | • Surgical, Cheap, and Flexible: Mitigating False Refusal (ICLR 2025)<br>• Bias Vector: Mitigating Biases with Task Arithmetic (2024) |
| **Редактирование знаний / Unlearning** | • Exact Unlearning of Finetuning Data via Model Merging (2025)<br>• NegMerge: Consensual Weight Negation for Unlearning (2024) |
| **Ускорение обучения** | • Checkpoint Merging via Bayesian Optimization (2024)<br>• Early Weight Averaging meets High Learning Rates (NeurIPS 2023) |
| **Ускорение рассуждений** | • Unlocking Efficient Long-to-Short LLM Reasoning (2025)<br>• Reasoning Pattern Alignment Merging (2026) |
| **Эффективность MoE** | • MergeMoE: Efficient Compression of MoE Models (2025)<br>• Merging Experts into One (EMNLP 2023) |
| **Слияние LLM-агентов** | • ARM: Role-Conditioned Neuron Transplantation (2026)<br>• AgentMerge: Enhancing Generalization (NeurIPS 2024) |
| **Комбинирование экспертных способностей** | • Souper-Model: Simple Arithmetic Unlocks SOTA (2025)<br>• FuseChat-3.0: Preference Optimization + Heterogeneous Fusion (2025) |

### Мультимодальные LLM (MLLMs)

| Приложение | Ключевые статьи |
|------------|----------------|
| **Мультимодальная фузия** | • Jointly training large autoregressive multimodal models (ICLR 2024)<br>• π-Tuning: Optimal Multi-task Interpolation (ICML 2023) |
| **Кросс-модальный перенос** | • Multimodal Attention Merging (ICASSP 2024) |
| **Экспертные MLLM** | • FRISM: Fine-Grained Reasoning Injection (2026)<br>• RobustMerge: Parameter-Efficient Merging for MLLMs (NeurIPS 2025)<br>• UQ-Merge: Uncertainty Guided Merging (ACL 2025) |

### Модели генерации изображений

| Приложение | Ключевые статьи |
|------------|----------------|
| **Смешивание стилей** | • ZipLoRA: Any Subject in Any Style (2023)<br>• Mix-of-Show: Decentralized LoRA Adaptation (NeurIPS 2023)<br>• MoLE: Mixture of LoRA Experts (ICLR 2024) |
| **Снижение стоимости обучения** | • Linear Combination of Saved Checkpoints (2024)<br>• LCM-LORA: Accelerating STABLE-DIFFUSION (2024) |
| **Улучшение качества** | • SELMA: Learning and Merging Skill-Specific Experts (2024)<br>• Decouple-Then-Merge: Better Training for Diffusion (2024) |
| **Детекция дипфейков** | • Real-Aware Residual Model Merging (2025) |

## Приложения в ML Subfields

### Непрерывное обучение (Continual Learning)
| Фокус | Ключевые статьи |
|-------|----------------|
| **Смягчение катастрофического забывания** | • Merge before Forget: Single LoRA Continual Learning (2025)<br>• RECALL: Catastrophic-forgetting ALLeviation (2025)<br>• MagMax: Leveraging Model Merging for Continual Learning (ECCV 2024)<br>• Lm-cocktail: Resilient tuning via model merging (ACL 2024) |

### Многозадачное/Многоцелевое обучение
| Фокус | Ключевые статьи |
|-------|----------------|
| **Multi-Task** | • G-Merging: Graph Models Merging (ICLR 2026)<br>• Representation Surgery for Multi-Task Model Merging (ICML 2024)<br>• AdaMerging: Adaptive Model Merging (ICLR 2024) |
| **Multi-Objective** | • Pareto Merging: Multi-Objective Optimization (ICML 2025)<br>• Bone Soups: Controllable Multi-Objective Generation (2025) |

### OOD-обобщение (Out-of-Distribution)
| Ключевые статьи |
|----------------|
| • Model soups need only one ingredient (2026) |
| • Model soups: averaging weights improves accuracy (ICML 2022) |
| • Diverse weight averaging for OOD generalization (NeurIPS 2022) |
| • Model ratatouille: Recycling diverse models (ICML 2023) |

### Федеративное обучение (Federated Learning)
| Ключевые статьи |
|----------------|
| • Communication-Efficient Personalized Adaptation via Federated-Local Merging (2026) |
| • FedMerge: Federated Personalization via Model Merging (2025) |
| • Federated Learning with Matched Averaging (ICLR 2020) |
| • Model fusion via optimal transport (NeurIPS 2020) |

### Zero-shot/Few-shot обучение
| Фокус | Ключевые статьи |
|-------|----------------|
| **Zero-Shot** | • Model Merging Improves Zero-Shot Generalization (NeurIPS 2025)<br>• Learning to Route Among Specialized Experts (ICML 2024) |
| **Few-Shot** | • LoraHub: Efficient Cross-Task Generalization (COLM 2024)<br>• LoraRetriever: Input-Aware LoRA Retrieval (ACL 2024) |

### Состязательное обучение (Adversarial Learning)
| Тип | Ключевые статьи |
|-----|----------------|
| **Как атака** | • Merge Hijacking: Backdoor Attacks to Model Merging (2025)<br>• LoBAM: LoRA-Based Backdoor Attack (2024)<br>• BadMerging: Backdoor Attacks (CCS 2024) |
| **Как защита** | • Do Not Merge My Model! Safeguarding Open-Source LLMs (AAAI 2026)<br>• Model Unmerging: Making Models Unmergeable (2025)<br>• MergePrint: Robust Fingerprinting (2024) |

## Бенчмарки и оценка

| Бенчмарк | Год | Оцененные модели |
|----------|-----|-----------------|
| FusionBench: Comprehensive Benchmark | 2025 JMLR | Mistral-7B, MetaMath-Mistral-7B |
| MergeBench: Domain-Specialized LLMs | 2025 ArXiv | Llama-3.2-3B, Llama3.1-8B, Gemma-2 |
| Model-GLUE: Democratized LLM Scaling | 2024 NeurIPS | 15+ LLMs (7B range) |
| What Matters for Model Merging at Scale? | 2024 ArXiv | PaLM-2 (1B-64B) |
| A Systematic Study of Model Merging | 2025 ArXiv | Llama-3.2-3B, Qwen3-4B/8B |

## Ключевые концепции и термины

| Концепция | Описание |
|-----------|----------|
| **Task Arithmetic** | Редактирование моделей через векторную арифметику в пространстве параметров |
| **Model Soups** | Усреднение весов нескольких fine-tuned моделей |
| **Linear Mode Connectivity** | Свойство, при котором модели могут быть соединены линейными путями |
| **Permutation Symmetry** | Учет инвариантности перестановки нейронов при слиянии |
| **LoRA Merging** | Слияние Low-Rank Adaptation адаптеров |
| **Fisher-weighted Averaging** | Использование информации Фишера для взвешенного слияния |
| **Sparse Merging** | Использование разреженности для снижения интерференции |
| **Dynamic/Routing Merging** | Стратегии слияния, зависящие от входа |

## Масштабирование и популярные модели

**Отмеченные статьи:** Репозиторий отмечает статьи, экспериментирующие с моделями ≥7B или малыми mainstream LLM для практической参考价值.

**Популярные семейства моделей:**
- LLaMA/Llama-2/Llama-3 series (7B, 13B, 70B, 8B, 72B)
- Mistral-7B series
- Qwen/Qwen2/Qwen2.5 series (0.5B-72B)
- Gemma/Gemma-2 series (2B, 7B, 9B, 27B)
- Vicuna, WizardLM, CodeLlama, и другие

Этот репозиторий служит **центральным каталогом** для всех методов слияния моделей и связан с:

- [[model_merging_in_llm_pretraining.md]] - Общие принципы слияния моделей в предобучении LLM
- [[demix_framework.md]] - Фреймворк DeMix для оптимизации смешивания данных
- [[methods.md]] - Детальное описание методов слияния
- [[theories.md]] - Теоретические основы слияния моделей
- [[applications.md]] - Приложения слияния моделей
- [[../../foundations/moco_model_collaboration_research.md]] - Библиотека MOCO для коллаборации моделей
- [[../../frameworks_and_libraries/mergekit.md]] - Инструментарий mergekit для слияния LLM

## Ресурсы

- **GitHub репозиторий:** https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications
- **ACM Publication:** https://dl.acm.org/doi/10.1145/3787849

## Источники

- [Awesome-Model-Merging-Methods-Theories-Applications GitHub Repository](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) - Основной репозиторий с коллекцией методов слияния моделей
- Yang, E., et al. (2026). Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities. ACM Computing Surveys. https://dl.acm.org/doi/10.1145/3787849 - Обзорная статья по слиянию моделей
