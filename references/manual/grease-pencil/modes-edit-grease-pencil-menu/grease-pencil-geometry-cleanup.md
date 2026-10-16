# Grease Pencil Menu: **Clean Up.**, Tools to remove degenerate geometry.

**Clean Up.**

Tools to remove degenerate geometry.

Clean Loose Points — Menu ‣ Grease Pencil ‣ Clean Up ‣ Delete Loose Points. Eliminates strokes composed of very few points. Limit defines the point count below which a stroke is considered loose.

Delete Duplicate Frames — Menu ‣ Grease Pencil ‣ Clean Up ‣ Delete Duplicate Frames. Removes duplicate keyframes.

Merge by Distance — Menu ‣ Grease Pencil ‣ Clean Up ‣ Merge by Distance. Simplifies strokes by merging selected points closer than a specified distance.

Merge Distance — threshold for merging points.

Unselected — allows selected points to merge with unselected ones; when disabled, only selected points merge together. Note: selected points must be contiguous unless Unselected is enabled.

Reproject Strokes — Menu ‣ Grease Pencil ‣ Clean Up ‣ Reproject. When strokes are drawn unintentionally at different 3D depths but appear correct from a particular view or camera, Reproject flattens them from a chosen viewpoint.

Reprojected Type:
- Front: onto the front plane (XZ).
- Side: onto the side plane (YZ).
- Top: onto the top plane (XY).
- View: onto the current viewport.
- Surface: onto mesh surfaces.

Surface Offset — controls stroke offset from the object when Surface mode is active.

Cursor — reprojected onto 3D cursor rotation.

Keep Original — preserves the original strokes after applying the tool.

**Outline.**

Menu ‣ Grease Pencil ‣ Outline. Converts selected strokes into closed perimeter shapes, creating new strokes around the stroke boundary with adjustable thickness.

View — defines the projection method:
- View: current viewport perspective.
- Front: X-Z axes (front view).
- Side: Y-Z axes (side view).
- Top: X-Y axes (top view).
- Camera: active camera perspective.

Radius — sets outline thickness on both sides of the original stroke; higher values produce wider perimeters.

Offset Factor — scales the outline inward or outward:
- Positive values expand the perimeter away.
- Negative values contract it toward center.
- 0 places the perimeter directly on the original stroke.

Corner Subdivisions — subdivisions for smoothing corners at stroke endpoints and joints; higher values create smoother corners but increase complexity.

**Delete.**

Menu ‣ Grease Pencil ‣ Delete; shortcuts X, Delete. Opens a menu for removing geometry.

Strokes — Menu ‣ Grease Pencil ‣ Delete ‣ Strokes. Removes selected points; a stroke with only one point becomes invisible, and a stroke with all points removed is deleted entirely.

Only Strokes — Menu ‣ Grease Pencil ‣ Delete ‣ Only Strokes. Removes the stroke outline while preserving any fill geometry.

Only Fills — Menu ‣ Grease Pencil ‣ Delete ‣ Only Fills. Removes only fill components, leaving the stroke outline.

Dissolve — Menu ‣ Grease Pencil ‣ Delete ‣ Dissolve; shortcut Ctrl+X. Removes points between other points and reconnects the remaining ones.

Ctrl+X opens a menu to choose the dissolve type:
- Dissolve: removes selected points without splitting the stroke; remaining points stay connected.
- Dissolve Between: removes all points between selected points without splitting.
- Dissolve Unselect: removes all unselected points without splitting.

Delete Active Keyframe (Active Layer) — Menu ‣ Grease Pencil ‣ Delete ‣ Delete Active Keyframe (Active Layer). Wipes whatever strokes occupy the present frame on that one active layer.

Delete Active Keyframes (All Layers) — Menu ‣ Grease Pencil ‣ Delete ‣ Delete Active Keyframes (All Layers); shortcut Shift+Delete. Purges every stroke existing on this keyframe across all available layers.

[Related references](INDEX.md).
