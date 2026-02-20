# Графовые нейронные сети в рекомендательных системах (GNNs for RecSys)

## Описание

Графовые нейронные сети (GNN) играют важную роль в современных рекомендательных системах. В отличие от традиционных подходов, GNN явно учитывают структуру взаимодействий между пользователями и айтемами, моделируя рекомендательную задачу как задачу на графе.

## Основные концепции

### User-Item граф

Рекомендательные системы естественным образом порождают графы, где user-item взаимодействия образуют двудольный граф. В этом случае:
- Матрица R (пользователь-айтем) → матрица смежности графа
- Задача рекомендаций (matrix completion) → link prediction на графе

![User-item граф как основа для GNN](../../../../media/img_1765027576_aqadbgtrgzboul_user_item.jpg) <!-- TODO: Broken image path -->

**Изображение показывает:** Составление двудольного графа из user-item взаимодействий, где вершины - пользователи и айтемы, а рёбра - взаимодействия. Матрица R становится матрицей смежности графа, а задача рекомендаций превращается в link prediction на графе.

### Проблемы традиционных подходов

- Матричная факторизация моделирует структуру графа неявно через задачу обучения
- Основной фокус на обучаемые эмбеддинги популярных айтемов
- У популярных айтемов много рёбер (высокая степень вершины), у хвостовых айтемов мало
- Требуется явное моделирование связей более высокого порядка
- Необходимо улучшить качество на хвостовых айтемах

## Категории моделей

### 1. Глубокие графовые модели

- **Neural Graph Collaborative Filtering (NGCF)** - использует message passing для распространения информации о предпочтениях
- **LightGCN** - упрощение NGCF с простым усреднением соседей
- **PinSage** - индуктивная модель с применением GraphSAGE для масштаба Pinterest

### 2. Случайные блуждания

- **Pixie** - biased random walks по графу для рекомендаций
- **DeepWalk, node2vec** - unsupervised подходы с обучением на результатах случайных блужданий

### 3. Гетерогенные графовые модели

- **TwHIN** - Twitter Heterogeneous Information Network
- **TTGL** - Graph Learning at TikTok

### 4. Контрастивное самообучение (2021-2025)

- **SGL** (Self-supervised Graph Learning) - контрастивное обучение с аугментациями графа
- **SimGCL** - упрощённое контрастивное обучение с добавлением шума
- **XSimGCL** - расширенная версия с адаптивным шумом и hard negatives
- **NCL** - Neighborhood-enriched Contrastive Learning

### 5. Методы с явными функциями потерь

- **DirectAU** - явные alignment и uniformity потери (текущий SOTA)
- **CGCL** - Cluster-level alignment
- **DCCL** - Disentangled Contrastive Learning

### 6. Продвинутые архитектуры (2024-2025)

- **LightGCL** - упрощённое контрастивное обучение
- **GFormer** - masked autoencoding для графов
- **HCCF/HGCF** - гиперболическая геометрия для иерархических отношений

## Применение в промышленности

### Pinterest
- Использование PinSage, MultiBiSage для масштабных рекомендаций
- Индуктивность позволяет обрабатывать новые пины
- Учет контента и структуры графа

### Twitter
- TwHIN для улучшения рекламы за счет данных из всей экосистемы

### TikTok
- TTGL как Foundation Graph Model
- Единое представление интересов пользователей и объектов

## Преимущества GNN в рекомендациях

- Явное моделирование структуры графа
- Учет связей более высокого порядка
- Улучшенная производительность на хвостовых айтемах
- Возможность работы с гетерогенными графами

## Современные методы и лучшие практики (2024-2025)

### Эволюция производительности

| Модель | Yelp2018 R@20 | Amazon-Book R@20 | Ключевая идея |
|--------|--------------|------------------|---------------|
| NGCF | 0.0560 | 0.0342 | Message passing с MLP |
| LightGCN | 0.0639 | 0.0411 | Упрощённая свёртка |
| SGL | 0.0675 | 0.0478 | Контрастивное обучение |
| SimGCL | 0.0680 | 0.0480 | Контрастивное обучение с шумом |
| DirectAU | 0.0703 | 0.0506 | Alignment + Uniformity |
| LightGCL | 0.0710 | 0.0515 | Упрощённое контрастивное |

### Рекомендации по выбору метода

- **Быстрый старт**: LightGCN — базовый уровень с минимальными настройками
- **Улучшенное качество**: SimGCL или DirectAU — баланс качества и сложности
- **Разреженные данные**: SGL/XSimGCL — контрастивное обучение особенно эффективно
- **Максимальное качество**: LightGCL или GFormer — state-of-the-art результаты
- **Ограниченные ресурсы**: LightGCN с 2 слоями и малой размерностью

### Лучшие практики

- **Инициализация**: Xavier/Glorot uniform для эмбеддингов
- **Число слоёв**: 2-3 слоя оптимально (глубже вызывает over-smoothing)
- **Размер батча**: 2048+ для методов с uniformity loss
- **Аугментации**: Edge dropout (p=0.2) предпочтительнее node dropout
- **Тренд**: Упрощение архитектур + principled loss design

## Ограничения и вызовы

- **Масштаб**: популярные айтемы могут иметь миллионы соседей
- **Холодный старт**: необходимость обработки новых узлов
- **Оверсмазивание (over-smoothing)**: проблема при глубоких GNN
- **Вычислительная сложность**: полные графы могут не помещаться в GPU

## Связи с другими темами

- [[gnn_architectures.md]] - Базовые архитектуры графовых нейронных сетей
- [[traditional_approaches.md]] - Сравнение с традиционными подходами к рекомендациям
- [[NGCF.md]] - Neural Graph Collaborative Filtering
- [[LightGCN.md]] - Light Graph Convolutional Network
- [[GraphSAGE.md]] - Индуктивные графовые представления
- [[PinSage.md]] - Приложение GraphSAGE в Pinterest
- [[Pixie.md]] - Случайные блуждания для рекомендаций
- [[TwHIN.md]] - Гетерогенные графы в Twitter
- [[TTGL.md]] - Графовое обучение в TikTok
- [[SGL_SimGCL.md]] - Методы контрастивного самообучения (SGL, SimGCL)
- [[DirectAU_alignment_uniformity.md]] - Методы с явными alignment/uniformity потерями
- [[modern_graph_recommendation_methods.md]] - Обзор современных методов и лучших практик

## Источники

1. [Stanford CS224W: GNNs for Recommender Systems] - лекции о применении GNN в рекомендательных системах
2. [NGCF: Neural Graph Collaborative Filtering] - статья об оригинальной модели NGCF
3. [LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation] - статья о LightGCN
4. [GraphSAGE: Inductive Representation Learning on Large Graphs] - оригинальная статья о GraphSAGE
5. [PinSage: Graph Convolutional Neural Networks for Web-Scale Recommender Systems] - статья о применении GraphSAGE в Pinterest
6. [TwHIN: Twitter Heterogeneous Information Network] - статья о Twitter графовой модели
7. [TTGL: Graph Learning at TikTok] - документация о графовом обучении в TikTok
8. [SGL: Self-supervised Graph Learning for Recommendation] - WWW 2021, статья о SGL
9. [SimGCL: Are Graph Augmentations Needed in Self-supervised Graph Learning for Recommendation?] - SIGIR 2022
10. [DirectAU: Direct Alignment and Uniformity for Collaborative Filtering] - 2023
11. [LightGCN and Its Improvements in Recommender System Research] - Zenn 2025, сравнение современных методов
12. [A Survey of Graph Neural Networks for Recommender Systems] - ACM TORS 2024, обзор области