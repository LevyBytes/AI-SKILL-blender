# Interpolate

## Interpolate

### Interpolate

Reference

Mode :

Draw Mode

Tool :

Toolbar ‣ Interpolate

By interpolating strokes across the previous and next Grease Pencil keyframes, the Interpolate tool builds an in-between keyframe. Sit on a frame between two keyframes, then click and drag to add a fresh breakdown keyframe whose stroke shape is set by how far you drag.

This hands artists manual say over how strokes shift from one pose or drawing to the next, with fine control over the result.

Note

Interpolating across curves of differing types triggers a priority system that settles which curve type wins. From highest priority to lowest: NURBS –> Bézier –> Catmull-Rom –> Polyline .

### Usage

Park the Timeline playhead at any frame sitting between two existing Grease Pencil keyframes. Then drag sideways in the viewport — the horizontal distance sets the blend amount — and let go to lock it in. A fresh breakdown keyframe appears, holding strokes blended between its two neighbours according to the amount you dialled in.

### Tool Settings

Layer
Hold interpolation to the Active Layer or All Layers .

Only Selected ( Edit Mode )
Once active, the interpolation touches selected strokes only.

Exclude Breakdowns
Keep existing Breakdown keyframes from serving as interpolation extremes.

Flip Mode
Flips the interpolation direction, trading the start and end strokes. Automatic mode tries to work out the right direction per stroke on its own.

Smooth
How much smoothing the interpolated strokes get, to cut jitter or visual noise.

Iterations
How many smoothing passes run over the freshly made strokes. Higher counts smooth more but can erode shape fidelity.

[Related references](INDEX.md).
