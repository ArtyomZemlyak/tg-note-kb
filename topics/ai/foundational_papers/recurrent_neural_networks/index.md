# Рекуррентные нейронные сети и модели последовательностей

## Обзор

Эта секция содержит ключевые работы по рекуррентным нейронным сетям (RNN) и моделям для обработки последовательностей, включая LSTM, внимательность к последовательностям, и более ранние достижения в этой области.

## Ключевые темы

### Введение и понимание RNN
- [[unreasonable_effectiveness_rnn.md]] - "The Unreasonable Effectiveness of Recurrent Neural Networks" (Karpathy, 2015) - Блог-пост о возможностях RNN
- [[understanding_lstm.md]] - "Understanding LSTM Networks" (Olah, 2015) - Объяснение LSTM сетей

### Регуляризация и улучшения RNN
- [[rnn_regularization.md]] - "Recurrent Neural Network Regularization" (Zaremba et al., 2014)

### Рекуррентные архитектуры и расширения
- [[multidimensional_rnn.md]] - "Multi-Dimensional Recurrent Neural Networks" (Graves, Schmidhuber, 2007)
- [[grid_lstm.md]] - "Grid Long Short-Term Memory" (Kalchbrenner, Danihelka, Graves, 2015)
- [[supervised_sequence_labeling_rnn.md]] - "Supervised Sequence Labelling with Recurrent Neural Networks" (Graves, 2012) - Книга по RNN

### Нейросети с внешней памятью
- [[neural_gpu_learn_algorithms.md]] - "Neural GPUs Learn Algorithms" (Kaiser, Sutskever, 2015)
- [[pointer_networks.md]] - "Pointer Networks" (Vinyals et al., 2015)
- [[order_matters_seq2seq_sets.md]] - "Order Matters: Sequence to Sequence for Sets" (Vinyals et al., 2016)
- [[hypernetworks.md]] - "HyperNetworks" (Ha, 2016)

### Машины с внешней памятью
- [[neural_turing_machines.md]] - "Neural Turing Machines" (Graves et al., 2014)
- [[differentiable_neural_computers.md]] - "Hybrid computing using a neural network with dynamic external memory" (Graves et al., 2016) - DNC

### Отношения и рекуррентные сети
- [[relational_recurrent_nets.md]] - "Relational Recurrent Neural Networks" (Santoro et al., 2018)

## Значение для глубокого обучения

RNN и LSTM стали основой для обработки последовательностей в таких областях, как машинный перевод, распознавание речи и анализ временных рядов. Они позволили нейронным сетям работать с переменными по длине последовательностями и запоминать информацию на протяжении длительных промежутков времени. Работы по внешней памяти, такие как NTM и DNC, расширили возможности рекуррентных архитектур.

## См. также

[[../attention_transformers/index.md]] - Трансформеры, которые частично заменили RNN в многих задачах
[[../theoretical_foundations/index.md]] - Теоретические основы глубокого обучения