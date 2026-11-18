---
name: xxd-panel-030
description: "XXD Panel 030｜Nature Unbound: rebuilds the subject of a photo as an editorial illustration assembled from real, clearly recognisable natural materials — leaves, petals, twigs, fruit, seeds, grass stems, bark and dried leaves — using their own shapes, textures and irregular edges rather than cutting them into neat geometry or outlining them, set mostly inside a simple rectangular colour field or paper area (no drawn frame) with a few directional parts growing naturally past its edge, wide whitespace on a pale ground, only a few thin, loose black hand-drawn marks for eyes, mouth, small gestures or links, and a short title with a few tiny notes aligned to a twig or leaf. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-030 or asks for botanical collage illustration, pressed-leaf and petal art or natural-material assemblage from a photo."
---

# XXD Panel 030

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-030/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-030-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
