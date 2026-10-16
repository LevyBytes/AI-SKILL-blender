# Transform Panel

## Transform Panel

Edit Mode Transform panel properties:

Reference

Mode :

Edit Mode

Panel :

Sidebar ‣ Transform

When nothing is selected, the panel shows nothing.
With multiple vertices selected, the median is displayed
and "Median" appears in the labels.

Control Point, Vertex
The first set of controls (X, Y, Z) shows the coordinates of the chosen point or handle.
With NURBS curves, a fourth component appears (W),
setting the weight
of the chosen control point or median weight.

Space
Radio buttons choose whether coordinates are local
(relative to object origin) or global.

Global, Local

Weight
Set the "goal weight" for chosen control points,
used when a curve has Soft Body physics,
anchoring the curve to their original positions via the weight.

Radius
Control the extrusion/bevel width along the curve path.
Radius is smoothed point-to-point (visible via normals).

Tilt
Control how curve normals twist around each control point (applies to 3D curves only).
Tilt is smoothed point-to-point (visible via normals).

[Related references](INDEX.md).
