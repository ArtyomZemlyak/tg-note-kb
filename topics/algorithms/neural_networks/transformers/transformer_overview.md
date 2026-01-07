# Трансформеры (Transformers)

## Определение

Трансформеры - это архитектура нейронных сетей, основанная на механизмах внимания (attention), которая преобразовала области обработки естественного языка, компьютерного зрения и других доменов.

## Архитектура

### Основные компоненты

- **Механизм внимания (Attention)** - позволяет модели фокусироваться на различных частях входных данных
- **Остаточные соединения (Residual Connections)** - обеспечивают стабильную передачу сигналов
- **Нормализация (Layer Normalization)** - стабилизирует обучение
- **Позиционные кодировки (Positional Encoding)** - добавляют информацию о позиции элементов

## Математическая формулировка

Трансформерный слой включает:
```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h)W^O
```
где:
```
head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```

## История

- Введены в работе "Attention is all you need" (Vaswani et al., 2017)
- Ставшие основой для всех современных крупных языковых моделей

## Применения

- Обработка естественного языка (BERT, GPT)
- Компьютерное зрение (Vision Transformers)
- Генерация кода
- Многомодальные модели

## Связи с другими темами

- [[ai/deep_learning/architectures/mhc_manifold_constrained_hyper_connections.md]] - улучшения остаточных соединений в трансформерах
- [[computer_science/deep_learning/residual_connections.md]] - базовая компонента трансформеров

## Источники

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing systems, 30.