# Generative Models

This section contains information about generative models in machine learning.

## Contents

- [[bitdance.md]] - BitDance: авторегрессионная генерация изображений с бинарными токенами и diffusion head
- [[representation_autoencoders_rae.md]] - Overview of Representation Autoencoders (RAE) for text-to-image generation
- [[scaling_diffusion_transformers_with_rae.md]] - Deep dive into scaling diffusion transformers using RAE
- [[technical_insights_rae_scaling.md]] - Technical insights on RAE scaling for text-to-image generation
- [[unified_latents_ul.md]] - Unified Latents (UL): диффузионная регуляризация латентов с контролем битрейта
- [[variational_autoencoders.md]] - Traditional VAE approaches for comparison
- [[diffusion_models.md]] - Foundation concepts for diffusion-based generation
- [[gan.md]] - Generative Adversarial Networks

## Overview

Generative models learn the underlying distribution of input data and can generate new samples that resemble the training data. These models are used for creating new content, data augmentation, and understanding data distributions.

Current focus areas include:
- Variational Autoencoders (VAE) and their alternatives
- Representation Autoencoders (RAE) for improved reconstruction and convergence
- Diffusion models for high-quality generation
- GANs for adversarial training approaches
- Autoregressive models with binary tokenization (BitDance) for fast image generation

```metadata
category: machine_learning
subcategory: generative_models
tags: ml, generative, gan, vae, rae, diffusion_models, creative_ai, text_to_image
```