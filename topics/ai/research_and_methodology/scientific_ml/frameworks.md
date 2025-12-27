# Фреймворки для Scientific Machine Learning

## Обзор

Для эффективной реализации методов Scientific Machine Learning разработано несколько фреймворков, каждый из которых предлагает свои уникальные возможности и подходы. Эти инструменты упрощают разработку и реализацию SciML-решений.

## Основные фреймворки

### PINA (Physics-Informed Neural networks for Advanced modeling)

**PINA** — это открытая Python-библиотека, построенная на основе PyTorch, PyTorch Lightning и PyTorch Geometric, официально вошедшая в экосистему PyTorch. Основные особенности:

- Модульная архитектура для гибкой разработки
- Поддержка многоустройственного обучения
- Интеграция с PyTorch ecosystem
- Инструменты для решения дифференциальных уравнений

См. подробнее: [[pinn/pina_framework.md]]

### DeepXDE

**DeepXDE** — библиотека для решения дифференциальных уравнений с использованием глубокого обучения. Особенности:

- Поддержка различных типов уравнений
- Гибкие граничные условия
- Визуализация результатов
- Поддержка TensorFlow и PyTorch

### NeuralPDE.jl

**NeuralPDE.jl** — фреймворк на языке Julia для решения дифференциальных уравнений с использованием нейронных сетей. Особенности:

- Интеграция с DifferentialEquations.jl
- Поддержка различных типов PDE
- Автоматическое дифференцирование

### PyDEns

**PyDEns** — библиотека для решения дифференциальных уравнений с использованием нейронных сетей на Python. Особенности:

- Простой интерфейс
- Поддержка ODE и PDE
- Интеграция с PyTorch

## Сравнение фреймворков

| Фреймворк | Язык | Архитектура | Особенности | Интеграция |
|-----------|------|-------------|-------------|------------|
| PINA | Python | PyTorch-based | Модульная, масштабируемая | PyTorch, PyTorch Lightning |
| DeepXDE | Python | TensorFlow/PyTorch | Гибкие граничные условия | TensorFlow, PyTorch |
| NeuralPDE.jl | Julia | Julia-based | Интеграция с DifferentialEquations.jl | Julia ecosystem |
| PyDEns | Python | PyTorch | Простой интерфейс | PyTorch |

## Выбор фреймворка

При выборе фреймворка для SciML-задач следует учитывать:

- Тип решаемой задачи (ODE, PDE, обратные задачи)
- Требования к производительности
- Необходимость интеграции с существующей экосистемой
- Уровень зрелости и поддержки фреймворка
- Гибкость архитектуры

## Связи с другими темами

- [[pinn/pina_framework.md]] - Основной фреймворк PINA
- [[sciml_overview.md]] - Обзор Scientific Machine Learning
- [[applications.md]] - Применение фреймворков
- [[../tools/pytorch.md]] - PyTorch, основа для многих фреймворков

## Источники

1. [PINA: A PyTorch Framework for Solving Differential Equations by Deep Learning](https://iclr.cc/virtual/2024/21395) - Статья о фреймворке PINA
2. [DeepXDE: A Deep Learning Library for Solving Differential Equations](https://arxiv.org/abs/1902.04482) - Описание библиотеки DeepXDE
3. [NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximation](https://arxiv.org/abs/2107.09443) - Описание NeuralPDE.jl
4. [PINA Joins the PyTorch Ecosystem: A Unified Framework for Scientific Machine Learning](https://pytorch.org/blog/pina-joins-the-pytorch-ecosystem-a-unified-framework-for-scientific-machine-learning/) - Официальный анонс PINA в PyTorch