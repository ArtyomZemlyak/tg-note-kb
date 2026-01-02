# Основные связи и развитие моделей графовых нейронных сетей в рекомендациях

## Иерархия и эволюция моделей

### Graph Neural Networks (GNN) для рекомендаций
- [[graph_neural_networks_for_recommendations.md]] - Общее описание подхода
- [[traditional_approaches.md]] - Контекст традиционных методов

### Базовые GNN архитектуры
- [[NGCF.md]] - Neural Graph Collaborative Filtering
  - [[LightGCN.md]] - Упрощение NGCF (LightGCN)
- [[GraphSAGE.md]] - Индуктивная архитектура

### Промышленные применения
- [[Pixie.md]] - Случайные блуждания (ранний подход в Pinterest)
  - [[PinSage.md]] - Развитие GraphSAGE для промышленных рекомендаций
    - [[MultiBiSage.md]] - Расширение для нескольких графов
- [[TwHIN.md]] - Гетерогенная модель для Twitter
- [[TTGL.md]] - Графовое обучение для TikTok

### Подходы к обучению
- [[unsupervised_graph_learning.md]] - Обучение без учителя (DeepWalk, node2vec, metapath2vec)
- [[graph_neural_networks_for_recommendations.md]] - Сравнение подходов

## Ключевые инновации

### Индуктивность vs. трансдуктивность
- [[GraphSAGE.md]] и [[PinSage.md]] решают проблему холодного старта через индуктивность
- [[TwHIN.md]] - трансдуктивная модель с дообучением

### Масштабируемость
- [[PinSage.md]] - решение проблемы масштаба через сэмплирование соседей
- [[LightGCN.md]] - упрощение для эффективности

### Гетерогенные графы
- [[TwHIN.md]] - объединение разных типов данных
- [[TTGL.md]] - foundation graph model для всей экосистемы

### Сравнение подходов
- [[NGCF.md]] vs [[LightGCN.md]]: сложность vs. эффективность
- [[Pixie.md]] vs [[PinSage.md]]: простота vs. мощь GNN
- [[TwHIN.md]] vs [[TTGL.md]]: трансдуктивность vs. фундаментальная модель