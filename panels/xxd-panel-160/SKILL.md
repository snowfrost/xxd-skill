---
name: xxd-panel-160
description: "XXD Panel 160｜Expressive Pen-and-wash Illustration: redraws the most recognisable subject of a photo as an expressive pen-and-wash illustration — free, loose, sketch-like ink or fineliner lines with searching, repeated and unclosed strokes, then a few touches of transparent watercolour and simplified colour patches in 2–4 lively, brightened colours from the photo — one small, clear focal point with almost no background and very large whitespace, plus a few quiet words. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-160 or asks for loose ink-and-watercolour, urban-sketch or pen-and-wash illustration from a photo."
---

# XXD Panel 160

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

Use loose pen lines, searching or repeated marks, open edges and sparse transparent watercolour. Retain one small recognisable focus and vast whitespace; remix 2–4 lively source colours into light washes. Avoid complete scene tracing, heavy modelling, precise vector lines and filled backgrounds.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-160/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-160-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
