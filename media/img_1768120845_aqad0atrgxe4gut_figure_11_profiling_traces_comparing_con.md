# Image Description

**File:** img_1768120845_aqad0atrgxe4gut_figure_11_profiling_traces_comparing_con.jpg
**Original:** image.jpg
**Received:** 1768120845

## Extracted Text (OCR)

Figure 11 Profiling traces comparing convld implementations on production shape. PyTorch convld (top) launches five separate kernels including layout transformations and GEMM. Py'Torch conv2d (middle) reduces to four kernels via optimized NHWC paths. KernelEvolve (bottom) fuses operations into two kernels with cross-operation fusion. Note that durations shown in the profiling trace include profiling overhead and do not represent actual kernel latency.

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1768120845_aqad0atrgxe4gut_figure_11_profiling_traces_comparing_con.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
