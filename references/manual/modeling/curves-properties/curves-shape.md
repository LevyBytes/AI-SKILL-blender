# Shape

## Shape

Shape panel controls curve appearance.

Shape panel. 

Dimensions
New curves default to 3D, allowing control points anywhere in space.
Set to 2D to restrict points to the curve's local XY plane.

Resolution Preview/Render U
The resolution property defines points calculated between each pair of control points.
Curves become smoother or rougher by adjusting resolution.
Preview U sets 3D Viewport resolution; Render U sets render resolution. If Render U is zero (0),
Preview U applies to both 3D Viewport and render.

| Description | Description |
| --- | --- |
| Curves with a resolution of 3.  | Curves with a resolution of 12.  |

Twist Method
3D curves have control points outside the local XY plane.
This creates twist affecting curve normals.
Adjust how twist calculates by choosing
Minimum, Tangent, or Z-Up.

| Description | Description |
| --- | --- |
| Curves with a twist of Minimum.  | Curves with a twist of Tangent.  |

Smooth
Interactively remove twists from the curve. Useful if a curve has "kinks"
from over-twisting; possible when converting meshes to curves.

Fill Mode
Fill determines display when a curve is beveled (see Beveling details below).
Set to Half for display as half a cylinder.

| Description | Description |
| --- | --- |
| Curves with a fill of Half.  | Curves with a fill of Full.  |

Fill Solver
Triangulation algorithm for filling 2D curves.

Sweep Line :

Fast triangulation for well-formed outlines.
Doesn't handle self-intersecting curves.

Delaunay :

Uses Constrained Delaunay Triangulation (CDT).
More robust, supports self-intersecting curves, but slower.

Fill Rule
Fill rule for the Delaunay Fill Solver determining inside regions.

Even-Odd :

Alternate inside/outside based on boundary crossing count.
Overlapping regions may cancel based on crossing count.

Non-Zero :

Inside/outside depends on winding direction.
Overlapping curves with matching winding are filled as union;
opposite winding creates holes.

Curve Deform

Radius
Scale the deformed object by the curve's radius.
Used with curves as paths or the Curve Modifier.

Stretch
Let the mesh object stretch or compress across the entire curve.
Combine with Bounds Clamp for intended behavior.
Used with the Curve Modifier.

Bounds Clamp
Disregard the object and mesh offset along deformation axis.
Helpful with Stretch or negative axes.
Used with the Curve Modifier.

[Related references](INDEX.md).
