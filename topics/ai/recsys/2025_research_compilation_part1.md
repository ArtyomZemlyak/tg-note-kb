# Подборка статей 2025 по рекомендательным системам (часть 1)

## Описание

Этот документ представляет собой подборку статей и исследований по рекомендательным системам, представленных в 2025 году. Подборка охватывает три основные области: End2End генеративные системы, LLM-базированные рекомендации и масштабирование генеративных подходов.

## Структура документа

Документ разделен на три основные категории, отражающие ключевые направления исследований в области рекомендательных систем:

1. **End2End генеративные рекомендательные системы** - исследования, посвященные унификации и генеративным подходам
2. **LLM-базированные рекомендательные системы** - применение больших языковых моделей в рекомендациях
3. **Масштабирование генеративных подходов** - методы для работы с длинными последовательностями и увеличением модели

## 1. End2End генеративные рекомендательные системы

### OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment

Одна из ключевых работ, продолжение технического отчета OneRec от Kuaishou, описывающая подход к унификации поиска и ранжирования через генеративные рекомендательные системы. Система использует итеративное выравнивание предпочтений для улучшения качества рекомендаций.

См. также: [[end_to_end_generative_recommendation_systems.md]], [[onerec_think/main.md]]

### OneRec Technical Report

Технический отчет, описывающий основы архитектуры OneRec - одной из первых промышленных end-to-end генеративных рекомендательных систем. В работе описываются подходы к токенизации айтемов, претрейну и файнтюну модели.

См. также: [[end_to_end_generative_recommendation_systems.md]], [[onerec_think/main.md]]

### OneRec-V2 Technical Report

Расширенная версия OneRec, включающая улучшения архитектуры, масштабирование и новые подходы к интеграции семантических идентификаторов (SIDs) и логического вывода (reasoning).

См. также: [[end_to_end_generative_recommendation_systems.md]], [[onerec_think/main.md]]

### OneLoc: Geo-Aware Generative Recommender Systems for Local Life Service

Новая архитектура генеративных рекомендательных систем, специализирующихся на локальных сервисах. В работе представлены подходы к интеграции географического контекста в генеративные рекомендательные модели.

См. также: [[generative_retrieval_models.md]]

### OneSug: The Unified End-to-End Generative Framework for E-commerce Query Suggestion

Единый фреймворк для генерации поисковых запросов в e-commerce системах. Подход объединяет понимание пользовательских намерений и генерацию релевантных предложений.

См. также: [[generative_retrieval_models.md]]

### OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search

Предварительное исследование применения end-to-end генеративных подходов к e-commerce поиску. Работа задает основы для дальнейшего развития унифицированных поисковых систем.

См. также: [[generative_retrieval_models.md]]

### UniSearch: Rethinking Search System with a Unified Generative Architecture

Архитектура, пересматривающая традиционные подходы к поисковым системам через призму генеративных моделей. Работа предлагает унифицированный подход к поиску и рекомендациям.

См. также: [[generative_retrieval_models.md]], [[transformer_based_models.md]]

### EGA-V1: Unifying Online Advertising with End-to-End Learning

Первая версия EGA (End-to-end Generative Advertising) от Meituan, описывающая подход к унификации онлайн рекламы через end-to-end обучение. Система заменяет традиционные каскады на одну генеративную модель.

См. также: [[end_to_end_generative_recommendation_systems.md]], [[unirom_end_to_end_advertising_system.md]]

### EGA-V2: An End-to-end Generative Framework for Industrial Advertising

Расширенная версия EGA, включающая улучшения для промышленного внедрения, оптимизации инференса и масштабирования. Вторая версия включает улучшенные подходы к аукциону и персонализации рекламы.

См. также: [[end_to_end_generative_recommendation_systems.md]], [[unirom_end_to_end_advertising_system.md]]

### GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation

Работа, описывающая подход к предобучению единой модели для масштабных рекламных рекомендаций. GPR (Generative Pre-trained Recommendation) использует генеративные методы для унификации различных рекламных сценариев.

См. также: [[generative_retrieval_models.md]], [[plum/main.md]]

## 2. LLM-базированные рекомендательные системы

### PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations

Фундаментальная работа Google/YouTube по адаптации предобученных языковых моделей для промышленных генеративных рекомендаций. В работе представлены подходы к токенизации айтемов, претрейну и файнтюну моделей на задачах рекомендаций.

См. также: [[plum/main.md]], [[semantic_ids_in_recsys.md]]

### OneRec-Think: In-Text Reasoning for Generative Recommendation

Расширение OneRec, добавляющее возможности логического вывода (reasoning) в генеративные рекомендательные системы. Подход позволяет модели генерировать обоснования для рекомендаций, улучшая интерпретируемость.

См. также: [[onerec_think/main.md]], [[end_to_end_generative_recommendation_systems.md]]

### Align3GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation

Новый фреймворк для выравнивания на нескольких уровнях (пользователь, айтем, сессия) в LLM-базированных генеративных рекомендациях. Работа предлагает методы для согласования представлений на различных уровнях абстракции.

См. также: [[llm_based/main.md]]

### GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks

Применение генеративных потоковых сетей (Generative Flow Networks) для дообучения генеративных рекомендательных фреймворков. Подход позволяет лучше моделировать распределения предпочтений пользователей.

См. также: [[generative_retrieval_models.md]]

## 3. Масштабирование генеративных подходов

### LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders

Новый подход к масштабированию моделирования длинных последовательностей в промышленных рекомендательных системах. LONGER предлагает архитектурные и алгоритмические улучшения для обработки очень длинных пользовательских историй.

См. также: [[transformer_based_models.md]], [[long_context_handling_methods.md]]

### Scaling Generative Recommendations with Context Parallelism on Hierarchical Sequential Transducers

Исследование эффективного масштабирования генеративных рекомендаций с использованием параллелизма контекста на иерархических последовательных трансдюсерах. Работа предлагает новые методы для распределения вычислений при обучении и инференсе.

См. также: [[transformer_based_models.md]], [[ulysses_context_parallelism_method.md]]

### Twin-Flow Generative Ranking Network for Recommendation

Архитектура генеративной сети ранжирования с двойным потоком, позволяющая эффективно масштабировать рекомендательные системы. Twin-Flow разделяет моделирование пользовательских интересов и айтемов для улучшения производительности.

См. также: [[ranking.md]]

### InterFormer: Effective Heterogeneous Interaction Learning for Click-Through Rate Prediction

Новая архитектура трансформера для эффективного обучения гетерогенным взаимодействиям в задаче предсказания CTR. InterFormer позволяет эффективно интегрировать различные типы признаков и масштабировать модели.

См. также: [[interformer_architecture.md]], [[transformer_based_models.md]]

### MARM: Unlocking the Recommendation Cache Scaling-Law through Memory Augmentation and Scalable Complexity

Новый подход MARM (Memory-Augmented Recommendation Model), разблокирующий закон масштабирования кэша рекомендаций через аугментацию памяти и масштабируемую сложность. Работа исследует, как увеличение емкости памяти влияет на производительность рекомендательных систем.

См. также: [[traditional_approaches.md]]

### TBGRecall: A Generative Retrieval Model for E-commerce Recommendation Scenarios

Генеративная модель поиска, разработанная Alibaba для сценариев e-commerce рекомендаций. TBGRecall использует подход к предсказанию сессий и показывает эффективность генеративных методов в промышленных системах.

См. также: [[tbgrecall.md]], [[generative_retrieval_models.md]]

### RankMixer: Scaling Up Ranking Models in Industrial Recommenders

Архитектура, позволяющая масштабировать модели ранжирования в промышленных рекомендательных системах. RankMixer использует внимание между историей и кандидатами для более точного моделирования взаимодействий.

См. также: [[rankmixer_mtgr_transact_v2.md]]

### Climber: Toward Efficient Scaling Laws for Large Recommendation Models

Новый подход к эффективным законам масштабирования для больших рекомендательных моделей. Climber исследует, как различные архитектуры и методы обучения влияют на масштабирование рекомендательных систем.

См. также: [[transformer_based_models.md]]

### MTGR: Industrial-Scale Generative Recommendation Framework in Meituan

Промышленный фреймворк генеративных рекомендаций от Meituan, использующий графовые методы и мультизадачное обучение. MTGR (Multi-Task Graph Recommender) демонстрирует эффективность графовых подходов в масштабных системах.

См. также: [[rankmixer_mtgr_transact_v2.md]]

### Action is All You Need: Dual-Flow Generative Ranking Network for Recommendation

Новый подход к рекомендациям, где "действия" пользователей становятся основой для генеративных моделей. Dual-Flow архитектура эффективно моделирует как последовательности действий, так и айтемные представления.

См. также: [[ranking.md]]

### Meta's Generative Ads Model (GEM): The Central Brain Accelerating Ads Recommendation AI Innovation

Центральная генеративная модель рекламы от Meta, описывающая архитектуру GEM (Generative and Evolutionary Model). Модель внедрена и показала значительный рост конверсии в рекламе, становясь центральным элементом AI-инноваций в рекламе.

См. также: [[gem_model.md]]

### OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender

Единая архитектура трансформера для взаимодействия признаков и моделирования последовательностей в промышленных рекомендательных системах. OneTrans объединяет различные типы признаков в одной модели для лучшего масштабирования.

См. также: [[onetrans_unified_model.md]]

### Massive Memorization with Hundreds of Trillions of Parameters for Sequential Transducer Generative Recommenders

Исследование подходов к масштабному запоминанию с сотнями триллионов параметров для генеративных последовательных рекомендательных систем. Работа исследует, как увеличение параметров влияет на способность моделей запоминать и использовать прошлый опыт пользователей.

См. также: [[transformer_based_models.md]]

### From Features to Transformers: Redefining Ranking for Scalable Impact

Исследование эволюции подходов к ранжированию от традиционных методов к трансформерам, с фокусом на масштабируемость и влияние на бизнес-метрики.

См. также: [[transformer_based_models.md]], [[ranking.md]]

### From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction

Новый взгляд на трансформеры для предсказания CTR, где акцент делается на структурированной экспрессивности, а не просто на масштабировании. Работа предлагает более эффективные архитектуры для моделирования пользовательского поведения.

См. также: [[transformer_based_models.md]], [[target_aware_architectures_in_ranking.md]]

### Scaling Transformers for Discriminative Recommendation via Generative Pretraining

Применение генеративного предобучения для масштабирования трансформеров в дискриминативных рекомендательных системах. Подход позволяет эффективно масштабировать модели, используя знания, извлеченные из генеративных задач.

См. также: [[transformer_based_models.md]]

### Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations

Новый подход Meta Lattice к перепроектированию пространства моделей для экономически эффективных промышленных рекламных рекомендаций. Работа предлагает архитектуру, снижающую вычислительные затраты при сохранении качества.

См. также: [[transformer_based_models.md]]

## Связи с другими темами

- [[generative_retrieval_models.md]] - Генеративные модели поиска: родственные подходы к генеративным рекомендациям
- [[end_to_end_generative_recommendation_systems.md]] - End-to-end генеративные рекомендательные системы: контекст для понимания эволюции подходов
- [[llm_based/main.md]] - LLM-базированные рекомендательные системы: основа для LLM-подходов
- [[transformer_based_models.md]] - Трансформерные модели в системах рекомендаций: архитектурный контекст
- [[scaling_generative_recsys.md]] - Масштабирование генеративных рекомендательных систем: дополнительный контекст (предполагаемый файл)

## Источники

1. [OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment] - основная статья о подходе OneRec к унификации поиска и ранжирования в генеративных рекомендательных системах
2. [OneRec Technical Report] - технический отчет, описывающий архитектуру OneRec и внедрение в промышленной среде
3. [OneRec-V2 Technical Report] - расширенная версия OneRec с улучшениями архитектуры и масштабирования
4. [OneLoc: Geo-Aware Generative Recommender Systems for Local Life Service] - статья о генеративных системах для локальных сервисов с учетом географического контекста
5. [OneSug: The Unified End-to-End Generative Framework for E-commerce Query Suggestion] - исследование унифицированного подхода к генерации поисковых запросов
6. [OneSearch: A Preliminary Exploration of the Unified End-to-End Generative Framework for E-commerce Search] - предварительное исследование e-commerce поиска с генеративным подходом
7. [UniSearch: Rethinking Search System with a Unified Generative Architecture] - работа, пересматривающая поисковые системы через призму генеративных архитектур
8. [EGA-V1: Unifying Online Advertising with End-to-End Learning] - первая версия end-to-end фреймворка для рекламы от Meituan
9. [EGA-V2: An End-to-end Generative Framework for Industrial Advertising] - расширенная версия EGA с улучшениями для промышленного внедрения
10. [GPR: Towards a Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation] - подход к предобучению единой модели для рекламных рекомендаций
11. [PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations] - фундаментальная работа Google о применении LLM в промышленных рекомендациях
12. [OneRec-Think: In-Text Reasoning for Generative Recommendation] - расширение OneRec с возможностями логического вывода
13. [Align3GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation] - фреймворк для выравнивания на нескольких уровнях в LLM-рекомендациях
14. [GFlowGR: Fine-tuning Generative Recommendation Frameworks with Generative Flow Networks] - применение генеративных потоковых сетей для дообучения
15. [LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders] - подход к масштабированию длинных последовательностей
16. [Scaling Generative Recommendations with Context Parallelism on Hierarchical Sequential Transducers] - масштабирование с использованием параллелизма контекста
17. [Twin-Flow Generative Ranking Network for Recommendation] - архитектура с двойным потоком для эффективного ранжирования
18. [InterFormer: Effective Heterogeneous Interaction Learning for Click-Through Rate Prediction] - эффективное обучение гетерогенным взаимодействиям
19. [MARM: Unlocking the Recommendation Cache Scaling-Law through Memory Augmentation and Scalable Complexity] - архитектура с аугментацией памяти для масштабирования
20. [TBGRecall: A Generative Retrieval Model for E-commerce Recommendation Scenarios] - генеративная модель поиска для e-commerce от Alibaba
21. [RankMixer: Scaling Up Ranking Models in Industrial Recommenders] - архитектура для масштабирования моделей ранжирования
22. [Climber: Toward Efficient Scaling Laws for Large Recommendation Models] - подход к эффективным законам масштабирования
23. [MTGR: Industrial-Scale Generative Recommendation Framework in Meituan] - мультизадачный графовый рекомендательный фреймворк
24. [Action is All You Need: Dual-Flow Generative Ranking Network for Recommendation] - новый подход к рекомендациям через действия пользователей
25. [Meta's Generative Ads Model (GEM): The Central Brain Accelerating Ads Recommendation AI Innovation] - описание центральной генеративной модели рекламы от Meta
26. [OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender] - единая архитектура для взаимодействия признаков и моделирования последовательностей
27. [Massive Memorization with Hundreds of Trillions of Parameters for Sequential Transducer Generative Recommenders] - исследование масштабного запоминания в генеративных системах
28. [From Features to Transformers: Redefining Ranking for Scalable Impact] - эволюция подходов к ранжированию от признаков к трансформерам
29. [From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction] - новый взгляд на трансформеры для предсказания CTR
30. [Scaling Transformers for Discriminative Recommendation via Generative Pretraining] - масштабирование трансформеров через генеративное предобучение
31. [Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations] - перепроектирование пространства моделей для эффективных рекламных рекомендаций