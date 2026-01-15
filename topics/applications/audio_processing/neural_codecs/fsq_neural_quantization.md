# Finite Scalar Quantization (FSQ)

## Overview

Finite Scalar Quantization (FSQ) is an alternative to vector quantization that operates on scalar dimensions independently. Unlike traditional VQ methods that use codebooks, FSQ treats quantization as a direct mapping of continuous values to discrete levels.

## Methodology

FSQ maps continuous latent vectors to discrete tokens by:

1. Projecting continuous vectors through tanh to range (-1, 1)
2. Quantizing each dimension to discrete levels (e.g., L = [4, 4, 4, 4])
3. Packing indices using mixed-radix numeral systems

## Advantages

- No need for training codebook embeddings
- Deterministic quantization
- Better gradient flow during training

## Applications

- Neural audio codecs
- Discrete representation learning
- Latent space discretization

## Metadata
```metadata
category: quantization
subcategory: neural_methods
tags: quantization, fsq, neural_networks, discrete_representations
```