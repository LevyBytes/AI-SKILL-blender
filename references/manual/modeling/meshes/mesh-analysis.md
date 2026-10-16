# Mesh Analysis

## Mesh Analysis

### Mesh Analysis

Reference

Mode :

Edit Mode

Panel :

Header ‣ Overlays ‣ Mesh Analysis

Use mesh analysis to surface mesh attributes that could matter for particular workflows.

It runs in Edit Mode with Solid Viewport shading. High values come up red, low values blue, and anything beyond the chosen range turns gray. The modes available today are aimed mainly at 3D printing.

### Overhang

Because extrusion printers can only handle so much overhang before it fails, this mode visualizes overhang across an angle range with a selectable axis.

Minimum/Maximum
Low and high bounds of the angle shown.

Axis
The axis and direction the visualized angle is measured against.

Overhang.

### Thickness

Walls below a printer's minimum thickness won't come out, so this check casts rays over a distance range to gauge how thick the geometry is.

Minimum/Maximum
Low and high bounds of the thickness shown.

Samples
How many samples feed the thickness calculation.

Thickness.

### Intersections

Surfaces that cross one another are another frequent printing headache, since a model's inside and outside can no longer be told apart reliably.

This mode has no gradient; an element is either flagged or it isn't.

Intersecting faces.

### Distortion

Distorted geometry is a problem because there's no defined way to triangulate a distorted n-gon.

The measure is non-flatness: faces whose parts angle off in different directions.

Minimum/Maximum
Minimum/Maximum distortion to display.

Distorted Faces.

### Sharp Edges

As with thickness, sharp edges may produce features too thin to print.

Minimum/Maximum
Minimum/Maximum angle to display.

Sharp edges.

### Known Limitations

A couple of caveats apply to mesh analysis:

- At the moment it only shows up with Deform Modifiers.

- On high-poly meshes editing turns sluggish.

[Related references](INDEX.md).
