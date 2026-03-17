# Оптимизация LLM

## Краткое описание

Этот раздел посвящен различным методам оптимизации больших языковых моделей (LLM), включая техники сжатия, квантования, прунинга и параметрически эффективного обучения. Эти методы позволяют улучшить производительность моделей, снизить вычислительные требования и ускорить инференс.

## Основные темы

- [[compress_to_impress_single_gradient_llm_adaptation.md]] - Метод адаптации LLM за один шаг градиентного спуска
- [[evolution_strategies_optimization.md]] - Оптимизация LLM с помощью эволюционных стратегий
- [[intrinsic_dimensionality.md]] - Внутренняя размерность в обучении LLM
- [[laser_layer_selective_rank_reduction.md]] - Оригинальный метод понижения ранга без обучения
- [[lora_optimization.md]] - Low-Rank Adaptation (LoRA) для оптимизации LLM
- [[structured_pruning.md]] - Структурированный прунинг в LLM
- [[smol_training_playbook.md]] - Руководство по эффективному обучению небольших языковых моделей
- [[techniques_for_small_models.md]] - Конкретные техники эффективного обучения небольших моделей
- [[../ouro_llm.md]] - Ouro-LLM: подход к параметрической эффективности через зацикленные архитектуры
- [[kv_cache_optimization.md]] - Оптимизация KV-кеширования
- [[kvzap_kv_cache_pruning.md]] - Методы сжатия KV-кэшей
- [[attention_locality_kv_cache_optimization.md]] - Оптимизация через локальность внимания
- [[pre_rope_post_rope_optimization.md]] - Оптимизация до и после применения RoPE
- [[shadowkv_comprehensive_analysis.md]] - Комплексный анализ ShadowKV
- [[sequential_attention.md]] - Sequential Attention: подход к эффективному выбору подмножества с механизмом внимания
- [[idap_plus_plus.md]] - IDAP++: продвинутый метод дивергенс-ориентированного прунинга через фильтровую и слоевую оптимизацию
- [[low_precision_training_instability.md]] - Анализ нестабильности низкоточного обучения трансформеров с Flash Attention (BF16 ошибки округления, loss explosion)