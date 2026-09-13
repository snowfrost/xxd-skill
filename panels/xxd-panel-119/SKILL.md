---
name: xxd-panel-119
description: "Create XXD Panel 119 raster artwork by translating a source photograph into a hand-sewn textile collage with simplified fabric silhouettes, cotton-linen fibres, raw-edge appliqué, sparse embroidery, 2–4 vivid source-derived colours, and exceptionally generous negative space. Supports isolated image or directory inputs and strict 50:50 top-bottom or left-right comparisons, design-only work, and wallpapers. Use when the user invokes xxd-panel-119 or asks for this hand-sewn textile collage editorial style."
---

# XXD Panel 119

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

Before delivery, run the available xxd-strip-ai-meta workflow on final images and verify no AI provenance metadata remains. Inspect every result at full and thumbnail size. Accept only when the source, ratio, and source visibility are correct; for comparison modes, the split direction and exact 50:50 midpoint are correct; the transformed region follows the hand-sewn textile collage brief directly from the current source; the small distilled subject is built with few large layered fabric pieces, raw edges and sparse stitches; abundant negative space dominates and 2–4 source-derived colours remain lively, warm and clean; text follows the chosen mode and locale; and there is no watermark, SVG substitute, UI, third band, or second-pass artefact.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-119/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-119-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
