# Brush spacing, jitter and smoothing

## Spacing and strength

Spacing Distance is available in Sculpt Mode. View measures spacing relative to the viewport; Scene uses three-dimensional stroke positions, helping keep spacing consistent over curved surfaces.

Adjust Strength for Spacing keeps strength consistent when spacing changes. It applies to Space, Line, and Curve methods.

Dash Ratio controls the fraction of samples in each cycle where the brush is enabled. Dash Length sets the cycle length in stroke samples. Both apply to Space, Line, and Curve methods, for effects such as painted dashed lines or sculpted stitches.

## Jitter

Jitter offsets each dab's position. Its pressure control enables tablet-pressure sensitivity. Expand the control to edit the pressure-response curve; the default rising curve produces more jitter at higher pressure.

Jitter Unit chooses View for screen-space measurement or Scene for three-dimensional measurement. Scene Units sets the latter's unit system and scale.

## Input smoothing

Input Samples averages recent mouse positions to smooth the stroke. Use Unified Input Samples shares that setting across brushes.

Stabilize Stroke makes the stroke trail the cursor along a smoother path. Toggle it with `Shift-S` or its header checkbox.

- Radius is the minimum distance from the last position before the stroke continues.
- Factor controls smoothing. Higher values produce smoother strokes and a stronger dragging sensation.

[Related references](INDEX.md).
