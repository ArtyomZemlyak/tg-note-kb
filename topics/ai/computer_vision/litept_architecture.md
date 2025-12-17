# LitePT: Lighter Yet Stronger Point Transformer

## Overview
LitePT is a lightweight, high-performance 3D point cloud architecture that significantly outperforms the state-of-the-art Point Transformer V3 (PTv3) in terms of efficiency while maintaining or exceeding performance. It has 3.6× fewer parameters, runs 2× faster, and uses 2× less memory than PTv3.

## Architecture Design Principle
The core design principle of LitePT is based on the observation that different computational blocks serve different purposes in the feature hierarchy:

- **Early stages (high-resolution)**: Convolution is adequate to extract low-level geometry where attention is expensive without benefits
- **Late stages (low-resolution)**: Attention captures high-level semantics and context more efficiently

This insight leads to a hybrid architecture that employs:
- Convolution blocks in early stages for local geometry processing
- PointROPE-enhanced attention blocks in later stages for semantic understanding

## Key Components

### Tailored Blocks for Different Stages
- **Early stages (i ≤ Lc)**: Operate on point sets with high spatial resolution and density; use convolution layers to efficiently aggregate information over local receptive fields
- **Deep stages (i > Lc)**: Operate on few, high-dimensional tokens; switch to attention-based blocks for long-range context and semantic concepts

### Point Rotary Positional Embedding (PointROPE)
- Parameter-free 3D positional encoding that replaces convolutional positional encoding
- Adapts Rotary Positional Embedding (RoPE) to 3D point clouds by dividing the embedding dimension into three equal subspaces corresponding to x, y, and z axes
- Uses standard 1D RoPE embedding independently for each axis

## Variants
- **LitePT-S**: Smallest variant with 12.7M parameters; C = (36, 72, 144, 252, 504), B = (2, 2, 2, 6, 2)
- **LitePT-B**: Medium variant with 45.1M parameters; C = (54, 108, 216, 432, 576), B = (3, 3, 3, 12, 3)  
- **LitePT-L**: Large variant with 85.9M parameters; C = (72, 144, 288, 576, 864), B = (3, 3, 3, 12, 3)

## Performance
LitePT outperforms Point Transformer V3 on multiple benchmarks while being significantly more efficient:

| Method | #Params | Training Latency | Training Memory | Inference Latency | Inference Memory |
|--------|---------|------------------|-----------------|-------------------|------------------|
| PTv3 | 46.1M | 110ms | 5.8G | 51ms | 4.1G |
| LitePT-S | 12.7M | 72ms | 2.3G | 21ms | 2.0G |

### Benchmark Results
- **ScanNet semantic segmentation**: 76.5 mIoU
- **Structured3D semantic segmentation**: 83.6 mIoU
- **NuScenes semantic segmentation**: 82.2 mIoU
- **Waymo semantic segmentation**: 73.1 mIoU
- **ScanNet instance segmentation**: 64.9 mAP50

## Advantages
1. **Parameter Efficiency**: 3.6× fewer parameters than PTv3
2. **Computational Efficiency**: 2× faster runtime
3. **Memory Efficiency**: 2× lower memory footprint
4. **Performance**: Matches or outperforms PTv3 across benchmarks
5. **Scalability**: Can be scaled up while maintaining efficiency benefits

## Applications
LitePT is suitable for various 3D point cloud processing tasks:
- 3D semantic segmentation
- 3D instance segmentation
- 3D object detection
- Robotics and autonomous driving
- Environmental monitoring
- 3D scene understanding

## Implementation Details
The architecture follows a U-Net structure with five stages. Per default, stages 1, 2, 3 use ConvBlocks, while stages 4, 5 use AttnBlocks. Each ConvBlock consists of a sparse convolution layer, a linear layer, and LayerNorm with residual connection. Each AttnBlock consists of PointROPE embedding followed by attention computed locally within groups of points.

## Training Settings and Experimental Details

### Semantic Segmentation Training Settings
- **NuScenes & Waymo**: 
  - Input features: XYZ+Intensity
  - Grid size: 0.05m
  - Loss: CrossEntropy+Lovasz
  - Optimizer: AdamW
  - Weight decay: 0.005
  - Scheduler: OneCycleLR
  - Learning rate: 0.002 (NuScenes), 0.006 (Waymo)
  - Batch size: 12
  - Epochs: 50 (NuScenes), 1200 (Waymo)
  - GPUs: 4

- **ScanNet & Structured3D**:
  - Input features: RGB+Normal
  - Grid size: 0.02m
  - Loss: CrossEntropy+Lovasz
  - Optimizer: AdamW
  - Weight decay: 0.05
  - Scheduler: OneCycleLR
  - Learning rate: 0.012
  - Batch size: 48
  - Epochs: 200
  - GPUs: 16

### Instance Segmentation Training Settings
- **ScanNet & ScanNet200**:
  - Input features: RGB+Normal
  - Head: PointGroup framework
  - Optimizer: AdamW
  - Weight decay: 0.05
  - Scheduler: OneCycleLR
  - Learning rate: 0.006
  - Batch size: 12
  - Epochs: 800
  - GPUs: 4

### Object Detection Training Settings
- **Waymo**:
  - Input features: XYZ+Intensity+Elongation
  - Grid size: (0.32m, 0.32m, 6.0m)
  - Head: CenterPoint-Pillar framework
  - Optimizer: Adam
  - Weight decay: 0.01
  - Scheduler: OneCycleLR
  - Learning rate: 0.006
  - Batch size: 64
  - Epochs: 40
  - GPUs: 16

### Ablation Study Results
- PointROPE ablation: Removing PointROPE causes a performance drop of 2.6 percentage points in mIoU on NuScenes
- PointROPE works similarly well with base frequencies in the range of 10-1000, with b=100 yielding the best score
- Equal weighting of x:y:z axes (6:6:6) in PointROPE performs better than uneven splits

### Performance without TTA and Chunking
- PTv3 without chunking and TTA: 78.3 mIoU, 86.0 mAcc on NuScenes
- LitePT-S without chunking and TTA: 80.4 mIoU, 86.9 mAcc on NuScenes
- This indicates that LitePT maintains its efficiency advantages even in simpler evaluation settings

## Source
Based on the paper "LitePT: Lighter Yet Stronger Point Transformer" by Yuanwen Yue, Damien Robert, Jianyuan Wang, Sunghwan Hong, Jan Dirk Wegner, Christian Rupprecht, and Konrad Schindler from ETH Zurich, University of Oxford, and University of Zurich.

## Links
- [[point_rotary_positional_embedding.md]] - The novel positional encoding used in LitePT
- [[point_transformer_v3.md]] - The state-of-the-art architecture that LitePT improves upon
- [[../../llm/attention/specialized_attention_mechanisms.md]] - Related attention mechanisms
- [[../../llm/architectures/hybrid_architectures.md]] - Hybrid architectures approach
- [[../../llm/architectures/hybrid_efficient_llm_architectures.md]] - Efficiency-focused hybrid approaches

## Sources
- Original paper: "LitePT: Lighter Yet Stronger Point Transformer" (2512.13689v1.pdf)
- Code and models: https://github.com/prs-eth/LitePT

## Media References
- Original document PDF: [[../../media/doc_1765946152_agaddyqaalqxeeo.pdf]]