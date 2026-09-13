---
name: xxd-panel-180
description: "Create Panel 180 raster artwork: vintage circular souvenir stamps with woodcut and etched print texture on aged ivory paper. Use when the user invokes xxd-panel-180 or requests this visual language."
---

# XXD Panel 180

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

The source explicitly prohibits left-right layout and Chinese captions: preserve these defaults. An explicit current request for left-right mode overrides only the layout prohibition; explicitly requested text or locale overrides only the corresponding text restriction. State these overrides in the delivery preamble and retain every other source instruction. For default prompt text, preserve the source brief’s English headline below the stamp and smaller keywords beneath it. Use English unless the current user explicitly overrides the language.

Recompose the core subject plus only 1–2 identifying environmental clues into a small circular souvenir stamp. Use hand-cut woodcut/rubber-stamp and etched print textures: worn broken variable-width lines, aged ivory paper fibres, subtle impressions, ink absorption, uneven coverage, slight colour misregistration and missing ink. Derive 2–3 faded vintage ink colours from the source. Optional gold foil must be tiny. Preserve subject identity and extensive intentional whitespace; placement may be centred or asymmetrical. Retain the English headline below the stamp with smaller keywords beneath it, rather than reducing all copy to tiny annotations. Avoid smooth vectors, anime, watercolour, impasto, 3D, glossy icons and thick black frames.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-180/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-180-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
