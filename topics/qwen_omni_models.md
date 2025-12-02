# Qwen-Omni Models

## Overview
Qwen-Omni represents a family of natively omni-modal foundation models developed by Alibaba Cloud. These models are designed to process and understand multiple modalities simultaneously.

## Key Features

### Qwen3-Omni
- **Description**: Qwen3-Omni is the natively end-to-end multilingual omni model
- **Capabilities**: It processes text, images, audio, and video, and delivers real-time streaming
- **Architecture**: Natively omni-modal, allowing for end-to-end processing of multimodal inputs

### General Qwen-Omni Characteristics
- Can accept a combination of text and a single other modality (image, audio, or video) as input
- Generates responses in text or other modalities as appropriate
- Part of Alibaba Cloud's Model Studio

## Integration with vLLM-Omni
The Qwen-Omni models are specifically supported by the vLLM-Omni framework, which provides efficient inference and serving capabilities for omni-modal models. The framework offers:

- High-throughput inference
- Memory-efficient serving
- Support for complex omni-modal workflows
- Distributed inference capabilities

## Model Variants
- Qwen2.5-Omni-3B
- Qwen2.5-Omni-7B
- Qwen3-Omni (various sizes)

## Related Technologies
- [vLLM-Omni](vllm_omni_project.md) <!-- TODO: Broken link --> - Inference and serving framework for omni-modal models
- Alibaba Cloud Model Studio - Platform for accessing Qwen-Omni models

## References
- [Alibaba Cloud Qwen-Omni Documentation](https://www.alibabacloud.com/help/en/model-studio/qwen-omni)
- [Qwen Blog - Qwen3-Omni Announcement](https://qwen.ai/blog?id=65f766fc2dcba7905c1cb69cc4cab90e94126bf4&from=research.latest-advancements-list)