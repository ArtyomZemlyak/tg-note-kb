# Механистическая интерпретируемость (Mechanistic Interpretability)

## Краткое описание

Механистическая интерпретируемость — это подход к пониманию внутренней работы нейронных сетей и особенно больших языковых моделей (LLM), сосредоточенный на выявлении точных вычислительных механизмов, лежащих в основе их поведения. В отличие от других подходов к интерпретируемости, которые могут фокусироваться на важности признаков или визуализации активаций, механистическая интерпретируемость стремится к "реверс-инжинирингу" модели, выявляя конкретные схемы (circuits) и вычислительные пути, ответственные за конкретные аспекты поведения.

## Основные концепции

### Направления исследований

1. **Схемы (Circuits)**: Специфические подмножества параметров модели, ответственные за конкретные вычислительные функции
2. **Индукционные головы**: Особый тип голов внимания, участвующих в процессе завершения паттернов и повторов
3. **Счетчики внимания (Attention Heads)**: Механизмы, позволяющие моделям отслеживать позиции и повторы
4. **Трансдьюсеры (Transducers)**: Специфические компоненты, отвечающие за последовательную обработку информации
5. **Информационно-теоретические подходы**: Анализ моделей с использованием концепций теории информации, таких как синергия и избыточность

### Методы анализа

- **Activation Patching**: Изменение активаций в определённых точках для понимания их роли
- **Circuit Analysis**: Картирование вычислительных путей через модель
- **Representation Analysis**: Изучение внутренних представлений и их изменения
- **Attention Analysis**: Изучение паттернов внимания и их роли в принятии решений
- **Information-Theoretic Methods**: Использование теории информации для анализа потоков информации (например, ΦID)

## Связи с другими темами

[[activation_oracles.md]] - Activation Oracles: метод интерпретации внутренних активаций с использованием естественного языка
[[attention_head_stability_circuit_universality.md]] - Стабильность attention-голов и универсальность схем: исследование воспроизводимости attention-голов при разных random seeds и последствия для circuit universality
[[synergistic_core_in_llms.md]] - Открытие синергетического ядра в LLM с использованием информационно-теоретических методов
[[phi_information_decomposition_phid.md]] - Информационно-теоретический метод для анализа динамики информации в LLM
[[partial_information_decomposition_pid.md]] - Фреймворк для декомпозиции информации на синергетическую, избыточную и уникальную
[[../../specialized/models_specific/sparse_autoencoders_interpretability.md]] - Метод для интерпретации внутреннего представления LLM
[[transcoders_for_interpretability.md]] - Инструменты для анализа внутренних состояний трансформеров
[[circuits_in_transformers_using_sae.md]] - Использование разреженных автоэнкодеров для открытия схем в трансформерах
[[feature_manifolds_geometry_counting.md]] — Многообразия признаков и геометрия счёта: как трансформеры выполняют арифметические задачи через манипуляции с низкоразмерными геометрическими структурами
[[../../neuroscience_principles_in_transformers.md]] - Принципы из нейронаук, применяемые к архитектурам трансформеров
[[../mechanistic_interpretability.md]] - Общее введение в механистическую интерпретируемость
[[path_patching.md]] - Path Patching: метод анализа влияния активаций на логиты
[[logit_lens.md]] - Logit Lens: метод анализа эволюции логитов по слоям
[[neural_ode.md]] - Нейронные ODE: анализ непрерывной эволюции скрытых состояний
[[partial_prompt_evaluation.md]] - Частичная оценка промптов (PPE): метод обнаружения проливов данных
[[functional_anchors.md]] - Функциональные якоря: слои, определяющие стратегию решения задачи
[[structural_adapters.md]] - Структурные адаптеры: слои, реализующие стратегию генерации токенов
[[jensen_shannon_divergence.md]] - Jensen-Shannon Divergence: информационно-теоретическая мера различия между распределениями

## Источники

1. Olah, C., et al. (2020). Zoom In: An Introduction to Circuits. Distill. https://distill.pub/2020/circuits/zoom-in/
2. Nanda, N., et al. (2020). Progress Measures for Grokking via Mechanistic Interpretability. arXiv preprint arXiv:2211.04808.
3. Cammarata, N., et al. (2020). Thread: Identifying and Controlling Neurons in Transformer LMs. Anthropic Blog.
4. Pedro Urbina-Rodriguez, Zafeirios Fountas, Fernando E. Rosas, Jun Wang, Andrea I. Luppi, Haitham Bou-Ammar, Murray Shanahan, Pedro A. M. Mediano. A Brain-like Synergistic Core in LLMs Drives Behaviour and Learning. 2026. https://arxiv.org/abs/2601.06851