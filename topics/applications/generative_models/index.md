# Generative Models

Generative models learn the underlying probability distribution of data to generate new, similar data samples.

## Overview

Unlike discriminative models that learn to classify or predict, generative models learn the joint probability distribution P(X,Y) to understand how data is generated. This enables them to create new samples that resemble the training data.

## Types of Generative Models

- Variational Autoencoders (VAEs) - Probabilistic graphical models
- Generative Adversarial Networks (GANs) - Competitive training approach
- Normalizing Flows - Exact likelihood models
- Diffusion Models - Denoising diffusion probabilistic models
- Autoregressive Models - Sequential generation models
- Energy-Based Models - Unnormalized probability distributions

## Common Architectures

- Variational Autoencoders (VAEs)
- Generative Adversarial Networks (GANs)
- Diffusion Models (DALL-E, Stable Diffusion)
- Flow-based Models
- Autoregressive Models (PixelCNN, WaveNet)
- Transformer-based Generators

## Applications

- Image synthesis and editing
- Text generation
- Music composition
- Drug discovery
- Data augmentation
- Style transfer

## Evaluation Metrics

- Inception Score (IS)
- Fréchet Inception Distance (FID)
- Learned Perceptual Image Patch Similarity (LPIPS)
- Kernel Inception Distance (KID)
- Diversity measures

## Related Topics

- [Neural Networks](../../algorithms/neural_networks/index.md) <!-- TODO: Broken link -->
- [Specialized Algorithms](../../algorithms/specialized/index.md) <!-- TODO: Broken link -->