# Set Curve Normal Node

## Set Curve Normal Node

Set Curve Normal Node

Configures the normal calculation strategy for each curve. Normals are computed later as needed; the tilt attribute at each control point provides additional rotation around the tangent.

Internally modifies the normal_mode attribute per curve.

Inputs:
Curve — Standard geometry input.
Selection — Toggle whether to apply changes to each curve.
Mode — Calculation approach:
Minimum Twist — Minimizes tangent-axis rotation across the entire curve.
Z-Up — Perpendiculars to both the Z axis and tangent. Uses X for vertical curves.
Free — Employs a custom_normal attribute as the final normals. Provides an additional Normal input for setting values.

Note: Custom normals are not rotation-invariant; apply after rotations (end of tree or bottom of modifier stack).

Outputs:
Curve — Standard geometry output.

[Related references](INDEX.md).
