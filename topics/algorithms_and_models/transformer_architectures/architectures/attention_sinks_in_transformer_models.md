# Attention Sinks in Transformer Models

## Definition

An attention sink is a phenomenon observed in transformer models where certain tokens in the input sequence receive disproportionately high cumulative attention scores from other tokens in the sequence. These tokens effectively "absorb" or "sink" attention, anchoring information flow through the model.

## Characteristics

- Attention sinks are tokens that consistently receive abnormally high attention scores across layers and heads
- The phenomenon is widespread, occurring even in models as small as 14M parameters
- Early tokens in the sequence (such as the beginning-of-sequence token ⟨bos⟩) often act as attention sinks
- The effect is caused by normalization and geometric constraints in attention mechanisms

## Emergence

- Attention sinks emerge during the pre-training phase of language models
- The phenomenon occurs in various types of transformer-based models, including mixture-of-experts (MoE) models
- The effect appears to be a fundamental characteristic of transformer attention mechanisms rather than a training artifact

## Implications

- **Model Quantization**: Attention sinks can impact how models behave when quantized
- **KV Cache Optimization**: Understanding attention sinks is important for optimizing key-value cache usage
- **Streaming**: The phenomenon affects how information flows through the model during streaming inference
- **Security**: Attention sinks may be relevant to certain security vulnerabilities in transformer models
- **Information Processing**: The phenomenon may reveal core mechanisms of how transformers process information internally

## Research Context

The attention sink phenomenon has been studied across different types of transformer models, including:
- Dense models
- Mixture-of-experts (MoE) models like Hunyuan
- Diffusion language models

## Mathematical Foundation

The attention mechanism in transformers typically follows the formula:
```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```
Where Q represents queries, K represents keys, and V represents values. The normalization through softmax and geometric constraints in the attention computation contribute to the emergence of attention sinks.

## References

- Xiao et al. (2024) identified attention sinks as a phenomenon where models disproportionately attend to initial tokens
- Several studies have documented the occurrence of attention sinks in both diffusion language models and traditional transformer models
- Research is ongoing to better understand the emergence and implications of this phenomenon

## See Also

- [[sparse_gating_mechanism_attention_sink_mitigation.md]] - Research on using sparse gating mechanisms to mitigate attention sink phenomena
- [[when_attention_sink_emerges_research_paper.md]] - Study on when attention sinks emerge during model training
- [[hunyuan_models_attention_sink_research.md]] - Investigation of attention sinks in mixture-of-experts architectures

```metadata
category: machine_learning
subcategory: transformer_architecture
tags: attention_mechanisms, attention_sinks, transformer_models
```