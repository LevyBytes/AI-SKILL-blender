# Bounding Box Center

## Bounding Box Center

Bounding Box Center (pivot point) — Reference: Mode: Object Mode and Edit Mode; Location: Header ‣ Transform Pivot Point ‣ Bounding Box Center; Shortcut: Period. Here the pivot point sits at the center of the bounding box — the box wrapped as tightly as possible around the selection while staying aligned to the world axes. In Object Mode: the pivot lands at the midpoint of the box enclosing the selected objects' origin points rather than their geometry, so for a single selected object the pivot equals the object's origin point (which can be customized and needn't be centered — in the manual's example the orange rectangle has it in a corner). With multiple objects selected, the pivot becomes the center of an imaginary box around their origins; the manual contrasts this with Median Point, which instead averages the origins' positions, so the pivot shifts toward the area with the most objects. In Edit Mode: the pivot becomes the center of the bounding box around the selected mesh elements (the manual shows rotation in different selection modes with the pivot as a yellow circle), and again Median Point may give a different result.

[Related references](INDEX.md).
