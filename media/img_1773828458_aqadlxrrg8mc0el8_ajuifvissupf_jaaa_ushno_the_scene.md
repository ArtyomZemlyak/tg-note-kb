# Image Description

**File:** img_1773828458_aqadlxrrg8mc0el8_ajuifvissupf_jaaa_ushno_the_scene.jpg
**Original:** image.jpg
**Received:** 1773828458

## Extracted Text (OCR)

AJUIFVISSUPF) |JaAa]-USHNo]

## [а] The Scene: Computational Cognitive Dissonance (5) Macroscopic Diagnosis: Geometric Anomaly

107+

107?

User: 5 there a motorcycle in the image? Perceptual Instability (Hew)

VLM Evidence: п the image, tnere 15 a motorcycle parkea next to a bus. he motorcycle is not in motion, and itis stationary... Conclusion: Глегетоге, the final answer 15 No.

ic) Stage 1 Diagnosis: Perceptual Failure {ар Stage 2 Diagnosis: Logicai-Causal Failure

НПА АТО:

Nomina: Threshold "parked"

(aj2o5 DOWWAS) АЗЫ AJIIGEQO,

LC Density of Nominal Interences

Eey¥ytreme Contiict

окей Geneération Step (Evidence Chain} Inféréential Conflict Score [бели

Figure 1: An example of computational cognitive dissonance in Idefics2, where a cascade of failures leads to a coincidentally correct answer. (1) Perceptual Failure: The model hallucinates a 'motorcycle' in the evidence chain, an object not present in the image (a cyclist is visible). Our framework captures this as high Perceptual Instability (see panel (c)). (2) Logical Failure: [he model then contradicts its own faulty evidence, concluding the final answer is "No'. This breakdown of self-consistency is diagnosed as extremely high Inferential Conflict (see panel (d)). This case study demonstrates the limitation of accuracy-only evaluations and highlights our framework's ability to perform a stage-bystage differential diagnosis of a VLM's cognitive process, identifying complex, multi-stage failure trajectories.

interact within a single cognitive trajectory. Current approaches to hallucination detection generally treat the generation process as an indivisible, monolithic event. [hey either evaluate the semantic consistency of final outputs via multiple sampling Manakul et al. (2023); Farquhar et al. (2024) or probe for a binary 'truthfulness' representation within internal states Azaria &amp; Mitchell (2023); Chen et al. (2024b). While foundational, these reductionist views conflate fundamentally different failure modes. They struggle to distinguish whether a hallucination stems from an initial failure to ground concepts in the image (perceptual drift) or from an illogical jump that bypasses extracted facts (inferential bypass). Our central thesis is that hallucination is a process-level failure that must be diagnosed within a structured model of cognition.

To address this, we introduce a normative principle of computational rationality Gershman et al. (2015); Oulasvirta et al. (2022) for VLMs, formalized as a Markovian information Percent flow: Image (Z) ape', Textual Evidence (Tevi) inference, Final Answer (A). This principle asserts that for a rational agent, the final answer A is conditionally independent of the image Т given the evidence Ти, implying the conditional mutual information Г.А; Z|7e,y;) must be zero. Critics might argue that requiring an explicit evidence chain limits the applicability of such a framework. However, we employ Chain-of-Thought (CoT) not as a strict operational! constraint, but as a crucial diagnostic probe in explainable Al (XAI)—akin to a medical contrast agent. By forcing the model to externalize its latent reasoning, we make the implicit cognitive trajectory observable and mathematically diagnosable.

To diagnose this cognitive process, we design a suite of probes. While Scons directly measures violations of our core principle, Perceptual Entropy (НЕ) and Decision Entropy

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1773828458_aqadlxrrg8mc0el8_ajuifvissupf_jaaa_ushno_the_scene.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
