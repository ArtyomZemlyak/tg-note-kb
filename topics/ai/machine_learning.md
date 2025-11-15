# Машинное обучение (Machine Learning)

## Общее описание

Машинное обучение - это область искусственного интеллекта, которая изучает алгоритмы и статистические модели, позволяющие компьютерным системам выполнять задачи без явного программирования. Вместо этого системы учатся на данных и находят в них паттерны.

## Основные направления

### 1. Обучение с учителем (Supervised Learning)
- Алгоритмы обучаютcя на данных с известными метками
- Примеры: классификация, регрессия

### 2. Обучение без учителя (Unsupervised Learning)
- Модели находят паттерны в данных без известных меток
- Примеры: кластеризация, снижение размерности
- [[self_supervised_learning.md]] - Self-supervised learning: современная парадигма обучения на неотмеченных данных с автоматически создаваемыми обучающими сигналами

### 3. Обучение с подкреплением (Reinforcement Learning)
- Агент обучается принимать решения, взаимодействуя со средой
- Использует сигналы вознаграждения для улучшения поведения

### 4. Непрерывное обучение (Continual Learning)
- Модели учатся на последовательности задач без забывания предыдущих
- Включает в себя приращение класса и задачи
- Основные проблемы: катастрофическое забывание и потеря пластичности
- [[continual_learning/nested_learning.md]] - Вложенное обучение: новая парадигма ИИ от Google, решающая проблему катастрофического забывания

## Важные концепции

### Катастрофическое забывание
- Тенденция нейронных сетей забывать предыдущую информацию при обучении новой
- [[catastrophic_forgetting/catastrophic_forgetting.md]] - Подробнее о проблеме

### Потеря пластичности
- Проблема потери способности к обучению новой информации со временем
- [[plasticity/loss_of_plasticity.md]] - Подробнее о проблеме
- [[plasticity/dormant_units.md]] - Спящие юниты: механизм потери пластичности
- [[plasticity/continual_backpropagation.md]] - Continual Backpropagation: метод решения

### Приращение класса
- Сценарий, при котором модель обучается новым классам последовательно
- [[class_incremental_learning/class_incremental_learning.md]] - Подробнее о задаче

### Иерархические модели рассуждения
- Модели, которые используют многоуровневый подход к рассуждению и планированию
- [[reasoning_models/hierarchical_reasoning_model_hrm.md]] - Иерархическая Модель Рассуждения (HRM)
- [[reasoning_models/hrm_critique_analysis.md]] - Критический анализ HRM
- [[reasoning_models/tiny_recursive_model_trm.md]] - Крошечная Рекурсивная Модель (TRM) - упрощенная версия HRM
- [[reasoning_models/trm_vs_hrm_comparison.md]] - Сравнение TRM и HRM
- [[../llm/reasoning/thoughtbubbles_vs_others_comparison.md]] - Сравнение современных подходов к рассуждению, включая Thoughtbubbles

### Графовые нейронные сети
- [[graphs/gLSTM/gLSTM.md]] - gLSTM: архитектура для борьбы с over-squashing
- [[graphs/over_squashing.md]] - Проблема over-squashing в GNN

### Нейронные сети
- [[../kan/index.md]] - Сети Колмогорова-Арнольда (KAN): новая архитектура нейронных сетей, альтернатива MLP
- [[graphs/gLSTM/gLSTM.md]] - gLSTM: архитектура для борьбы с over-squashing
- [[graphs/over_squashing.md]] - Проблема over-squashing в GNN
- [[neuro_symbolic_systems.md]] - Нейросимволические системы: объединение нейронных и символических подходов
- [[symbolic_ai.md]] - Символический ИИ: классические подходы к представлению знаний и логическим рассуждениям

### Методы решения проблем
- [[rehearsal/experience_replay.md]] - Методы воспроизведения опыта
- [[regularization/elastic_weight_consolidation.md]] - Регуляризационные методы
- [[class_incremental_learning/memo_2022.md]] - Архитектурные методы (Memo)
- [[llm/optimization/smol_training_playbook.md]] - Руководство по эффективному обучению небольших моделей с использованием методов машинного обучения

## Связи с другими темами

- [[../reinforcement_learning/laser_reinforcement_learning.md]] - Связь с обучением с подкреплением в LLM
- [[../llm/llm_memory_systems/llm_memory_overview.md]] - Связь с системами памяти в LLM и проблемой катастрофического забывания
- [[../nlp/transformers/transformer_architecture.md]] - Архитектура трансформеров, основа современных LLM
- [[../nlp/models/speech_synthesis.md]] - Применение в обработке естественного языка
- [[../optimization/cpu/cpu_optimization.md]] - Оптимизация вычислительных процессов
- [[less_is_more_philosophy.md]] - Философия "меньше значит больше" в архитектурах ИИ
- [[memory_efficient_training.md]] - Память-эффективные методы обучения
- [[../knowledge_base_overview]] - Обзор всей базы знаний
- [[../knowledge_base_gaps_analysis]] - Анализ пробелов в базе знаний