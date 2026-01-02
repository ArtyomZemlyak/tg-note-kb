# Лучшие практики RAG: Обзор

## Описание

Сборник лучших практик и подходов для построения систем RAG (Retrieval-Augmented Generation), основанный на рекомендациях сообщества и ресурсах, собранных из различных источников, включая исследования, стримы и обсуждения.

RAG (Retrieval-Augmented Generation) - это архитектура, которая объединяет возможности поисковых систем и языковых моделей для генерации ответов на основе внешних знаний. Такие системы извлекают релевантные документы из внешнего источника и используют их как контекст для генерации ответов.

## Основные компоненты RAG

### 1. Chunking (Разбиение на фрагменты)
- Использование sliding window для эффективного разбиения
- Вдохновение можно почерпнуть из подходов Langchain
- Библиотека Chonkie для эффективного chunking'а без излишнего оверхеда

### 2. Векторные базы данных
- Для начала подойдет Chroma с алгоритмами IVF_Flat или HNSW
- Перспективы расширения до pgvector, Qdrant и других систем
- Важна производительность и масштабируемость системы

### 3. Модели эмбеддингов
- Для русскоязычных приложений: 
  - ai-forever/FRIDA
  - BAAI/bge-m3
  - intfloat/multilingual-e5-large
  - Qwen3-Embedding-8B

### 4. Реранжирование
- После KNN-поиска производить дополнительное ранжирование
- Модели для реранжирования:
  - BAAI/bge-reranker-v2-m3
  - Qwen3-Reranker-8B

### 5. Языковые и визуальные модели
- Базовая модель: qwen-2.5-7b-instruct
- Адаптированные версии:
  - RefalMachine/RuadaptQwen2.5-14B-Instruct
  - t-tech/T-lite-it-1.0
  - t-tech/T-pro-it-2.0

## Agentic RAG

- Использование Qwen3-30B-A3B-Instruct-2507 для построения агентных RAG-систем
- Репозиторий: https://github.com/vamplabAI/sgr-agent-core/tree/tool-confluence

## Фреймворки и инструменты

### Одобренные сообществом фреймворки:
- [Langgenius Dify](https://github.com/langgenius/dify/)
- [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG)
- [LlamaIndex](https://github.com/run-llama/llama_index)
- [Mastra](https://github.com/mastra-ai/mastra)

## Полезные ресурсы

### Академические работы:
- [Best RAG Practices](https://arxiv.org/abs/2407.01219) - комплексное исследование лучших практик RAG

### Презентации и исследования:
- Презентация от Дяди "Построение RAG систем от исследований до индустрии"
- Создатель ERC (Rinat Abdullin https://t.me/llm_under_hood) - https://abdullin.com/erc/

### Хорошо описанные подходы:
- Подходы от Богдана: https://t.me/bogdanisssimo/2047

### Решения и кейсы:
- Лучшее решение РАГ по документации от Ильи (@IlyaRice) - https://github.com/IlyaRice/RAG-Challenge-2/tree/main
- Кейс red_mad_robot по RAG (DCD) для строительной компании (t-lite) - https://habr.com/ru/companies/redmadrobot/articles/892882/
- Серия про file first от Рефата - https://t.me/nobilix/182

### Классика:
- Запись эфира по RAGу без эмбеддингов - https://t.me/oestick/397

## Связи с другими темами

- [[../../nlp/memory_architectures/retrieval_augmented_generation.md]] - Общая информация о RAG системах
- [[../../llm/memory/llm_memory_overview.md]] - Обзор систем памяти для LLM
- [[../retrieval_strategies.md]] - Стратегии поиска для RAG систем
- [[../embedding_models.md]] - Модели для генерации эмбеддингов

## Источники

1. [Best RAG Practices (2024)](https://arxiv.org/abs/2407.01219) - комплексное исследование лучших практик RAG систем, включающее анализ существующих подходов и рекомендации по оптимизации
2. [Langchain text splitters](https://github.com/langchain-ai/langchain/tree/master/libs/text-splitters) - библиотека с различными подходами к разбиению текста на фрагменты
3. [Chonkie library](https://github.com/chonkie-inc/chonkie) - специализированный фреймворк для chunking'а, разработанный как альтернатива тяжелым библиотекам
4. [RAG от Дяди](https://t.me/neuraldeep/1124) - стрим про RAG от автора сообщества
5. [ERC - Entity Relationship Chat](https://abdullin.com/erc/) - система, описывающая кейсы использования RAG технологий
6. [RAG Challenge 2](https://github.com/IlyaRice/RAG-Challenge-2/tree/main) - первое место на ERC2, лучшее решение RAG по документации
7. [red_mad_robot RAG кейс](https://habr.com/ru/companies/redmadrobot/articles/892882/) - реальный кейс внедрения RAG для строительной компании