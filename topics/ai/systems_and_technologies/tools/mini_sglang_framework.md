# Mini-SGLang Framework

## Overview

Mini-SGLang is a lightweight yet high-performance inference framework for Large Language Models. It serves as a compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems. With a compact codebase of approximately 5,000 lines of Python, it functions as both a capable inference engine and a transparent reference for researchers and developers.

## Key Features and Characteristics

### Educational and Research-Focused
- **Compact Codebase**: Only 5k lines of Python code compared to ~300k lines in the original SGLang, making it significantly easier for learners and researchers to understand core components of modern LLM serving engines
- **Modular and Readable**: Clean, modular, and fully type-annotated codebase that is easy to understand and modify
- **Research Prototyping**: Designed to facilitate the integration of new optimizations by researchers who might struggle with complex frameworks

### High Performance
- **State-of-the-Art Throughput**: Achieves performance comparable to the full SGLang with advanced optimizations
- **Efficient Resource Utilization**: Advanced optimizations without sacrificing performance

### Advanced Optimizations
- **Radix Cache**: Reuses KV cache for shared prefixes across requests, improving efficiency
- **Chunked Prefill**: Reduces peak memory usage for long-context serving
- **Overlap Scheduling**: Hides CPU scheduling overhead with GPU computation, mitigating CPU overhead that can lead to GPU idling
- **Tensor Parallelism**: Scales inference across multiple GPUs
- **Optimized Kernels**: Integrates FlashAttention-3 for prefill kernel and FlashInfer for decode kernel on NVIDIA Hopper architecture
- **Just-in-Time (JIT) Compilation**: For better runtime performance

## Architecture

### System Components
- **Frontend API Server**: Handles incoming requests and communication protocols
- **Tokenizer Server**: Manages tokenization processes
- **Backend Scheduler**: Manages GPU-specific scheduling and computation

### Technical Implementation
- Primarily implemented in Python (~76% of codebase)
- Includes CUDA (8.9%), C (8.3%), and C++ (6.6%) for performance-critical components
- Supports OpenAI-compatible API serving
- Provides both online serving and interactive shell capabilities

## Performance and Benchmarks

### Offline Inference
- Tested on 1xH200 GPU with Qwen3-0.6B and Qwen3-14B models
- 256 sequences with random input length (100-1024 tokens)
- Random output length (100-1024 tokens)

### Online Inference
- Tested on 4xH200 GPUs (NVLink connected) with Qwen3-32B model
- Using Qwen trace dataset, replaying first 1000 requests
- Performance comparison shows nearly identical performance between Mini-SGLang and SGLang
- Both achieved similar throughput, P90 TTFT (Time To First Token), and TBT (Time Between Tokens)

## Usage and Deployment

### Installation and Setup
- Environment setup using `uv` package manager
- Single-command deployment for OpenAI-compatible API servers

### Example Usage
```bash
# Single GPU deployment
python -m minisgl --model "Qwen/Qwen3-0.6B"

# Multi-GPU deployment with tensor parallelism
python -m minisgl --model "meta-llama/Llama-3.1-70B-Instruct" --tp 4 --port 30000
```

### Additional Features
- Interactive shell mode for direct command-line interaction
- Out-of-the-box support for models like Llama-3 and Qwen-3
- Fine-grained NVTX annotations for kernel debugging
- Environment variable control (e.g., `MINISGL_DISABLE_OVERLAP_SCHEDULING=1` for ablation studies)

## Comparison with SGLang

| Aspect | SGLang | Mini-SGLang |
|--------|--------|-------------|
| **Codebase Size** | ~300k lines of Python | Only 5k lines of Python |
| **Purpose** | Full-featured production engine | Educational tool + research prototyping |
| **Complexity** | Complex, comprehensive | Lightweight, modular |
| **Target Users** | Production deployment | Learning, research, prototyping |
| **Performance** | High performance | Nearly identical performance |

Both frameworks retain advanced features like Radix Attention, Chunked Prefill, Overlap Scheduling, and Tensor Parallelism, but Mini-SGLang accomplishes this with dramatically simplified code.

## Motivation and Goals

The Mini-SGLang project addresses two main challenges with the original SGLang:

1. **Educational Access**: Making complex LLM serving systems more accessible to newcomers
2. **Research Prototyping**: Providing a framework that is easy to inspect, extend, and optimize for researchers working on new optimizations

## Significance

Mini-SGLang represents a valuable contribution to the AI ecosystem by demonstrating that it's possible to achieve state-of-the-art performance in LLM inference while maintaining code simplicity and readability. This approach bridges the gap between educational tools and production-grade systems, making it ideal for both learning and research applications.

The project successfully distills the power of state-of-the-art inference engines into a compact, understandable codebase while maintaining impressive performance characteristics, embodying the philosophy of having a minimalistic codebase for experimentation and onboarding new contributors.

```metadata
category: computer_science
subcategory: artificial_intelligence
tags: llm_inference, sglang, mini_sglang, machine_learning, python, gpuscaling, radix_cache, tensor_parallelism
```