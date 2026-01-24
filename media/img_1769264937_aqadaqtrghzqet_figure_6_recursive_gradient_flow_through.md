# Image Description

**File:** img_1769264937_aqadaqtrghzqet_figure_6_recursive_gradient_flow_through.jpg
**Original:** image.jpg
**Received:** 1769264937

## Extracted Text (OCR)

Figure 6: Recursive gradient flow through working memory. With working-memory capacity //—40, at sentence step t=42, the forward pass cross-attends only to the current memory contents 4S2,...,S41 ¢ (51 has been evicted from the fixed-capacity memory). However, because sentence vectors are written to memory without detaching, the vectors in the memory retain computation-graph links to the graph of earlier sentences that they attended to when they were formed. Thus, gradients from the step 42 token losses backpropagate through the stored computation graphs and reach $1 via the graph of the stored $2. | he chain terminates at the first sentence of each sentence stream, where the memory Is reset (Stop-gradient).

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1769264937_aqadaqtrghzqet_figure_6_recursive_gradient_flow_through.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
