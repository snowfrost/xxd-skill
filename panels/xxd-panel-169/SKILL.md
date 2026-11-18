---
name: xxd-panel-169
description: "XXD Panel 169｜Warm Ochre Ink-line Spot Illustration: redraws the most recognisable subject of a photo as a small, isolated spot illustration that stops once the important part is drawn — loose, fine, slightly hesitant charcoal-black ink lines with broken and searching strokes, and thin transparent watercolour or gouache in ochre, tan and khaki with only a touch of burnt or terracotta orange on warm white paper, no competing blue, green or purple and no full background. About 75–85% of the design stays unpainted paper and 15–25% holds the subject, with a few words in a small, slightly imperfect editorial type. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-169 or asks for a spot illustration, vignette ink sketch or warm ochre pen-and-wash from a photo."
---

# XXD Panel 169

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

Keep 75–85% of the design region as unpainted warm-white paper and only 15–25% as an isolated spot vignette. Use thin loose charcoal-black ink, broken searching lines and tiny transparent washes. The fixed limited palette is warm white, charcoal grey, ochre/yellow-brown/khaki and sparse burnt or terracotta orange. Do not import competing blue, green or purple, large washes, thick outlines or a full watercolour landscape.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-169/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-169-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
