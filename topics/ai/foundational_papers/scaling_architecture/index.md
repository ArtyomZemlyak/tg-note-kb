# Архитектура, масштабирование и продвинутое обучение

## Обзор

Эта секция содержит работы, посвященные масштабированию нейронных сетей, эффективной архитектуре, и продвинутым методам обучения, которые позволяют тренировать огромные модели.

## Ключевые темы

### Масштабирование и эффективность
- [[gpipe_efficient_giant_nets.md]] - "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism" (Huang et al., 2019)
- [[scaling_laws_neural_language_models.md]] - "Scaling Laws for Neural Language Models" (Kaplan et al., 2020)
- [[compute_optimal_large_language_models.md]] - "Training Compute-Optimal Large Language Models" (Hoffmann et al., 2022)

### Модули отношения и передачи сообщений
- [[relational_reasoning_nets.md]] - "A Simple Neural Network Module for Relational Reasoning" (Santoro et al., 2017)
- [[neural_message_passing_quantum_chemistry.md]] - "Neural Message Passing for Quantum Chemistry" (Gilmer et al., 2017)

### Методы оптимизации
- [[distilling_knowledge_neural_nets.md]] - "Distilling the Knowledge in a Neural Network" (Hinton, Vinyals, Dean, 2015) - Знаменитая дистилляция знаний
- [[adam_method_stochastic_optimization.md]] - "Adam: A Method for Stochastic Optimization" (Kingma, Ba, 2014)
- [[batch_normalization_acceleration.md]] - "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift" (Ioffe, Szegedy, 2015)

### Теория и принципы
- [[gshard_scaling_giant_models.md]] - "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding" (Lepikhin et al., 2020)
- [[switch_transformers_sparse.md]] - "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity" (Fedus et al., 2021)

## Значение для глубокого обучения

Эти работы обеспечивают понимание того, как масштабировать нейронные сети до огромных размеров, эффективно обучать их и строить архитектуры, которые могут обрабатывать сложные отношения. Законы масштабирования особенно важны для понимания того, как характеристики производительности изменяются с увеличением масштаба моделей и данных.

## См. также

[[../attention_transformers/index.md]] - Трансформеры часто масштабируются до больших размеров
[[../generative_models/index.md]] - Генеративные модели также масштабируются