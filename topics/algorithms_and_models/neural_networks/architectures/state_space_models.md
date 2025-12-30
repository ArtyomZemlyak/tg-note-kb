# State Space Models

См. полное описание в [[../../transformer_architectures/architectures/state_space_models.md|основной статье о State Space Models]].

State Space Models (SSM) - это класс моделей для обработки последовательностей, который используется в архитектурах типа Mamba для эффективной обработки длинных последовательностей. SSM моделируют динамическую систему с внутренним состоянием, которое обновляется при поступлении новых входных данных.

## Ключевые компоненты SSM

SSM описывается системой уравнений:
- x(t) = Ax(t-1) + Bu(t)  (обновление состояния)
- y(t) = Cx(t) + Du(t)    (генерация выхода)

Где:
- u(t) - входной сигнал (токен на позиции t)
- x(t) - внутреннее состояние
- y(t) - выходной сигнал
- A, B, C, D - параметры модели

## Селективные механизмы

В моделях типа Mamba, SSM расширяется селективными механизмами, которые позволяют модели адаптивно фильтровать информацию и эффективно обрабатывать длинные последовательности с линейной сложностью.

Для полного описания теории и приложений State Space Models см. [[../../transformer_architectures/architectures/state_space_models.md]].

## Ссылки

- [[../../transformer_architectures/architectures/state_space_models.md]] - Подробное описание State Space Models
- [[mamba_architecture.md]] - Архитектура Mamba, использующая SSM
- [[selective_state_spaces.md]] - Селективные State Space Models

```metadata
category: neural_network_architectures
subcategory: sequential_models
tags: ssm, state_space_models, sequential_modeling, mamba
```