# HPC-Ops: Tencent High-Performance Computing Operations Framework

![HPC-Ops Prefill Performance Visualization](image_prefill.jpg) <!-- TODO: Broken image path -->

## Overview
HPC-Ops is a working library released by Tencent Hunyuan AI Infra that powers their own infrastructure for production-scale large model inference. The framework was rebuilt from scratch using pure CUDA and CuTe specifically for the Hopper architecture to maximize GPU utilization and squeeze out maximum performance from H100 and H200 GPUs.

## Architecture & Design Philosophy
- Built specifically for Hopper architecture (SM90 cards)
- Pure CUDA and CuTe implementations
- Designed to maximize GPU utilization rather than patching older solutions
- Addresses limitations of popular solutions like vLLM or default FlashAttention that don't fully utilize hardware capabilities

## Core Components
- Optimized attention kernels with paged attention
- Quantized Grouped GEMM with FP8 support and block scaling
- Fused Mixture of Experts (Fused MoE)
- Distributed system node communication tools for multi-GPU setups

## Performance Achievements
- **Overall throughput**: 30% increase for Tencent's own models
- **Cross-model performance**: 17% improvement for DeepSeek models
- **H20 acceleration**: Up to 2.22x speedup compared to previous solutions

### Decoding Performance
- BF16 attention mechanism: 2.2x faster than FlashInfer, FlashAttention, and TensorRT-LLM combination
- FP8 decoding: 2x speedup improvement
- FusedMoE in FP8: nearly 50% speed increase in prefill mode

### Prefill Performance
- Overall prefill improvement: ~1.33x (more modest gains than decoding)
- FP8 prefill: Pleasant 12% speed improvement

## Compatibility
- Works with vLLM and SGLang ecosystems
- Requires SM90 architecture (Hopper) cards - not compatible with older hardware

## Future Roadmap
- Sparse attention implementation
- 4-bit quantization support
- New kernels that merge computation and data transfer between GPUs

## Technical Context
Production deployment of large models is expensive at scale, motivating efforts to optimize every percentage point of performance. HPC-Ops addresses this by focusing on maximum GPU load utilization, making it valuable for organizations optimizing inference on Hopper architectures where token-per-second efficiency is critical.

## Licensing
MIT License

## Key Application Areas
- Large model inference optimization
- High-performance computing for AI workloads
- GPU resource maximization for production systems