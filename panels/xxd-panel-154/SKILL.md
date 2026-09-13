---
name: xxd-panel-154
description: "Create XXD Panel 154 raster artwork from photographs using true low-resolution 16-bit pixel art, deliberate hard-edged pixel clusters without anti-aliasing, a 2–4-colour palette, a small stamp-like subject, bitmap text and vast whitespace. Use when the user invokes xxd-panel-154 or requests this style. Supports individual images, isolated directory batches, strict 50:50 comparisons, design-only outputs, and wallpapers."
---

# XXD Panel 154

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

Check deliberate pixel clusters, visibly stepped contours, the restricted source-derived palette, and a small stamp-like anchor. Do not accept a mosaic-filter photograph as pixel art. If deterministic resizing is needed, preserve hard edges in the design with nearest-neighbor resampling; keep photographic resampling separate. This Panel's `scripts/compose_panel.py` may use NEAREST for the design region; do not replace it with the family LANCZOS helper.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-154/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-154-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
