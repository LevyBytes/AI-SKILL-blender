# Draw

Reference

Mode: Edit Mode
Tool: Toolbar ‣ Draw

Draw freehand curves in the viewport.

Tool Settings

Curve Stroke panel.

Type specifies the curve basis.

Poly: A straight-segment Bézier (auto handles).
Bézier: Smoothed curve type.

Tolerance: Lower values match your stroke; higher values smooth it out.

Method determines the fitting approach:

Refit: Incremental refitting yields the best visual match.
Split: Iterative splitting prioritizes interactive responsiveness.

Detect Corners: When the angle exceeds the threshold, corners are recognized and handles are set non-aligned for crispness.

Taper Start, End: Shrink or expand the stroke's thickness at the beginning and endpoints.

Radius Min: The smallest stroke width at minimum pressure (also the taper minimum).
Max: Full stroke width at maximum pressure or no tablet.

Use Pressure: Stylus pressure modulates the radius.

Depth specifies drawing plane and method.

Cursor: Depth under the pointer.
Surface: Drawn atop other objects.

Project Onto Selected: Constrain projection to chosen objects only.

Offset: How far the curve sits from the surface.
Absolute Offset: A fixed distance unscaled by curve radius.
Only First: Depth sample at stroke beginning only.

Plane: Orientation when Only First is on.

Normal to Surface: Aligns to the surface.
Tangent to Surface: Perpendicular to surface direction.
View: Aligned to screen view.

Curve 2D: Project onto the Z axis.

As NURBS: Output NURBS with Bézier knots rather than plain Bézier.

After execution, the Adjust Last Operation panel offers refinement:

Error: Deviation distance in object units (subdivision rate analogue). Lower makes it closer to your input; higher smooths more.

Fit Method:

Refit: Incremental refitting (best results).
Split: Splitting until tolerance is reached (faster).

Corner Angle: Angles above this threshold are corners.

Cyclic: Toggle whether the curve closes on itself.

[Related references](INDEX.md).
