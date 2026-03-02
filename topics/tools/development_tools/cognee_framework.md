# Cognee: Открытый движок знаний для памяти ИИ-агентов

## Краткое описание

**Cognee** — это 100% open-source инструмент для самообучающейся памяти ИИ-агентов, который трансформирует сырые данные в постоянную и динамическую AI-память. В отличие от традиционных vector database, Cognee объединяет **векторный поиск с графовой базой данных**, создавая систему знаний с отношениями между сущностями.

**Ключевая проблема, которую решает Cognee:**
- Большинство AI-агентов ничего не помнят — каждый диалог для них как первый
- Vector search находит похожие куски текста, но не понимает связи между ними
- Документы остаются изолированными фрагментами без понимания отношений

**Решение Cognee:**
- Vector search + графовая база = поиск по смыслу + связи между сущностями
- Документы превращаются в knowledge graph с автоматическим извлечением сущностей и отношений
- Память, которая сохраняется, понимает связи и улучшается со временем

## Ключевые возможности

### 1. Composable Pipelines (Компонуемые пайплайны)

Можно собирать свои пайплайны обработки данных:

```
chunking → embedding → entity extraction → обработка
```

Cognee предоставляет гибкую систему для создания пользовательских задач и модульных пайплайнов с встроенными endpoint'ами для поиска.

### 2. Weighted Memory (Взвешенная память)

- Чем чаще используется связь — тем она сильнее
- Память адаптируется под реальное использование
- Приоритизация релевантных связей на основе частоты использования

### 3. Self-evolving Memory (Самоэволюционирующая память)

Пайплайн **memify** автоматически:
- Усиливает полезные связи
- Удаляет устаревшие данные
- Оптимизируется по принципам RL (Reinforcement Learning)

## Архитектура

```
┌─────────────────────────────────────────────────────────┐
│                    COGNEE ENGINE                        │
├─────────────────────────────────────────────────────────┤
│  Data Ingestion Layer (30+ источников данных)           │
│         ↓                                               │
│  Knowledge Graph Generation (cognify)                   │
│         ↓                                               │
│  Memory Algorithms (memify)                             │
│         ↓                                               │
│  Search & Query Layer                                   │
└─────────────────────────────────────────────────────────┘
          ↓                    ↓
    Vector Database      Graph Database
    (Semantic Search)    (Relationship Mapping)
```

## Как это работает (6 строк кода)

### Python API

```python
import cognee
import asyncio

async def main():
    await cognee.add("Cognee turns documents into AI memory.")  # Поглощение данных
    await cognee.cognify()        # Генерация графа знаний
    await cognee.memify()         # Добавление алгоритмов памяти
    results = await cognee.search("What does Cognee do?")  # Поиск

asyncio.run(main())
```

### CLI интерфейс

```bash
cognee-cli add "your text"      # Добавление данных
cognee-cli cognify              # Генерация графа знаний
cognee-cli search "your query"  # Семантический поиск
cognee-cli ui                   # Открыть локальный UI
```

## Технические детали

### Векторный поиск + Графовая база

| Компонент | Описание |
|-----------|----------|
| **Vector Search** | Семантический поиск по всем поглощенным данным через эмбеддинги |
| **Graph Database** | Neo4j поддержка, автоматическое извлечение сущностей и отношений через `cognify()` |
| **Knowledge Graphs** | Автогенерация из сырых документов, поддержка пользовательского извлечения сущностей/отношений |

### Поддерживаемые источники данных

- **30+ источников данных**: conversations, files, images, audio transcriptions
- Pythonic data pipelines для ingestion
- Мультимодальная поддержка: текст, изображения, аудио транскрипции, разговоры

### Интеграция с LLM

- OpenAI, Ollama и другие провайдеры
- Graph-RAG: комбинация retrieval-augmented generation с graph traversal
- Встроенные endpoint'ы для поиска и извлечения

## Установка и требования

```bash
# Установка через uv
uv pip install cognee

# Требования
- Python 3.10 to 3.13
- LLM API Key (OpenAI или другие провайдеры)
```

## Структура репозитория

| Компонент | Назначение |
|-----------|------------|
| `cognee/` | Основное ядро движка |
| `cognee-mcp/` | MCP интеграция |
| `cognee-starter-kit/` | Шаблоны для быстрого старта |
| `examples/` | Примеры использования |
| `evals/` | Инструменты оценки |
| `notebooks/` | Jupyter ноутбуки |

## Статистика проекта

- **GitHub**: https://github.com/topoteretes/cognee
- **Звёзды**: 12.8k stars, 1.3k forks
- **Лицензия**: Apache-2.0
- **Языки**: 93% Python, 7% TypeScript
- **Исследование**: arXiv paper published 2025

## Use Cases (Сценарии использования)

| Сценарий | Применение |
|----------|------------|
| **AI Agent Memory** | Постоянная, динамическая память для автономных агентов |
| **GraphRAG Systems** | Улучшенный retrieval с контекстом отношений |
| **Document Q&A** | Семантический поиск по коллекциям документов |
| **Conversation History** | Хранение и извлечение прошлых взаимодействий агент-пользователь |
| **Multi-Source Knowledge** |Unified knowledge из файлов, баз данных, API |

## Преимущества

| Преимущество | Описание |
|--------------|----------|
| **Data Interconnection** | Соединяет любые типы данных: разговоры, файлы, изображения, аудио транскрипции |
| **Unified Knowledge Engine** | Заменяет традиционные database lookups на graphs + vectors |
| **High Customizability** | Пользовательские задачи, модульные пайплайны, встроенные search endpoints |
| **Reduced Infrastructure Cost** | Меньше усилий разработчика при улучшении точности |
| **Self-Improvement** | Знания эволюционируют по мере изменения данных |

## Исследование

Опубликованная работа: **"Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning"** (arXiv:2505.24478, 2025)

**Авторы**: Vasilije Markovic, Lazar Obradovic, Laszlo Hajdu, Jovan Pavlovic

## Ресурсы

- **Документация**: www.cognee.ai
- **GitHub**: https://github.com/topoteretes/cognee
- **Discord**: Community support
- **Reddit**: r/AIMemory
- **Лицензия**: Apache-2.0

## Связи с другими темами

- [[memory_systems_for_ai_agents.md]] - **Системы памяти для ИИ-агентов**: обзор архитектурных подходов к памяти
- [[foundation_agent_memory_taxonomy.md]] - **Таксономия памяти фундаментальных агентов**: единый фреймворк классификации по трём измерениям (субстрат, когнитивный механизм, субъект)
- [[mem0_framework.md]] - **Mem0**: масштабируемая архитектура памяти с векторным хранением и графовой версией Mem0g
- [[memoryos_framework.md]] - **MemoryOS**: иерархическая система памяти для агентов
- [[general_agentic_memory_gam.md]] - **General Agentic Memory (GAM)**: JIT-компиляция памяти через Deep Research
- [[rl_for_memory_management.md]] - **Обучение с подкреплением для управления памятью**: RL-подходы к оптимизации операций с памятью (ADD, UPDATE, DELETE)
- ../../applications/nlp/rag/index.md - **RAG системы**: Retrieval-Augmented Generation, основа для агентов с доступом к знаниям
- [[knowledge_graphs.md]] - **Графы знаний**: представление знаний в виде связанных сущностей
- [[context_engineering/index.md]] - **Контекстная инженерия**: управление рабочей памятью агентов

## Источники

1. **Cognee GitHub Repository**
   - URL: https://github.com/topoteretes/cognee
   - Звёзды: 12.8k stars, 1.3k forks
   - Лицензия: Apache-2.0
   - Дата обращения: 2026-03-02

2. **Cognee Official Documentation**
   - URL: https://www.cognee.ai
   - Описание: Официальная документация и руководства по использованию

3. **Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning**
   - arXiv: https://arxiv.org/abs/2505.24478
   - Авторы: Vasilije Markovic, Lazar Obradovic, Laszlo Hajdu, Jovan Pavlovic
   - Год: 2025

4. **Implementing Long Term Memory for Google ADK using Cognee**
   - URL: https://medium.com/google-developer-experts/implementing-long-term-memory-tool-for-google-adk-bb7ee83d22fe
   - Дата публикации: 2025-12-31

5. **Cognee Community Repository**
   - URL: https://github.com/topoteretes/cognee-community
   - Описание: Community-managed plugins и addons для Cognee

## См. также

- [[diffmem_git_based_memory.md]] - Git-базированная дифференциальная память
- [[wikontic.md]] - Пайплайн для извлечения графов знаний
- [[agentic-flow/index.md]] - Платформа для оркестрации ИИ-агентов
