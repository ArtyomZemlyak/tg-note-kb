# Clinical Reasoning Failures in Large Language Models: SAE Insights

## Overview
Analysis of why Large Language Models show high performance on medical benchmarks but fail in real-world clinical scenarios, based on insights from explainable deep learning using Sparse Autoencoders (SAEs).

## Problem Statement
- High quality shown by open models on medical benchmarks
- Significant failures observed in real-world clinical applications

## Research Methodology
Authors investigated the cause of these failures on 3 synthetic oncology-related tasks: D1, D2, D3. For each task, multiple input perturbations were considered, where perturbation refers to term removal - each D' = Di\{i}. The stability and accuracy were analyzed in three solution modes:

1. **Chain-of-Thought (COT)** - reasoning chain approach
2. **Direct Queries** - two types of direct problem-solving requests:
   - Generation of Assessment & Plan structure - clinical conclusion and patient management plan
   - Simple direct questions, e.g., "What cancer stage?"

This experimental setup covered reasoning over problems, structured problem format, and free-form writing.

## Key Findings
### Accuracy Variability
For the same clinical case, OpenBioLLM showed 45.9% or 99.1% accuracy solely depending on whether the question was embedded in A&P or asked directly (with A&P showing lower accuracy). Similar effects were observed in MedGemma (74.8% vs 98.2%). GPT-5 performance remained consistent regardless of question format.

### Architectural Insights from SAE Analysis
- **MedGemma**: Shows bias toward storing multiple significant features in one SAE region, while contextual meaning is localized in other areas
- **OpenBioLLM**: Information encoding is more uniform without clear separation

## Significance of SAE Application
- The comparison of architectural ways of encoding information using SAEs is rarely explored
- This represents one of the first works applying SAEs to compare information encoding architectures in clinical reasoning contexts
- Training SAEs is time-consuming and resource-intensive, which limits widespread adoption
- Found architectural results should be interpreted as artifacts rather than definitive insights
- Correct and optimal SAE training for specific domains remains an open research question
- SAEs serve as indicators of architectural differences, though sensitivity to model retraining needs validation

## Implications
- Clinical research investigations using LLMs are complex, time-intensive, and challenging
- Alternative approaches might be more cost-effective, such as using high-performing models like GPT or implementing robust guardrails

## References
- "Why Large Language Models' Clinical Reasoning Fails: Insights from Explainable Deep Learning"