# vLLM-Omni Project

## Overview
vLLM-Omni is a framework that extends the original vLLM (designed for text-based autoregressive generation) to support omni-modality model inference and serving. It's positioned as "EASY, FAST, AND CHEAP OMNI-MODALITY MODEL SERVING FOR EVERYONE".

## Key Features

### Core Capabilities
- **Omni-modality support**: Processes text, image, video, and audio data
- **Non-autoregressive architectures**: Extends vLLM's AR support to Diffusion Transformers (DiT) and other parallel generation models
- **Heterogeneous outputs**: Supports outputs beyond traditional text generation to multimodal outputs

### Performance Features
- State-of-the-art AR support leveraging efficient KV cache management from vLLM
- Pipelined stage execution overlapping for high throughput performance
- Fully disaggregated architecture based on OmniConnector with dynamic resource allocation across stages

### Flexibility & Usability
- Heterogeneous pipeline abstraction for managing complex model workflows
- Seamless integration with popular Hugging Face models
- Support for tensor, pipeline, data and expert parallelism for distributed inference
- Streaming outputs
- OpenAI-compatible API server
- Support for both GPU and NPU hardware

## Supported Models

### Currently Supported Models Include:
- **Omni-modality models**: 
  - Qwen2.5-Omni
  - Qwen3-Omni
- **Multi-modality generation models**: 
  - Qwen-Image

The framework is designed to seamlessly support most popular open-source models on HuggingFace. The documentation specifically mentions offline and online inference examples for Qwen2.5-Omni, Qwen3-Omni, and Qwen-Image models.

## Architecture Highlights
- Multi-stage pipeline execution
- Support for different model types (AR, Diffusion, Generation)
- Distributed inference capabilities
- Modular architecture with separate components for different modalities

The project appears to be actively maintained with recent updates and comprehensive documentation covering user guides, developer guides, API references, and CLI references.

## GitHub Repository
- [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)

## Documentation
- [vLLM-Omni Documentation](https://docs.vllm.ai/projects/vllm-omni/en/latest/)

## Related Pull Request
A significant addition to the main vLLM project is PR #29757, which adds Mistral Large 3 support to vLLM.