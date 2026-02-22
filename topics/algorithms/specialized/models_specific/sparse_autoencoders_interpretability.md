# Sparse Autoencoders (SAE) for Model Interpretability

## Definition
Sparse Autoencoders (SAEs) are neural networks designed to learn sparse representations of input data. They consist of an encoder that maps inputs to a sparse latent representation and a decoder that reconstructs the input from this representation.

## Purpose in LLM Analysis
SAEs serve as tools for interpretability and understanding of neural network representations in large language models. They enable researchers to:
- Identify meaningful features in neural networks
- Understand how information is encoded and processed
- Compare architectural differences between models
- Analyze the geometry of learned representations

## Applications in Clinical Reasoning Analysis
SAEs have been applied to understand why Large Language Models fail in clinical reasoning despite high benchmark performance. Through SAE analysis, researchers discovered:
- Different models encode information differently
- MedGemma shows bias toward storing multiple significant features in one SAE region while contextual meaning is localized in other areas
- OpenBioLLM exhibits more uniform information encoding without clear separation

## Advantages
- Enable detailed analysis of model internals
- Allow comparison of architectural approaches across different models
- Provide insights into feature representations
- Help identify potential failure modes in specific domains

## Limitations
- Time-consuming and computationally intensive to train
- Training for specific domains requires expertise and resources
- Results may represent artifacts rather than definitive insights
- Sensitivity to model retraining needs validation
- Optimal SAE training strategies for specific applications remain under research

## Challenges
- Training SAEs requires significant computational resources
- Proper evaluation of SAE quality is complex
- Interpreting SAE features can be subjective
- SAE effectiveness varies across model architectures and domains

## Research Directions
- Optimizing SAE training for domain-specific applications
- Developing faster and more efficient SAE training methods
- Improving the interpretability of SAE features
- Creating standardized evaluation protocols for SAEs

## Применение SAE в диффузионных моделях (DLM-Scope)

**DLM-Scope** — первый фреймворк интерпретируемости на основе SAE для диффузионных языковых моделей (Diffusion Language Models). Работа представляет пионерское исследование, адаптирующее методы SAE для архитектур, отличных от авторегрессивных.

### Ключевые особенности применения SAE в DLM

1. **Формализация активаций**: В отличие от авторегрессивных моделей, в DLM требуется отдельная формализация того, какие активации имеет смысл использовать для обучения SAE. Учитывается временная динамика процесса денойзинга и маскированные токены.

2. **Валидация через диффузионный loss**: Осмысленность SAE проверяется заменой активаций слоя реконструкцией и измерением изменения диффузионной функции потерь. Интересно, что вставка SAE в ранних слоях может даже **снижать диффузионный loss**, что отличается от типичных наблюдений в авторегрессивных моделях.

3. **Steering во времени**: Управление поведением модели через SAE становится процессом, распределённым во времени, а не одноразовым сдвигом в пространстве активаций. Реализованы две стратегии:
   - Вмешательство во все токены
   - Вмешательство только в обновляемые токены

4. **Перенос между моделями**: Обнаружено сохранение и перенос SAE-признаков между base и instruction-tuned моделями, что сходно с наблюдениями в авторегрессивных моделях.

### Выпущенные модели

Авторы DLM-Scope выложили обученные SAE для:
- **Dream-7B** — 7-миллиардная диффузионная языковая модель
- **LLaDA-8B** — 8-миллиардная диффузионная языковая модель

## Связи с другими темами

- [[../../diffusion_models/interpretability/dlm_scope_sae.md]] — подробное описание фреймворка DLM-Scope для интерпретируемости диффузионных моделей
- [[../../../foundations/interpretability/mechanistic_interpretability/sparse_autoencoders/reasoning_features_identification.md]] — идентификация признаков рассуждения с помощью SAE
- [[../../../ai/llm/mechanistic_interpretability/logit_lens.md]] — другие методы интерпретируемости

## Источники

1. **DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders**. arXiv:2602.05859, февраль 2026.
   - URL: https://arxiv.org/abs/2602.05859
   - Первый фреймворк SAE-интерпретируемости для диффузионных языковых моделей