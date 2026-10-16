# Fillet Curve Node

## Fillet Curve Node

The Fillet Curve node smooths corners on curve points, similar to bevel on 2D mesh. The rounded sections are always circular arcs.

Curve: Standard input (curve component).
Radius: Circle arc radius per fillet.
Count: For Poly mode, control point count per fillet.
Limit Radius: Cap the radius to prevent overlapping fillets.
Mode: How to add vertices.

Bézier: Two control points per fillet. The aligned handles form the circular shape; segments depend on the spline's resolution.
Poly: Direct control of fillet vertices via an integer field input. Better for poly and NURBS.

Curve: Standard output.

A 3D poly spline with rounded corners. 

Fillet combined with curve primitives.

[Related references](INDEX.md).
