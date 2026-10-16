# Curves: Set Curve Type, Edit Mode

Set Curve Type:

Reference

Mode :

Edit Mode

Menu :

Curves ‣ Set Curve Type

Shortcut :

V

Convert splines between Bézier, NURBS, Poly, and Catmull Rom types.
Basic conversion—Blender doesn't maintain exact shape or point count.
Converting NURBS to Bézier maps each three-point NURBS group
to one Bézier point with handles.

Type
Specify the target type. See the
Spline Types documentation.

Bézier :

Convert to Bézier type.
- Poly convert with vector handles.
- NURBS or Catmull Rom convert with automatic handles.

Note

NURBS to Bézier conversion requires at least six points.
Non-multiple-of-three counts truncate.

NURBS :

Convert to NURBS type.

Poly :

Convert to poly type.

Catmull Rom :

Convert to Catmull Rom type.

Handles
Include handle information during conversion.

Toggle Cyclic:

Reference

Mode :

Edit Mode

Menu :

Curves ‣ Toggle Cyclic

Shortcut :

Alt - C

Switch between open and closed (Cyclic) curves.
Only curves with at least one chosen point close or open.
Closing segments use start/end handles for Bézier and neighbor points for NURBS.
Auto handles update if they are Auto type.
Open and Closed curves. 

This action applies only to the original first or last added point.
Segment deletion doesn't change this—only starting and last points apply. This means
Alt - C may join two curves instead of closing one!
Remember: closing a 2D curve creates a renderable flat face.

Open and Closed curves.

[Related references](INDEX.md).
