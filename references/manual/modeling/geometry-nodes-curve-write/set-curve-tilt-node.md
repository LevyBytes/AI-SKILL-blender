# Set Curve Tilt Node

## Set Curve Tilt Node

Set Curve Tilt Node

Adjusts the tilt angle rotating the normal vector at each control point during evaluation. Retrieved by Normal Node.

The rotation mechanism: Axis Angle around the tangent, equivalent to Vector Rotate Node applied to the untransformed normal using tangent as axis and tilt as angle.

Related: Curve Tilt node reads this attribute.

Inputs:
Curve — Standard geometry input.
Selection — Boolean mask for which control points change.
Tilt — Per-point rotation angle.

Outputs:
Curve — Standard geometry output.

[Related references](INDEX.md).
