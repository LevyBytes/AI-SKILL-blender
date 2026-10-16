# Sculpt paint and pose overlays

Sculpt Mode Overlays:
Mask — overlays Masks onto an object, with adjustable opacity.
Face Sets — overlays Face Sets onto an object, with adjustable opacity.

Vertex Paint Overlays:
Stencil Mask Opacity — has no effect here (stencil masks exist only for texture painting).
Show Wire — draws mesh edges in white (whereas the Wireframe overlay draws them black).

Weight Paint Overlays:
Opacity — the overlay's opacity.
Zero Weights — paints unreferenced and zero-weighted regions black, helping you locate spots with very low painted weight.
  None — vertices appear as normal.
  Active — vertices read black with no weight in the active vertex group.
  All — vertices read black with no weight in any vertex group.
Show Weight Contours — draws contour lines linking points of equal interpolated weight. This exposes weight variation too subtle to read from color alone and is useful for judging how smooth and even a gradient is, e.g. while using smoothing tools and brushes.
Show Wire — draws mesh edges in white (the Wireframe overlay draws them black).

Texture Paint Overlays:
Stencil Mask Opacity — the opacity of the stencil-mask overlay.

Pose Mode Overlays:
Fade Geometry — keeps the bones up front and pushes other geometry to the back, with opacity on a slider; available only in Pose Mode.

Grease Pencil — these overlays appear when a Grease Pencil object is selected.
Onion Skin — shows ghosts of the keyframes flanking the current frame; with Multiframe on, it instead ghosts the selected keyframes (see Onion Skinning).
Active Object Only — limits the onion skins to the active object.
Fade Inactive Layers — lowers the opacity of every layer in the object except the active one, controlled by a slider.
Fade Inactive Objects — covers the whole viewport apart from the active Grease Pencil object with a solid-color layer, improving visibility while you draw over busy scenes.
Fade Grease Pencil Objects — includes or excludes Grease Pencil objects.
Edit Lines (Edit, Sculpt, Weight Paint, or Vertex Paint Modes; Shift-Q) — draws a line between points on top of other geometry while you edit strokes.
Only in Multiframe (Shift-Alt-Q) — with Multiframe on and keyframes other than the current one selected, those keyframes' strokes show as edit lines only, the strokes themselves hidden; this leaves Onion Skinning untouched.
Handles — sets the visibility of Bézier curve handles in edit mode.
  None — hides every Bézier handle for an unobstructed look at the curve.
  Selected — shows handles only for selected control points.
  All — shows handles for all of the curve's control points.
Stroke Direction (Edit) — toggles drawing the selected strokes' start points (green) and end points (red) to reveal their direction.
Material Name (Edit) — shows the material name beside the selected strokes.
Vertex Paint Opacity (Vertex Paint) — how opaque the vertex-color overlay appears, taking effect in both Vertex Paint Mode and Draw Mode. In Draw Mode vertex paint is by default visible only in Material Preview and Rendered shading; to see it in Solid mode, either switch to Vertex Paint Mode or set the Color shading option to Attribute.

Canvas — draws a grid across the Grease Pencil drawing plane.
Canvas Grid Opacity — the grid's opacity.
Canvas X-Ray — draws objects behind the canvas grid.
Subdivisions — the count of subdivisions dividing one grid line from the next.
Grid Color — what color those grid lines are drawn in.
Scale X/Y — the grid's horizontal/vertical size.
Offset X/Y — how far to shift the grid up/down and left/right.

[Related references](INDEX.md).
