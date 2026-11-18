---
name: xxd-panel-223
description: "XXD Panel 223｜Vintage Engraved Miniature Atlas: breaks a photo into a small set of separate, unconnected miniature motifs — a few representative figures, details, objects, plants or architectural features — each drawn in vintage engraving linework with letterpress or woodcut texture (dark outlines, carved lines, hatching, black blocks, slight ink loss and offset), sparsely arranged so 70–80% of the warm white or ivory page stays empty, using black plus one accent per motif from two or three spot colours drawn from the photo (such as deep wine, petrol teal, ochre gold or ink green), with a few small, light, widely spaced words. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-223 or asks for vintage engraved spot illustrations, miniature motif sheets or old field-guide plates from a photo."
---

# XXD Panel 223

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.

## Panel-specific overlay

The transformed design is a sparse collection of small independent engraved motifs, not one large scene. Motifs stay unconnected, with about 70–80% of the field left as intentional paper. Draw them as vintage engraving and letterpress or woodcut: dark contours, cut lines, hatching and black-and-white masses, with slight uneven ink. Each motif is usually black plus one accent taken from the source. Type is sparse, small and editorial. It is not a modern flat icon set, a realistic sketch, a photo outline, connected decoration, a filled frame or a fully coloured illustration.

These overlay rules add to `references/soldier-runtime.md`. They never replace the source brief or the family runtime contract.

Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-223/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-223-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
