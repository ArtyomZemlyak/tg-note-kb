# OmniVinci: NVIDIA's Omni-Modal LLM

## Overview
OmniVinci is an open-source, omni-modal Large Language Model (LLM) developed by NVIDIA designed for joint understanding of vision, audio, and language. Released on October 19, 2024, it represents an initiative to build a strong, multi-modal AI system.

## Key Features
1. **Multi-Modal Support**: Handles vision, audio, and text jointly
2. **Three Key Architectural Innovations**:
   - **OmniAlignNet**: Strengthens alignment between vision and audio embeddings in a shared omni-modal latent space
   - **Temporal Embedding Grouping**: Captures relative temporal alignment between vision and audio signals
   - **Constrained Rotary Time Embedding**: Encodes absolute temporal information in omni-modal embeddings

## Technical Specifications
- **Model Size**: OmniVinci-9B
- **Training Data**: 24M single-modal and omni-modal conversations
- **Training Tokens**: Just 0.2T (6x reduction compared to Qwen2.5-Omni's 1.2T)
- **Architecture**: Built on the Hugging Face Transformers framework

## Performance
OmniVinci outperforms Qwen2.5-Omni with:
- +19.05 on DailyOmni (cross-modal understanding)
- +1.7 on MMAR (audio)
- +3.9 on Video-MME (vision)

Despite using significantly fewer training tokens (6x less), it achieves superior performance across modalities, demonstrating efficiency in cross-modal understanding.

## Applications
The model demonstrates omni-modal advantages in downstream applications spanning:
- Robotics
- Medical AI
- Smart Factory

## Architecture and Methodology
OmniVinci introduces a curation and synthesis pipeline that generates 24M single-modal and omni-modal conversations. The model leverages the insight that modalities reinforce one another in both perception and reasoning.

## Availability
- GitHub Repository: [https://github.com/NVlabs/OmniVinci](https://github.com/NVlabs/OmniVinci)
- Hugging Face Model: [https://huggingface.co/nvidia/omnivinci](https://huggingface.co/nvidia/omnivinci)
- Website: [https://nvlabs.github.io/OmniVinci](https://nvlabs.github.io/OmniVinci)
- Research Paper: [https://arxiv.org/abs/2510.15870](https://arxiv.org/abs/2510.15870)

## Key Innovations
1. **OmniAlignNet**: Strengthens alignment between vision and audio embeddings in a shared omni-modal latent space
2. **Temporal Embedding Grouping**: Captures relative temporal alignment between vision and audio signals
3. **Constrained Rotary Time Embedding**: Encodes absolute temporal information in omni-modal embeddings

## Citation
```
@article{omnivinci2025,
      title={OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM},
      author={Hanrong Ye, Chao-Han Huck Yang, Arushi Goel, Wei Huang, Ligeng Zhu, Yuanhang Su, Sean Lin, An-Chieh Cheng, Zhen Wan, Jinchuan Tian, Yuming Lou, Dong Yang, Zhijian Liu, Yukang Chen, Ambrish Dantrey, Ehsan Jahangiri, Sreyan Ghosh, Daguang Xu, Ehsan Hosseini-Asl, Danial Mohseni Taheri, Vidya Murali, Sifei Liu, Jason Lu, Oluwatobi Olabiyi, Frank Wang, Rafael Valle, Bryan Catanzaro, Andrew Tao, Song Han, Jan Kautz, Hongxu Yin, Pavlo Molchanov},
      journal={arXiv},
      year={2025},
}
```

## Significance
OmniVinci represents NVIDIA's commitment to advancing machine intelligence by developing the ability to perceive across multiple modalities, much as humans sense the world. The model demonstrates that with careful architectural choices and data curation, it's possible to achieve superior multi-modal performance with significantly reduced computational requirements.