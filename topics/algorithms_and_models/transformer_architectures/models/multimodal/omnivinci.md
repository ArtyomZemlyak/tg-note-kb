# OmniVinci: NVIDIA's Omni-Modal LLM

## Overview
OmniVinci is an open-source, omni-modal Large Language Model (LLM) developed by NVIDIA designed for joint understanding of vision, audio, and language. Released on October 19, 2024, it represents an initiative to build a strong, multi-modal AI system. The main contribution of the paper is not just the numerical results on benchmarks but the detailed explanation of all design decisions related to the model architecture and data collection for training.

## Key Features
1. **Multi-Modal Support**: Handles vision, audio, and text jointly
2. **Three Key Architectural Innovations**:
   - **OmniAlignNet**: Strengthens alignment between vision and audio embeddings in a shared omni-modal latent space
   - **Temporal Embedding Grouping**: Captures relative temporal alignment between vision and audio signals
   - **Constrained Rotary Time Embedding**: Encodes absolute temporal information in omni-modal embeddings
3. **Audio Encoder**: Uses the audio encoder from Audio Flamingo 3 (with Qwen2.5 audio encoder as an alternative)

## Technical Specifications
- **Model Size**: OmniVinci-9B
- **Training Data**: 24M single-modal and omni-modal conversations
- **Training Tokens**: Just 0.2T (6x reduction compared to Qwen2.5-Omni's 1.2T)
- **Architecture**: Built on the Hugging Face Transformers framework
- **Base LLM**: Qwen2.5-7B-Instruct

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

## Key Architectural Innovations

![OmniVinci Architecture Overview](../../../../../media/img_1764253587_aqadxgxrgze28uh_image.jpg) <!-- TODO: Broken image path -->

**Description:** This diagram shows the overall architecture of the OmniVinci model, illustrating how visual, audio, and language modalities are processed and integrated through the OmniAlignNet module, TEG, and CRTE.

### OmniAlignNet
In the process of training the model, each video is split into an audio stream and an image stream; semantically these streams are related, as sound can complement the image (and vice versa). To ensure that audio embeddings and image embeddings are in the same latent space, the model uses the OmniAlignNet module.

The general pipeline of the module works as follows:
1) For audio and visual streams, a sequence of embeddings is obtained
2) These sequences are used as key-value embeddings for cross attention; they are mixed with query embeddings (specific for each stream) and produce two multi-modal embeddings for each video (audio-omni and visual-omni)
3) Multi-modal embeddings are passed through three self-attention layers and L2 normalization
4) For a batch of multi-modal embeddings, maximize cross-modal distance (scalar product) for embeddings corresponding to different samples and minimize in the opposite case (for embeddings corresponding to identical samples) - contrastive loss, similar to that used in CLIP (symmetric cross-entropy from vision to audio and vice versa)

OmniAlignNet effectively models high-level semantic relationships between audio and visual embeddings. Additionally, to model lower-level relationships, the authors propose two types of embedding transformations, the details of which are discussed below.

![Omni-Modal Captions Generation](../../../../../media/img_1764253587_aqadjrbrg6wemel_figure_4_omni_modal_captions_generation.jpg) <!-- TODO: Broken image path -->

**Description:** This figure demonstrates the omni-modal caption generation capabilities of the OmniVinci model, showing how the model effectively combines visual and audio information to produce richer, more contextual captions than single-modality approaches.

### Temporal Embedding Grouping (TEG)
The idea of TEG is that correct ordering of embeddings of different modalities helps the language model better capture local semantic dependencies. The hyperparameter of this method is the temporal window size T_g, which controls the granularity of embedding grouping: embeddings are divided into chunks of size T_g; modalities alternate within chunks.

The authors claim that such granular concatenation of embeddings improves model quality compared to the approach where embeddings are concatenated in large blocks (vision block → audio block → vision block...).

### Constrained Rotary Time Embedding (CRTE)
CRTE is a modification of Rotary Time Embeddings (RoTE, not to be confused with RoPE), a three-stage process consisting of generating basic frequencies, modifying these frequencies, and the rotary part, i.e., rotating embeddings.

At the stage of generating basic frequencies in CRTE, a hyperparameter T_max is proposed to be added - this multiplier is added to the denominator when calculating basic frequencies. The smaller T_max, the more attention is paid to embeddings close to each other (and vice versa): w_i = 2π/(T_max·θ^(i/C)).

At the stage of modifying basic frequencies, CRTE continues the idea of RoTE: for determining rotation angles of embeddings, real distances in seconds are used, unlike discrete positions in RoPE: Ω_{i,j} = ω_i · t_j, where t_j is the real timestamp.

The authors conducted an ablation study and proved that all proposed modifications indeed improve model quality on multi-modal benchmarks.

![Ablation Study Table](../../../../../media/img_1764253587_aqadjhbrg6wemel_table_2_ablation_study_on.jpg) <!-- TODO: Broken image path -->

**Description:** This table shows the ablation study results demonstrating that each of the proposed modifications (OmniAlignNet, Temporal Embedding Grouping, and Constrained Rotary Time Embedding) indeed improves model quality on multi-modal benchmarks.

## Training Methodology

The model training can be divided into two major stages - modality-specific and omni-modal parts respectively, with the LLM-backbone being pre-trained (authors use Qwen2.5-7B-Instruct).

### Vision Module Training
Training of vision modules consists of the following stages:
- **Stage 1**: Vision Projector Alignment - only the vision projector is trained, solving the task of generating simple descriptions
- **Stage 2**: Vision Encoder Alignment - vision encoder and vision projector are trained
- **Stage 3**: Vision Pre-training - core stage, vision encoder is frozen, goal is to fine-tune vision projector and LLM. Multimodal data is used, the model learns to interpret and generate captions for images
- **Stage 4**: Image Instruction Tuning - fine-tuning of the model on vision instruction following tasks: answers to general and knowledge-based questions, generation of complex captions, logical and vision reasoning, document interpretation, diagram processing, etc. All modules are trained
- **Stage 5**: Video Instruction Tuning - final stage, all parts of the model are trained on the task of video understanding (activity recognition; object tracking over time (by frames), time-sensitive QA). Goal - to obtain temporal reasoning capability from the model

After the vision stage, the authors obtain a "vision preliminary checkpoint" - vision encoder, projector and LLM that are well trained on vision tasks.

### Audio Module Training
Training of audio modules is divided into two stages:
- **Stage 1**: Audio Projector & Encoder Alignment. LLM and vision part parameters are frozen, learning is done on audio-based QA, captioning, ASR tasks. Goal - to train audio representation projectors consistent with the semantic space of the language model
- **Stage 2**: Audio Instruction Tuning: LLM parameters are not frozen, the LLM learns together with the audio encoder and audio projector. Learning is done on all the same tasks + speech translation task; the idea of the stage is that diverse audio tasks with a trained projector will help the audio encoder learn both low-level acoustic features and high-level semantic representations.

### Omni-Modal Joint Training
During the multi-modal training stage, vision and audio encoders are frozen, all other modules are trained (OmniAlignNet, projectors and LLM). The paper describes two approaches: implicit and explicit learning.

![Implicit vs Explicit Learning in Omni-Modal Training](../../../../../media/img_1764253587_aqadxqxrgze28uh_image.jpg) <!-- TODO: Broken image path -->

**Description:** This illustration compares the implicit and explicit learning approaches used in OmniVinci's multi-modal training, highlighting how explicit learning with synthetic data effectively solves the problem of modality-specific hallucination.

- **Implicit learning** uses existing Video QA datasets, where the model implicitly learns to integrate both modalities without receiving unambiguous information about which part of the answer is taken from the video sequence and which from the sound.

- **Explicit learning** uses synthetic data, where the relationship between modalities is indicated. The main development of the authors is a data engine that generates separate descriptions for video and audio, and then uses an LLM with reasoning (Deepseek R1) to create combined captions indicating how visual and audio information complement each other. The problem this approach solves is eliminating "modality-specific hallucination". The key finding of the multi-modal stage: video description based on a single modality is often inaccurate; integration of both modalities is critical, and explicit learning effectively solves this problem.

![Modality-Specific Hallucination Problem](../../../../../media/img_1764253587_aqadxwxrgze28uh_mn_mn.jpg) <!-- TODO: Broken image path -->

**Description:** This figure illustrates the problem of modality-specific hallucination that OmniVinci addresses through its explicit learning approach, showing how integration of both visual and audio modalities is critical for accurate understanding.

The final training stage includes RL using GRPO. An important result: GRPO on audio-visual data converges faster and of higher quality than on purely visual data, which confirms the value of the multi-modal approach.

![Accuracy and Reward in Training](../../../../../media/img_1764253587_aqadjxbrg6wemel_figure_6_left_accuracy_reward.jpg) <!-- TODO: Broken image path -->

**Description:** This figure shows the training performance comparison, demonstrating that GRPO on audio-visual data converges faster and achieves higher quality than on purely visual data, confirming the value of the multi-modal approach.

## Сравнение с другими моделями
- [[qwen3-omni.md|Qwen3-Omni]] - Альтернативная мультимодальная модель от Alibaba Cloud, конкурирующая с OmniVinci в области мультимодального понимания
- [[ming_flash_omni_preview.md]] - Альтернативная omni-модель от Inclusion AI с архитектурой Sparse MoE, фокусирующаяся на более точном контроле при генерации и редактировании изображений, а также на распознавании речи с учетом диалектов

## Research Paper
- Research Paper: [https://arxiv.org/abs/2510.15870](https://arxiv.org/abs/2510.15870)

## Availability
- GitHub Repository: [https://github.com/NVlabs/OmniVinci](https://github.com/NVlabs/OmniVinci)
- Hugging Face Model: [https://huggingface.co/nvidia/omnivinci](https://huggingface.co/nvidia/omnivinci)
- Website: [https://nvlabs.github.io/OmniVinci](https://nvlabs.github.io/OmniVinci)

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

## Связи с другими темами
- [[ibm_granite_docling_258m.md]] - Альтернативная мультимодельная модель от IBM, специализирующаяся на обработке документов, в отличие от OmniVinci, которая фокусируется на визуальных, аудио и текстовых модальностях
- [[../../../ai/computer_vision/multimodal_models.md]] - Общие понятия о мультимодальных моделях, включая CLIP, на котором основан подход contrastive loss в OmniAlignNet
- [[transformer_architecture.md]] - Архитектура трансформеров, на которой основаны современные мультимодальные модели
- [[../../../ai/nlp/transformers/rope_rotary_embeddings.md]] - Ротационные позиционные эмбеддинги, на которых основывается CRTE

## Significance
In the OmniVinci paper, a comprehensive approach to creating multi-modal language models is presented, including architectural innovations and a well-thought-out training strategy with separation into modality-specific and omni-modal stages. The key contribution is the systematic study of multi-modal learning approaches. The authors demonstrate that explicit learning with synthetic data effectively solves the problem of modality-specific hallucination and improves overall model quality.

## Источники

1. [OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM - Part 1/2](https://speechinfo.ru/articles/omnivinci-enhancing-architecture-and-data-for-omni-modal-understanding-llm-1-2) - Статья о ключевых архитектурных новшествах OmniVinci, включая OmniAlignNet, TEG и CRTE
2. [OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM - Part 2/2](https://speechinfo.ru/articles/omnivinci-enhancing-architecture-and-data-for-omni-modal-understanding-llm-2-2) - Статья о процессе обучения модели и различии между implicit и explicit learning
3. [Original Research Paper: OmniVinci: Enhancing Architecture and Data for Omni-Modal Understanding LLM](https://arxiv.org/abs/2510.15870) - Оригинальная научная статья от команды NVIDIA о модели OmniVinci