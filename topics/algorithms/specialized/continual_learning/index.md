# Continual Learning

This section covers algorithms and techniques for continual learning - the ability of models to learn new tasks over time without forgetting previous knowledge.

## Categories

- [Catastrophic Forgetting](index.md) <!-- TODO: Broken link --> - Understanding and preventing knowledge loss
- [Class Incremental Learning](index.md) <!-- TODO: Broken link --> - Learning new classes over time
- [Rehearsal Methods](index.md) <!-- TODO: Broken link --> - Techniques to retain knowledge using past examples
- [Plasticity Methods](index.md) <!-- TODO: Broken link --> - Approaches to maintain adaptability
- [Hypernetwork-based Methods](../../../ai/llm/doc_to_lora.md) <!-- TODO: Broken link --> - Doc-to-LoRA и Text-to-LoRA для мгновенной адаптации

## Overview

Continual learning enables AI systems to accumulate knowledge over time, mimicking human-like learning capabilities while maintaining performance on previously learned tasks.

## Современные подходы

### Гиперсети для continual learning

- **Doc-to-LoRA** [[../../../ai/llm/doc_to_lora.md]] — использование гиперсетей для генерации LoRA-адаптеров из документов, решение проблемы долгосрочной памяти в LLM
- **Text-to-LoRA** [[../../../ai/llm/text_to_lora.md]] — генерация LoRA-адаптеров из описаний задач для мгновенной адаптации без переобучения