# Set Spline Type Node

Set Spline Type:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Set Spline Type

Shortcut :

V

Convert splines between Bézier, NURBS, Poly, and Catmull Rom types.
This is basic conversion—Blender doesn't preserve exact shape or point count.
For instance, converting NURBS to Bézier maps each three-point NURBS group
to one Bézier point with two handles.

Type
Specify the target spline type. See the
Spline Types documentation for details.

Bézier :

Convert to Bézier type.
- Poly splines convert with vector handles.
- NURBS or Catmull Rom splines convert with automatic handles.

Note

NURBS to Bézier conversion requires at least six points.
Non-multiple-of-three point counts result in truncation.

NURBS :

Convert to NURBS type.

Poly :

Convert to poly type.

Handles
Incorporate handle information during conversion.

Show/Hide:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Show/Hide

Shortcut :

Alt - H , H , Shift - H

Hide or show Edit Mode elements.
Only control points toggle; segments always display unless all connected points hide.

See Show/Hide in Object Mode .
See also the Curve Display panel.

## Set Spline Type Node

Set Spline Type Node

Converts splines to a target classification.

Inputs:
Curve — Standard geometry input with curve data.
Selection — Splines to convert.

Properties:
Spline Type — Target type. Consult Spline Types documentation.

Bézier — From poly: vector handles. From NURBS/Catmull Rom: auto handles. Requires ≥6 points for NURBS conversion; truncation occurs if point count is not a multiple of three.

NURBS — Target classification.
Poly — Target classification.
Catmull Rom — Target classification.

Outputs:
Curve — Standard geometry output.

[Related references](INDEX.md).
