# Attention Mechanisms

This section contains information about various attention mechanisms used in transformer architectures and neural networks.

## Basic Attention Mechanisms

- [[self_attention_mechanism.md]] - Fundamentals of self-attention
- [[scaled_dot_product_attention.md]] - The scaled dot-product attention mechanism
- [[multi_head_attention.md]] - Multi-head attention implementation

## Specialized Attention Mechanisms

- [[online_vector_quantized_attention_ovqa.md]] - Online Vector-Quantized Attention for efficient long-context processing
- [[dsa_with_top_k_selector.md]] - Dynamic Sparse Attention with Top-K Selector
- [[enhanced_mla_with_top_k_selector.md]] - Enhanced Matrix-Lens Attention with Top-K Selector
- [[dual_attention_loopcoder.md]] - Dual Attention mechanisms in LoopCoder
- [[attention_residuals_attnres.md]] - Attention Residuals: селективная агрегация представлений слоев через механизм внимания

## Advanced Topics

- [[why_three_matrices_q_k_v_instead_of_one.md]] - Explanation of why transformers use three separate matrices (Q, K, V) instead of one

## Overview

Attention mechanisms allow neural networks to focus on relevant parts of the input when making predictions. They have become a fundamental component of many state-of-the-art models, especially in natural language processing.

```metadata
category: machine_learning
subcategory: neural_networks
tags: ml, neural_networks, attention, transformers, algorithms
```