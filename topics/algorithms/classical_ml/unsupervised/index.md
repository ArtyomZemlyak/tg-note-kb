# Unsupervised Learning

## Общее описание

Unsupervised Learning (Обучение без учителя) — это тип машинного обучения, где модель обучается паттернам на немаркированных данных. Цель — обнаружить скрытые структуры или паттерны во входных данных без явного руководства.

## Основные задачи

### Кластеризация

Группировка похожих точек данных.

- [[kmeans_clustering.md]] — алгоритм K-Means (K-средних), математическая формулировка, проблемы производительности на GPU
- [[../../applications/clustering/index.md]] — общий раздел о методах кластеризации и их применении

### Снижение размерности

Coming soon...

### Другие задачи

Coming soon...

## Оптимизация алгоритмов

- [[../optimization/flash_kmeans.md]] — Flash-KMeans: оптимизированная GPU-реализация K-Means с ускорением до 200x

```metadata
category: machine_learning
subcategory: unsupervised_learning
tags: ml, unsupervised, clustering, dimensionality_reduction, algorithms
```