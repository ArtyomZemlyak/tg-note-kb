# Image Description

**File:** img_1764597140_aqad4w9rg916cul_files_changed_snow_next_lines.jpg
**Original:** image.jpg
**Received:** 1764597140

## Extracted Text (OCR)

## Files changed

Snow next Lines vllm/model\_executor/models/mistral\_1] [|

ОФ -В 9 +1,63 @@

```
г тд г м 13 15 18 14 +7 SPDX-License-Identifier: Apache-2.6 +# SPDX-FileCopyrignhtlext: Copyright contributors t о the vLLM project +Ггом collections.abc import Iterable +import regex as re +import toren +Ггот vllm.model_executor.models .deepseek_v?2 import DeepseekV3ForCausalLM +class MistralLarge3ForCausalLM|[ DeepseekV3ForCausalLM): # ТТ

: oft + remapping = 1 r layers\.(\d+)\.attention_norm\.weight— ‚ Г model,layers.\1.input_layernorm.weignt , # поаа: Eo) r"layers\.(\d+)\.attention\.wa_a\.(\w+)" . r model.layers.\1.self_attn.q_a_proj.\2 , # пода: #597 г layers\.(\d+) \,attention\.q_a_norm\.weignt : г model, layers. \1.selT_attn.g_a_layernorm.welgnt , # noga: E561 г" layers\.(\d+)\.attention\.wg_b\. (\w+)" ‚ Г model.layers.\1.selT_attn.q_b_proj.\2 , # поаа: #591 г" Зауегз\ . (\d+} \ attention\.wkv_a_with_maa\. ( \wt) г model.layers.\1.self_attn.kv_a_proj_with_maga.\2аа = aur ts
```

<!-- image -->

<!-- image -->

## Usage Instructions

When referencing this image in markdown:
1. Use relative path based on file location
2. Add descriptive alt text based on OCR content above
3. Add text description BELOW the image for GitHub rendering

Example:
```markdown
![Description based on OCR](../media/img_1764597140_aqad4w9rg916cul_files_changed_snow_next_lines.jpg) <!-- TODO: Broken image path -->

**Image shows:** [Describe what the image contains based on OCR]
```
