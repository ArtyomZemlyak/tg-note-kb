# Physics of Language Models: Part 3.2, Knowledge Manipulation

## Authors
- Zeyuan Allen-Zhu (Meta AI / FAIR Labs)
- Yuanzhi Li (Mohamed bin Zayed University of AI)

## Publication
- arXiv:2309.14402
- September 18, 2023 (version 2)
- https://physics.allen-zhu.com/part-3-knowledge/part-3-2
- Extended video: https://youtu.be/YSHzKmEianc

## Overview

This paper investigates the ability of language models to manipulate stored knowledge during inference time. While language models excel at knowledge retrieval, they struggle with simple knowledge manipulation tasks such as classification, comparison, and inverse search, even when the knowledge is perfectly stored in the model. The study demonstrates that language models require Chain of Thoughts (CoT) during both training and inference to perform basic knowledge manipulation tasks effectively.

## Key Research Questions

1. Can language models manipulate knowledge they have memorized during pretraining to solve different tasks at inference time?
2. Can models determine if Princeton is ranked higher than MIT based on their stored 2023 US News university ranking knowledge?
3. Can models answer questions like "Was Joe Biden born in an odd year?" or "Was Donald Trump born earlier than Nancy Pelosi?" based on memorized celebrity birthdays?
4. What are the fundamental limitations of knowledge manipulation in transformer-based language models?

## Methodology

The researchers used the same synthetic biography (BIO) dataset as in Part 3.1, consisting of N=100,000 individuals with six attributes (birth date, birth city, university, major, company name, company city). They conducted controlled experiments focusing on four types of knowledge manipulation tasks:

- **Knowledge Retrieval**: Extending previous work on knowledge extraction
- **Knowledge Classification**: Classifying attributes (e.g., "Was Anya born in an even month?")
- **Knowledge Comparison**: Comparing attributes between individuals (e.g., "Is Anya's university better than Sabrina's?")
- **Knowledge Inverse Search**: Identifying a person based on their attributes (e.g., "Who was born on October 2, 1996 in Princeton...")

The study used models pretrained on augmented biography data (bioS multi5+permute) that achieved near-perfect knowledge extraction accuracy to isolate manipulation difficulties from extraction difficulties.

## Main Results

### Result 1: Dual Knowledge Retrieval Challenges
- Dual retrieval is generally easy when both tasks are simple
- However, if there's a causal and spatial relationship between pieces of knowledge, their order may matter
- With properly augmented data (bioS multi5+permute), dual knowledge retrieval accuracy is nearly perfect
- With spatially dependent data (bioS multi5+fullname), answering company city first drastically reduces accuracy compared to answering company name first

### Result 2: Partial Knowledge Retrieval Challenges
- Even if an attribute (e.g., October 2, 1996) can be perfectly extracted, partially retrieving only its later tokens (e.g., the year 1996) may still be poor
- Models may fail to answer "What is the birth year of person Anya?" despite correctly answering "What is the birth date of person Anya?"
- This suggests models require Chain of Thought (CoT) reasoning to manipulate knowledge

### Result 3: Knowledge Classification Difficulties
- Without CoT examples, models' test accuracy is significantly low even for simple, single-step manipulation tasks
- Determining whether a month is even or odd requires 10,000 training samples to achieve 75% accuracy, despite theoretical sample complexity of O(12)
- Ranking months requires 50,000 training samples to reach 85% test accuracy with theoretical complexity of O(12²)
- Ranking 100 majors barely outperforms random even with 2.5 million training samples

### Result 4: CoT Dependency Issue
- Even when CoT examples are included during training, models struggle to answer without hints during testing
- This indicates that including hints during training does not improve test-time accuracy when hints are removed
- When models use hints during testing, accuracy significantly improves

### Result 5: Extraction vs Manipulation
- The difference between a BIO pretrained and QA finetuned model is minimal for downstream knowledge manipulation tasks
- Fine-tuning a model first to answer questions like "What major did Anya Briar Forger study" doesn't improve its performance on ranking/classification tasks based on that major

### Result 6: Generalization to Real Models
- Real-life GPT-4 also struggles with knowledge classification and comparison in the absence of CoTs
- GPT-4 has 71.1% accuracy comparing birth dates for celebrities from 1900-1950, but drops to 52.3% for 1900-1910 (almost random guess)
- Scaling up model size does not mitigate these issues

### Result 7: Knowledge Inverse Search Impossibility
- Models have near-zero accuracy for inverse knowledge search in P_test, even for the simplest task
- This holds even with BIO+QA mixed training approach and strong pretrain data knowledge augmentation
- Only when knowledge order is truly reversed in pretrain data (person name after attributes), test accuracies improve
- This demonstrates fundamental limitations due to left-to-right autoregressive training design

### Result 8: Inverse Search in Practice
- GPT-3.5/4 also exhibit huge difficulties with inverse knowledge search
- While GPT-4 can predict the next sentence in Jane Austen's works with 65.9% accuracy, it only has 0.8% accuracy predicting the preceding sentence

### Result 9: CoT for Inverse Search
- To improve inverse search of critical documents by LLMs, possible solutions include:
  - Retrieval Augmented Generation (RAG)
  - Preprocessing training data to include reverse knowledge
  - Introducing line numbers in documents

## Key Findings

### Chain of Thought (CoT) Dependency
Language models cannot efficiently manipulate knowledge from pre-training data during inference without explicit Chain of Thought reasoning. This is different from math reasoning where models can skip computation steps - for knowledge manipulation, models must explicitly state intermediate facts before making deductions.

### Fundamental Architectural Limitations
The autoregressive left-to-right training design prevents models from understanding bidirectional relationships. If a model learns "A equals B," it cannot infer "B equals A" unless it's also in the training data.

### Inverse Search Impossibility
Language models fundamentally cannot perform inverse knowledge search, indicating they cannot be used as databases. This is due to their autoregressive nature - bidirectional models like BERT also suffer even more severe issues in forward knowledge extraction.

### Scaling Inadequacy
Simply increasing model size, data size, or training samples does not solve these fundamental knowledge manipulation limitations, suggesting novel architectural or training approaches are needed.

## Practical Implications

1. **Training Data Enhancement**: Include Chain of Thought examples in training data to improve knowledge manipulation
2. **RAG Implementation**: Use Retrieval Augmented Generation to handle knowledge-intensive tasks
3. **Reversal Training**: Incorporate reverse knowledge patterns in pre-training data
4. **Multi-token Prediction**: Explore techniques that help with partial retrieval tasks
5. **Document Structuring**: Include line numbers or other identifiers for inverse search tasks

## Research Series Context

This is part 3.2 in the "Physics of Language Models" series, with:
- Part 1: Learning Hierarchical Language Structures
- Part 2: Grade-School Math and Reasoning Processes
- Part 3.1: Knowledge Storage and Extraction
- Part 3.3: Knowledge Capacity Scaling Laws

## Connections to Humans and AI

The findings suggest a Turing test to distinguish humans from modern generative language models: humans can perform simple knowledge manipulation tasks mentally, while language models require explicitly writing down the CoTs. Despite the challenge of inverse search for humans, the researchers identified tasks easily solvable by humans but not by GPT-4.

## References

- arXiv:2309.14402: Physics of Language Models: Part 3.2, Knowledge Manipulation
- arXiv:2309.14316: Physics of Language Models: Part 3.1, Knowledge Storage and Extraction
- arXiv:2404.05405: Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws
- arXiv:2305.13673: Physics of Language Models: Part 1, Learning Hierarchical Language Structures
- arXiv:2407.20311: Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process
- arXiv:2408.16293: Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems

## See Also

- [[physics_of_language_models_knowledge_storage_extraction.md]] - Part 3.1 covering knowledge storage and extraction
- [[physics_of_language_models_part1.md]] - Part 1 on learning hierarchical language structures
- [[attention_sinks_in_transformer_models.md]] - Related research on information flow in transformer models
- [[logical_reasoning_in_llms.md]] - Other approaches to logical reasoning in large language models
- [[coconut_chain_of_continuous_thought.md]] - Continuous Chain of Thought approaches

```metadata
category: machine_learning
subcategory: language_model_reasoning
tags: knowledge_manipulation, chain_of_thought, transformer_architecture, language_model_reasoning, knowledge_extraction
```