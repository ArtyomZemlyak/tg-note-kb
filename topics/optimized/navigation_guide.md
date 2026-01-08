# Knowledge Base Structure Migration Guide

## Overview

This guide explains the migration from the legacy structure to the optimized ML/DS/AI knowledge base structure. It identifies where content previously located in the old structure can now be found in the new organization.

## Legacy Structure vs. Optimized Structure

### 1. Legacy: `/ai/` → New: Multiple optimized locations

**Old Location**: `/topics/ai/`
**New Locations**: 
- Frameworks: `/topics/optimized/frameworks/` (for framework-specific AI content)
- Theory/Foundations: `/topics/optimized/theory_foundations/` (for foundational AI concepts)
- Applications: `/topics/optimized/applications/` (for AI applications in domains)
- Tasks: `/topics/optimized/tasks/` (for AI problem-solving approaches)

**Migration Notes**:
- AI applications like NLP and Computer Vision moved to `/topics/optimized/tasks/nlp/` and `/topics/optimized/tasks/cv/`
- Framework-specific AI content (PyTorch, TensorFlow) moved to `/topics/optimized/frameworks/`
- Foundational AI concepts moved to `/topics/optimized/theory_foundations/`

### 2. Legacy: `/algorithms/` → New: `/topics/optimized/algorithms/`

**Old Location**: `/topics/algorithms/`
**New Location**: `/topics/optimized/algorithms/`

**Migration Notes**:
- Preserved structure with better organization:
  - Classical ML: `/topics/optimized/algorithms/classical_ml/`
  - Neural Networks: `/topics/optimized/algorithms/neural_networks/`
  - Specialized Algorithms: `/topics/optimized/algorithms/specialized_algorithms/`

### 3. Legacy: `/frameworks_and_libraries/` → New: `/topics/optimized/frameworks/`

**Old Location**: `/topics/frameworks_and_libraries/`
**New Location**: `/topics/optimized/frameworks/`

**Migration Notes**:
- Moved to shorter, cleaner path: `/topics/optimized/frameworks/`
- Preserved all framework-specific content:
  - PyTorch: `/topics/optimized/frameworks/pytorch/`
  - TensorFlow: `/topics/optimized/frameworks/tensorflow/`
  - scikit-learn: `/topics/optimized/frameworks/scikit-learn/`
  - Etc.

### 4. Legacy: `/applications/` → New: `/topics/optimized/applications/`

**Old Location**: `/topics/applications/`
**New Location**: `/topics/optimized/applications/`

**Migration Notes**:
- Reorganized by industry/domain rather than technology:
  - Healthcare: `/topics/optimized/applications/healthcare/`
  - Finance: `/topics/optimized/applications/finance/`
  - Retail: `/topics/optimized/applications/retail/`
  - Etc.

### 5. Legacy: Various locations → New: `/topics/optimized/tasks/`

**Old Location**: Scattered across AI, applications, etc.
**New Location**: `/topics/optimized/tasks/`

**Migration Notes**:
- Consolidated task-oriented content here:
  - NLP tasks: `/topics/optimized/tasks/nlp/`
  - Computer Vision tasks: `/topics/optimized/tasks/cv/`
  - Classification tasks: `/topics/optimized/tasks/classification/`
  - Recommendation Systems: `/topics/optimized/tasks/recommendation_systems/`
- This eliminates duplication between AI applications and task descriptions

### 6. Legacy: `/tools/`, `/tools_and_platforms/` → New: `/topics/optimized/tools_platforms/`

**Old Location**: `/topics/tools/` and `/topics/tools_and_platforms/`
**New Location**: `/topics/optimized/tools_platforms/`

**Migration Notes**:
- Consolidated tool and platform content to eliminate overlap:
  - MLOps: `/topics/optimized/tools_platforms/mlops/`
  - Cloud Platforms: `/topics/optimized/tools_platforms/cloud_platforms/`
  - Development Tools: `/topics/optimized/tools_platforms/development_tools/`

## Navigation Tips

### For Framework-Specific Questions
Go to `/topics/optimized/frameworks/[framework_name]/` for documentation about specific tools like PyTorch, TensorFlow, or scikit-learn.

### For Algorithm-Specific Questions
Go to `/topics/optimized/algorithms/[algorithm_category]/` for information about different algorithm types.

### For Problem-Solving Questions
Go to `/topics/optimized/tasks/[task_name]/` for guidance on solving specific ML/DS problems like classification, NLP, or computer vision.

### For Application-Driven Questions
Go to `/topics/optimized/applications/[domain_name]/` for industry-specific use cases and implementations.

### For Infrastructure Questions
Go to `/topics/optimized/tools_platforms/[tool_category]/` for information about MLOps, deployment, and operational tools.

## Eliminating Duplicates

The new structure eliminates these common duplication points:

1. **NLP Content**: Previously scattered across AI, applications, and frameworks sections → Now consolidated in `/topics/optimized/tasks/nlp/` with cross-references to relevant frameworks

2. **Computer Vision Content**: Previously duplicated between AI and applications sections → Now in `/topics/optimized/tasks/cv/` with clear connections to frameworks and applications

3. **Framework Overviews**: Previously both in general frameworks section and AI applications → Now unified in `/topics/optimized/frameworks/` with specific use-cases referenced from task sections

4. **Practical Solutions**: Previously in multiple locations → Now consolidated in `/topics/optimized/tasks/practical_solutions/`

## Quick Reference Map

| Old Path Fragment | New Path Fragment | Purpose |
|------------------|-------------------|---------|
| `/ai/nlp/` | `/tasks/nlp/` | NLP tasks and techniques |
| `/ai/computer_vision/` | `/tasks/cv/` | Computer vision tasks |
| `/applications/nlp/` | `/tasks/nlp/` | See above |
| `/applications/computer_vision/` | `/tasks/cv/` | See above |
| `/ai/models/` | `/algorithms/neural_networks/` | Model architectures |
| `/tools/deployment/` | `/tools_platforms/mlops/` | Deployment and operations |
| `/practical_solutions/` | `/tasks/practical_solutions/` | Implementation guides |

## Maintaining the New Structure

To avoid future duplication:
1. Place content in the most specific applicable category
2. Use cross-references between related topics rather than duplicating content
3. Add new content to the optimized structure rather than creating new legacy-style sections
4. When updating existing content, move it to the appropriate optimized category

This structure ensures clear navigation and eliminates the redundancy that existed in the legacy organization.