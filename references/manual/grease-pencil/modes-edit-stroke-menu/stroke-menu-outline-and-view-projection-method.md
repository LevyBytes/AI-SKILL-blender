# Stroke Menu: **Outline.**, View - projection method

**Outline.**

Menu ‣ Grease Pencil ‣ Outline. Converts selected strokes into closed perimeter shapes, creating new strokes around the stroke boundary with adjustable thickness.

View - projection method:
- View: current viewport perspective.
- Front: X-Z axes (front view).
- Side: Y-Z axes (side view).
- Top: X-Y axes (top view).
- Camera: active camera perspective.

Radius: sets how far the outline extends on either side; larger numbers create thicker boundaries.

Offset Factor: shifts the outline in or out:
- Positive values expand the boundary away.
- Negative values contract it toward the center.
- 0 positions it directly atop the original stroke.

Corner Subdivisions: subdivisions for smoothing corners; higher values create smoother corners but increase complexity.

**Trim.**

Menu ‣ Stroke ‣ Trim. Trims selected stroke to first loop or intersection.

**Join.**

Join: Menu ‣ Stroke ‣ Join ‣ Join; shortcut Ctrl+J. Connects two or more strokes into a single one.

Type:
- Join: connects strokes by connecting points.
- Join and Copy: connects strokes by connecting points in a new stroke.

Leave Gaps: when enabled, does not use geometry to connect strokes.

Join and Copy: Menu ‣ Stroke ‣ Join ‣ Join and Copy; shortcut Shift+Ctrl+J. Identical to Join except the method automatically becomes Join and Copy.

**Move to Layer.**

Menu ‣ Stroke ‣ Move to Layer; shortcut M. Opens a menu to reassign the stroke to a different layer from existing ones or define a fresh layer.

**Assign Material.**

Menu ‣ Stroke ‣ Assign Material. Reassigns the material for the selected stroke, picking from the current Grease Pencil object's material library.

**Set as Active Material.**

Menu ‣ Stroke ‣ Set as Active Material. Makes the active object material match the material of the selected stroke.

**Arrange.**

Menu ‣ Stroke ‣ Arrange. Changes the drawing order of strokes in the 2D layer.

Bring to Front: moves selected points or strokes to the top.

Bring Forward: moves selected points or strokes up one position.

Send Backward: moves selected points or strokes down one position in the drawing order.

Send to Back: moves selected points or strokes to the bottom.

[Related references](INDEX.md).
