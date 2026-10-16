# Editing UVs: Editing UVs, Stitch UV map pieces back together.

## Editing UVs

Editing UVs

After unwrapping, you need to arrange UV maps for texturing or painting. Your goals include:

Stitch UV map pieces back together.

Minimize unused space.

Enlarge faces where more detail is needed.

Resize stretched faces.

Shrink over-detailed faces.

With minimal wasted space, pixels can focus on maximum detail and fineness. A UV face ranges from single-pixel to entire-image size. Start with major adjustments, then fine-tune.

Transform Operations

Editor: UV Editor
Mode: Edit Mode
Toolbar: Move, Rotate, Scale, Transform
Menu: UV ‣ Transform

Move — G
Rotate — R
Scale — S
Shear — Shift - Ctrl - Alt - S

Axis Locking

After activating a transform tool, press X or Y to lock the transform axis. Holding MMB also constrains movement to X or Y.

Vertex Slide

Mode: Edit Mode
Menu: UV ‣ Transform ‣ Vertex Slide
Shortcut: Shift - V

Vertex Slide repositions a vertex along one of its adjacent edges. Activate with Shift - V. The selected vertex nearest the cursor becomes the control point. Drag along the edge direction to position the vertex, then LMB to confirm.

Factor — Controls the slide amount. Negative values slide toward one vertex; positive toward the other.

Even (E) — By default, offset is a percentage of edge length. When Even is active, vertices shift by a fixed value.

Flipped (F) — When active, vertices maintain equal distance from adjacent vertices instead of moving from their original position.

Clamp (Alt or C) — Toggle clamping the slide within edge bounds.

Edge Slide

Mode: Edit Mode
Menu: UV ‣ Transform ‣ Edge Slide

Slides one or more edges across adjacent faces (selection must define a valid loop).

Factor — Controls the slide amount. Negative slides toward one face; positive toward the other.

Even (E) — Forces the edge loop to match the shape of the adjacent edge loop. Press F to flip to the opposite vertex.

Flipped (F) — When Even is active, flips between adjacent edge loops that the active loop will match.

Clamp (Alt or C) — Toggle clamping within edge bounds.

Mirror Editing — Propagates the operation to mesh-symmetric elements (local X direction).

[Related references](INDEX.md).
