# Сравнение архитектур современных LLM

## Описание

Детальный обзор архитектур ведущих моделей больших языковых моделей (LLM) 2025 года, включая DeepSeek V3/R1, OLMo 2, Gemma 3, Mistral Small 3.1, Llama 4, Qwen3, SmolLM3, Kimi K2, GPT-OSS, Grok 2.5, GLM-4.5 и Qwen3-Next.

## Подкатегории

- [[models/deepseek_v3.md|DeepSeek V3/R1]] - Архитектура с многоголовым латентным вниманием
- [[models/olmo_2.md|OLMo 2]] - Модель с пост-нормализацией и QK-нормализацией
- [[models/gemma_3.md|Gemma 3]] - Модель с вниманием со скользящим окном
- [[models/mistral_small_31.md|Mistral Small 3.1]] - Модель с фокусом на низкую задержку
- [[models/llama_4.md|Llama 4]] - Модель с архитектурой смеси экспертов
- [[models/qwen3.md|Qwen3]] - Серия моделей с плотными и MoE архитектурами
- [[models/smollm3.md|SmolLM3]] - Компактная модель с NoPE
- [[models/kimi_k2.md|Kimi K2]] - Триллионная модель с Muon оптимизатором
- [[models/gpt_oss.md|GPT-OSS]] - Открытая модель от OpenAI
- [[models/grok_25.md|Grok 2.5]] - Производственная модель xAI
- [[models/glm_45.md|GLM-4.5]] - Гибрид инструкций и рассуждений
- [[models/qwen3_next.md|Qwen3-Next]] - Улучшенная архитектура с DeltaNet

## Технические концепции

- [[techniques/multi_head_latent_attention.md|MLA]] - Многоголовое латентное внимание
- [[techniques/mixture_of_experts.md|MoE]] - Смесь экспертов
- [[techniques/sliding_window_attention.md|SWA]] - Внимание со скользящим окном
- [[techniques/no_positional_embeddings.md|NoPE]] - Без позиционных эмбеддингов
- [[techniques/qk_normalization.md|QK-Norm]] - Нормализация запросов и ключей
- [[../log_linear_attention.md|Log-Linear Attention]] - Промежуточный вариант между стандартным и линейным вниманием

## Ключевые архитектурные инновации

Современные LLM используют различные подходы для повышения эффективности, масштабируемости и производительности:

1. **Экономия памяти**: MLA, Sliding Window Attention, MoE
2. **Стабилизация обучения**: QK-Normalization, Post-Normalization, Attention Sinks
3. **Масштабируемость**: Гибридные архитектуры, Multi-Token Prediction
4. **Оптимизация инференса**: Gated DeltaNet, Sparse vs Dense модели

## Технические концепции (дополнительно)

- [[speed_always_wins_survey.md|Обзор Speed Always Wins]] - Систематизация ключевых инноваций в области эффективных архитектур для LLM
- [[linear_sequence_modeling.md|Линейное моделирование последовательностей]] - Подходы, сводящие сложность внимания к линейной
- [[sparse_sequence_modeling.md|Разреженное моделирование последовательностей]] - Подходы, ограничивающие взаимодействия между токенами
- [[hybrid_architectures.md|Гибридные архитектуры]] - Комбинации быстрых и мощных слоев
- [[diffusion_llm_architectures.md|Диффузионные LLM]] - Невавторегрессивные модели с параллельной генерацией
- [[flash_attention_and_grouped_mechanisms.md|FlashAttention и групповые механизмы]] - Оптимизация полного внимания

## Связи с существующими темами

- [[../llm_architectures_comparison.md|Общее сравнение архитектур LLM]] - Базовое сравнение encoder-only, decoder-only и encoder-decoder архитектур
- [[../mixture_of_experts_architecture.md|Архитектуры MoE]] - Подробное описание подходов с смесью экспертов
- [[../specialized_attention_mechanisms.md|Специализированные механизмы внимания]] - Дополнительные техники внимания, используемые в современных LLM
- [[../../nlp/transformers/transformer_architecture.md|Архитектура трансформеров]] - Основы архитектуры, на которой основаны современные LLM