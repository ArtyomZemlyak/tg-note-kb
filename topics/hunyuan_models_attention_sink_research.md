# Hunyuan Models and Attention Sink Research

## Overview

Hunyuan is a series of large language models developed by Tencent. The research around Hunyuan models has contributed to understanding phenomena such as attention sinks in mixture-of-experts (MoE) architectures.

## Hunyuan Model Series

- **Hunyuan-Large**: Currently one of the largest open-source Transformer-based mixture of experts models, with a total of 389 billion parameters and 52 billion activated parameters.
- **Hunyuan-0.5B-Instruct**: A smaller variant with 0.5B parameters in both pre-trained and instruction-tuned variants.
- **HunyuanOCR**: A lightweight Vision-Language Model specialized for OCR tasks.
- **Hunyuan Image 3.0**: A text-to-image model that was open-sourced by Tencent in September 2025.

## Attention Sink Research in MoE Models

### Research Context

The Hunyuan model series, particularly the MoE variants, has been used to study attention sink phenomena in large language models. Attention sinks are tokens that receive disproportionately high attention scores from other tokens in the sequence.

### Key Findings

- Attention sink phenomena are observed not only in dense transformer models but also in mixture-of-experts architectures like Hunyuan.
- The "Attention Sink Decay Rate" metric was designed to quantify the disruption to attention mechanisms when pruning super experts in MoE models.
- MoE models like Hunyuan exhibit attention sink behavior similar to dense models, with certain tokens consistently attracting excessive attention.
- The phenomenon is relevant for understanding how information flows through the expert routing mechanisms in MoE architectures.

### Implications for Hunyuan Models

- **Expert Routing**: Attention sinks could affect how tokens are routed to different experts in the mixture-of-experts architecture.
- **Model Efficiency**: Understanding attention sinks helps in optimizing the computational efficiency of MoE models like Hunyuan.
- **Quantization**: Attention sink behavior may impact how Hunyuan models behave when quantized for deployment.
- **KV Cache Management**: The attention sink phenomenon is relevant for optimizing key-value cache usage in long-context applications of Hunyuan models.

## Research Contributions

Research involving Hunyuan models has contributed to the broader understanding of:
- How attention sinks emerge during model pre-training
- The relationship between model scale and attention sink phenomena
- The impact of MoE architecture on attention sink behavior
- Potential mitigation strategies for attention sink-related issues

## References

- Research on Hunyuan-Large as an open-source MoE model with 52 billion activated parameters
- Studies on attention sink phenomena in large language models
- Empirical studies on when attention sinks emerge in language models during training