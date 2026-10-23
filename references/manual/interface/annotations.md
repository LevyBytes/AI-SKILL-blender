# Annotations

## Annotations

The annotation tool is available in several editors and lets you add notes to things like 3D objects or node setups (the arrow in the manual's screenshot is an annotation).

Annotation Tools: activate the tool in the Toolbar; its sub-tools are:
- Annotate: draw free-hand strokes in the main area.
- Annotate Line: click and drag to make a line, optionally choosing an arrow style for the start and end.
- Annotate Polygon: click repeatedly to chain connected lines, then press Return or Esc to confirm.
- Annotate Eraser: click and drag to remove lines; its Radius is set in Tool Settings.

Tool Settings - Common:
Color: set the color of existing and new strokes.
Annotation Layer: a pop-over menu (showing the current layer's name) for reaching the Annotation Layers.
Placement - where annotations are drawn:
- 3D Cursor: 3D Viewport only; the annotations join the 3D scene, drawn on an imaginary plane through the 3D Cursor and aligned to your view.
- Surface: 3D Viewport only; the annotations join the 3D scene, drawn onto the surface of the object under the mouse, falling back to 3D Cursor behavior where there's no surface.
- Image: 2D editors only (such as the Image Editor); the annotations join the 2D space, so their position and size shift as you pan and zoom.
- View: the annotations are 2D and stick to the screen, keeping their position, rotation, and size through any pan, orbit, or zoom.
Only End Points (Surface placement): snap using only the first and last parts of the stroke.
Project Onto Selected (Surface placement): project the strokes only onto selected objects.
Stabilize Stroke: curbs stroke jitter while drawing by delaying and correcting point locations.
Radius: the minimum distance from the last point before the stroke continues.
Factor: a smoothing factor; higher values give smoother strokes but make drawing feel like you're dragging the stroke along.

Annotate Line:
Style Start, End: the decoration at the beginning or end of the line segment, for example to make arrows pointing out specific scene details.

Annotation Layers: with the annotation tool enabled, the settings for managing multiple layers live in the Sidebar ‣ View ‣ Annotations panel.
Opacity: adjust the opacity of existing and new strokes.
Thickness: adjust the thickness of existing and new strokes.

Onion Skin: shows a ghosted image of strokes from frames before and after the current one; it works only in the 3D Viewport and Sequencer (see the Grease Pencil documentation on Onion Skinning).
Before/After: the color used for ghost frames before and after the current frame, with the number setting how many frames to show before and after.

[Related references](INDEX.md).
