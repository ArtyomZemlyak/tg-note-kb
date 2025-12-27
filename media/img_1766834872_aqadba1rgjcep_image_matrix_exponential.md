# Image Description

**File:** img_1766834872_aqadba1rgjcep_image_matrix_exponential.jpg
**Original:** image.jpg
**Received:** 1766834872

## Extracted Text (OCR)

<!-- image -->

## Matrix Exponential Attention

Author: Yifan Zhang

Date: December 15, 2025

<!-- formula-not-decoded -->

MEA approximates the matrix exponential of attention scores via a truncated Taylor series. By leveraging the stateSpace realization of Higher-order Linear Attention (HLA), MEA computes high-order interaction terms (powers of the attention matrix) in linear time without materializing n x и matrices.

See Higher-order Linear Attention (HLA) for the theoretical foundation of the streaming algorithms used here.

## Mathematical Formulation

Standard Scaled Dot-Product Attention utilizes the softmax nonlinearity:

<!-- formula-not-decoded -->

MEA replaces the softmax with the Matrix Exponential (MExp ). For ап unnormalized attention matrix А = ОК.

<!-- formula-not-decoded -->

We approximate this by truncating the series at order H (typically H = 2).

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1766834872_aqadba1rgjcep_image_matrix_exponential.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
