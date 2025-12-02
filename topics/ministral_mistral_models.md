# Ministral and Mistral Large 3 Models

## Overview
This document covers the latest developments in Mistral AI's model lineup, including the new Ministral models and the Mistral Large 3 model.

## Ministral Models

### Ministral3
- **Architecture**: Based on the Mistral architecture but with significant enough differences to warrant its own architecture type in llama.cpp
- **Variants**: Available in 3B, 8B, and 14B parameter sizes
- **Implementation**: The PR in llama.cpp adds support for Ministral3 models with a separate `MISTRAL3` architecture in GGUF format rather than reusing the Llama architecture
- **Status**: Released in December 2025, with actual model weights released after the code implementation

### Technical Implementation in llama.cpp
- Added new `Mistral3Model` class extending `LlamaModel`
- Registered `"Mistral3ForConditionalGeneration"` model type
- Added proper architecture handling in the GGUF conversion script
- Includes temporary compatibility code for conversion of older models

## Mistral Large 3

### PR #29757 in vLLM
- **Title**: ADD MISTRAL LARGE 3
- **Author**: juliendenize
- **Status**: Open at the time of documentation
- **Purpose**: Adds support for Mistral-Large-3 and its Eagle variant by reusing the DeepseekV2 architecture

### Key Changes in PR #29757
1. Adds new model files for Mistral Large 3
2. Updates model registry and configuration
3. Includes quantization support for fp8_e4m3 format
4. Adapts configuration for the new model

### Review Feedback
- Potential crash in speculative config due to assumptions about architectures list
- Potential regression in RoPE parameters
- Quantization regression - only supports fp8_e4m3 now, breaking compressed-tensors quantization

## Performance Data
- PPL results for the Ministral3 14B model (-Instruct variant, f16, ctx=32000, batch=8192): Final estimate: PPL = 5.5389 +/- 0.03163

## Related Links
- [llama.cpp PR #17644](https://github.com/ggml-org/llama.cpp/pull/17644) - Adds Ministral3 support
- [vLLM PR #29757](https://github.com/vllm-project/vllm/pull/29757) - Adds Mistral Large 3 support
- [Mistral AI](https://www.mistral.ai/)