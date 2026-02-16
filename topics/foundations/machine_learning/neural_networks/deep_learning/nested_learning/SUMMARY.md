# Вложенноe обучение (Nested Learning) - Обзор и связи

## Краткое описание

**Вложенноe обучение (Nested Learning, NL)** - это новая парадигма машинного обучения, предложенная в статье "Nested Learning: The Illusion of Deep Learning Architecture", которая представляет модели машинного обучения как систему связанных, многоуровневых задач оптимизации, каждая из которых имеет собственный поток контекста и частоту обновления.

## Темы, затронутые в материалах

### 1. Теоретические основы
- Математическое представление NL как вложенной системы оптимизаций
- Концепция ассоциативной памяти в NL
- Частоты обновления компонентов
- Нейронные обучающие модули

### 2. Оптимизационные аспекты
- Оптимизаторы как модули ассоциативной памяти
- Вложенные оптимизационные задачи
- Экспрессивные оптимизаторы (DGD, DMGD, GGD, M3)
- Архитектурно-специфичные оптимизаторы

### 3. Приложения и реализации
- Continuum Memory System (CMS)
- Hope архитектура
- Применения в непрерывном обучении и понимании длинного контекста
- Экспериментальные результаты

### 4. Связанные концепции
- Связь с традиционными архитектурами (трансформеры, RNN)
- Связь с метаобучением
- Связь с обучением в контексте и непрерывным обучением
- Нейрофизиологическая мотивация

## Связи с другими темами в базе знаний

[[foundations/machine_learning/neural_networks/index.md]] - Основы нейронных сетей, с которыми связано NL как новая парадигма
[[foundations/machine_learning/deep_learning/index.md]] - Глубокое обучение как контекст, в котором развивается NL
[[foundations/machine_learning/optimization/index.md]] - Оптимизация в машинном обучении, центральная тема в NL
[[foundations/machine_learning/architectures/transformers.md]] - Трансформеры как одна из архитектур, переосмысливаемых в NL
[[foundations/machine_learning/continual_learning.md]] - Непрерывное обучение, где NL показывает значительные улучшения
[[foundations/machine_learning/memory_augmented_networks.md]] - Системы с расширенной памятью, схожие с CMS в NL
[[foundations/machine_learning/recurrent_neural_networks.md]] - Рекуррентные сети как пример вложенных систем ассоциативной памяти

## Важные концепции и термины

- **Nested System of Associative Memories (NSAM)**: Система, в которой каждая оптимизационная задача представляет собой задачу ассоциативной памяти
- **Continuum Memory System (CMS)**: Обобщение традиционной концепции долгосрочной/краткосрочной памяти
- **Hope**: Архитектура, сочетающая самомодифицируемые Titans с CMS
- **Delta Gradient Descent (DGD)**: Обобщение градиентного спуска через дельта-правило
- **Multi-scale Momentum Muon (M3)**: Оптимизатор, основанный на CMS
- **Обучение в контексте (In-context learning)**: В NL рассматривается как прямое следствие наличия нескольких уровней в представлении NL

## Связи с нейрофизиологией

NL черпает вдохновение из работы человеческого мозга, особенно в аспектах:
- Мозговых осцилляций на разных временных масштабах
- Нейропластичности и универсальной архитектуры мозга
- Консолидации памяти через онлайн/офлайн процессы

## Источники информации

- Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, and Vahab Mirrokni. "Nested Learning: The Illusion of Deep Learning Architecture". arXiv:2512.24695, 2025.
- https://machinelearningatscale.substack.com/p/nested-learning-why-stacking-layers
- https://arxiv.org/abs/2512.24695

## Категории и теги

category: machine_learning
subcategory: deep_learning
tags: nested_learning, in_context_learning, continual_learning, optimization, associative_memory, cms, hope, transformers