# Механизмы внимания и трансформеры

## Обзор

Эта секция содержит ключевые работы по механизмам внимания и архитектурам трансформеров, которые революционизировали обработку естественного языка и распространились на другие домены, включая зрение и аудио.

## Ключевые темы

### Ранние работы по вниманию
- [[neural_machine_translation_alignment.md]] - "Neural Machine Translation by Jointly Learning to Align and Translate" (Bahdanau et al., 2015) - Оригинальная работа о механизме внимания

### Архитектура трансформеров
- [[attention_all_you_need.md]] - "Attention Is All You Need" (Vaswani et al., 2017) - Оригинальная работа о трансформерах
- [[annotated_transformer.md]] - "The Annotated Transformer" (Rush, 2018) - Детальное объяснение архитектуры трансформера

### Визуализация и объяснение
- [[illustrated_transformer.md]] - "The Illustrated Transformer" (Alammar, 2018) - Визуальное объяснение трансформеров

### Трансформеры для NLP
- [[bert_pretraining_understanding.md]] - "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (Devlin et al., 2018)
- [[transformer_xl_attentive_language_models.md]] - "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context" (Dai et al., 2019)
- [[universal_transformers.md]] - "Universal Transformers" (Dehghani et al., 2019)

## Значение для глубокого обучения

Архитектура трансформеров, представленная в "Attention Is All You Need", стала поворотным моментом в глубоком обучении. Механизм внимания позволил моделям обрабатывать зависимости между элементами в последовательности независимо от расстояния между ними, что трудно для RNN. Это привело к появлению мощных языковых моделей, таких как BERT, GPT и других, и изменило подход к множеству задач в ИИ.

## См. также

[[../recurrent_neural_networks/index.md]] - RNN, которые частично заменены трансформерами
[[../convolutional_neural_networks/index.md]] - CNN, которые также применяются в трансформерах