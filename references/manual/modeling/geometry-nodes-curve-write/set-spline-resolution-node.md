# Set Spline Resolution Node

## Set Spline Resolution Node

Set Spline Resolution Node

Configures the evaluated-point count per control point for NURBS, Bézier, and Catmull Rom splines. No effect on poly splines or Bézier segments between vector handles.

Evaluated points appear in the viewport, feed Curve to Mesh Node, and optionally supply Resample Curve Node. Higher settings improve operations like trimming and sampling but reduce speed.

Related: Spline Resolution node reads this attribute.

Inputs:
Curve — Standard geometry input.
Selection — Boolean mask for which splines change.
Resolution — Evaluated points per control point. Higher values increase accuracy at computational cost.

Outputs:
Curve — Standard geometry output.

[Related references](INDEX.md).
