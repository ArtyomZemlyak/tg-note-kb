# Image Description

**File:** img_1763367539_aqadzqtrg8hyuh_llm_output_drift_cross_provider_validati.jpg
**Original:** image.jpg
**Received:** 1763367539

## Extracted Text (OCR)

## LLM Output Drift: Cross-Provider Validation &amp; Mitigation for Financial Workflows

Rolando Franco

IBM - Financial Services Market New York, USA rfranco@us.ibm.com

## 1 Introduction

The financial services industry's adoption of LLMs for operational! tasks—from regulatory reporting to client communications—faces a fundamental challenge: nondeterministic outputs that violate audit and compliance requirements. Recent infrastructure incidents dramatically underscore this issue.

On September 17, 2025, Anthropic reported that Claude produced random anomalies due to a miscompiled sampling algorithm affecting only specific batch sizes [4]. Similarly, Thinking Machines Lab demonstrated that a 235B parameter model at temperature=@ produced 80 unique completions across 1000 identical runs due to batch variance effects [44].

Production incidents throughout 2024-2025 demonstrate persistent challenges in LLM determinism. ОрепАГ $ investigation into reported Codex degradation [33] reveals nondeterministic behavior affecting code generation quality—paralleling our findings on output drift. Notably, OpenAl's release of GPT-OSS-Safeguard-20B [34] signals industry recognition that smaller, purpose-built models may better serve compliance-critical workflows than frontier models. Microsoft's Azure outage on October 30, 2025, disrupted Al services including Copilot due to global misconfiguration [42]. demonstrating infrastructure-induced nondeterminism in cloud deployments. The Shadow Escape Attack exploit disclosed October 29 enables zero-click data extraction from LLMs via malicious PDFs [35], creating compliance risks in audit-exposed processes. These incidents align with our economic analysis of verification overhead, as deployments like Chronograph $ Claude integration for private equity portfolio analysis [13] demand deterministic controls to prevent drift in high-stakes financial decisions.

The economic implications are substantial. Morgan Stanley estimates $920 billion in potential savings from Al automation of fhnancial knowledge work [28], yet as industry observer Gene Marks

IBM - Financial Services Market New York, USA rafhi.khatchadourian!@ibm.com

Financial institutions deploy Large Language Models (LLMs) for reconciliations, regulatory reporting, and client communications, but nondeterministic outputs (output drift) undermine auditability and trust. We quantify drift across five model architectures (7B-120B parameters) on regulated financial tasks, revealing a stark inverse relationship: smaller models (Granite-3-8B, Qwen2.5-7B) achieve 100% output consistency at T=0.0, while GPT-OSS-120B exhibits only 12.5% consistency (95% CI: 3.5-36.0%) regardless of configuration (p&lt;0.0001, Fisher's exact test). This finding challenges conventional assumptions that larger models are universally superior for production deployment.

Our contributions include: (i) a finance-calibrated deterministic test harness combining greedy decoding (T=0.0), fixed seeds, and SEC 10-K structure-aware retrieval ordering; (ii) task-specific invariant checking for RAG, JSON, and SOL outputs using financecalibrated materiality thresholds (+5%) and SEC citation validation; (iii) a three-tier model classification system enabling riskappropriate deployment decisions; and (iv) an audit-ready attestation system with dual-provider validation.

structured tasks (SOL) remain stable even at T=0.2, while RAG tasks show drift (25-75%), revealing taskdependent sensitivi

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1763367539_aqadzqtrg8hyuh_llm_output_drift_cross_provider_validati.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
