# Surface Structure

## Surface Structure

### Surface Structure

Both Surfaces and Curves lean on Bézier or NURBS splines to build smooth geometry out of a set of control points. Where they part ways is in the output:
a Curve yields a line, whereas a Surface yields a sheet.

A single Surface object may hold several disconnected surfaces.
Whichever one is selected in Edit Mode goes by the name
"active spline."

### Control Point Grid

You might compare a Surface to a mesh carrying a
Subdivision Surface Modifier,
but the Surface is stricter: its control points have to sit in a rigid grid, where
every "row" marked by a yellow line carries the same number of
control points, and every "column" marked by a pink line does too.
Extending the surface is only possible by
extruding an entire row or column.

From the Active Spline panel you decide,
for each grid direction, whether the surface is cyclic (closed) and whether it
runs on Bézier or NURBS.

### Weights

To fine-tune the shape, change the weight of individual control
points over in the Transform Panel of the Sidebar.

Note that the relevant property goes by the name W ; a separate property labelled Weight
also exists, but that one serves as the Goal Weight for soft body simulations.

A control point with a higher weight pulls the surface towards it.

Note

Give every control point the same weight and they offset one another,
leaving the surface looking exactly as it did. For any effect to show, the
weights have to differ.

Pure shapes such as cylinders and spheres depend on weights to come out right.
The primitives in the Add menu
arrive with these already set.

Control point weights on a spherical Surface.

[Related references](INDEX.md).
