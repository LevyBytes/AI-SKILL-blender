# Active Spline

## Active Spline

### Active Spline

Reference

Editor :

3D Viewport

Mode :

Edit Mode

Panel :

Sidebar ‣ Item ‣ Active Spline

The properties of whichever surface is currently active live in the Active Spline panel.

Active Spline panel.

Cyclic U/V
Turn this on and the surface's last row/column loops back to the first,
forming a closed loop.

Bézier U/V
Turn this on and, along the row/column direction, the surface is built from a chain of Bézier splines
in place of a NURBS curve.

Endpoint U/V
Sets whether the surface reaches all the way to the edges of its control point grid.

Surface with Endpoint U enabled.

Order U/V
Raising Order widens how far each control point reaches along its
row/column. The surface comes out smoother, but it hugs
the shape of the control grid less tightly.
See NURBS Curves Order.

Surfaces with Order U set to 2 (top) and 4 (bottom).

With Bézier turned on, Order instead sets how many control points each spline gets.

Order in any one direction can't exceed the count of control
points running along that direction.

Resolution U/V
Sets the preview density of the generated surface mesh. Crank it up and you get
more vertices and a smoother-looking surface.

Only the active surface is affected by this. To set the resolution for every surface
in the object, turn to the Resolution Preview U/V setting in the
Shape panel instead.

Should the Render U/V values in the Shape panel be nonzero, they take precedence over these
Resolution U/V values when rendering.

Smooth
Whether smooth shading gets applied
to the generated surface mesh.

[Related references](INDEX.md).
