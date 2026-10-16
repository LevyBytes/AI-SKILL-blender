# Spline types and control points

## Curve Structure

Splines are the basic parts of curve objects, defining their shapes.
A curve object can hold multiple splines,
like how a mesh object can have multiple separate meshes.
Each spline's shape comes from its Control Points.
Splines exist in types: Poly, Bézier, and NURBS, each with its own curve-definition method,
covered in the Spline Types section.

Splines carry unique properties adjustable in Edit Mode via the
Active Spline panel.

Control Points:

Each spline is assembled out of control points that join together into its shape.
Selecting and dragging those points lets you reshape the spline—
much the same idea as nudging the vertices on a mesh.

See also

Curve Editing

Spline Types:

Poly:

Poly splines are the simplest kind, performing no interpolation from one point across to the next.
Used when converting meshes to curves
for faithful original mesh representation.
Though Poly splines are exact, Bézier or NURBS splines typically work better for smooth curves.

Bézier:

Bézier splines use points and handles to form their shape.
A segment lies between two points, with handles controlling curvature.

Below, the points sit at the pink line centers, with handles extending outward.
Arrows show curve normals, pointing direction and tilt.

Bézier Curve in Edit Mode. 

Bézier curves support four handle varieties, changed with V :

Bézier Curve Handle Types. 

Automatic :

Automatically sets handle length and direction for the smoothest curve.
Shown as yellow. Becomes Aligned when moved.

Vector :

Handles aim directly at neighbor points, allowing straight lines or sharp corners.
Shown as green. Becomes Free when moved.

Aligned :

Handles sit on a straight line, ensuring smooth curves.
Shown as purple.

Free :

Handles move independently, allowing asymmetric curves.
Shown as black.

Note

When a point is active, its handles highlight in red, changing their standard color.
For instance, Vector handles (usually green) appear yellow when active,
which can look like Automatic handles.

To fix this,
adjust the relevant entries under 3D Viewport ‣ Active Spline within Theme Preferences.

NURBS:

NURBS (Non-Uniform Rational B-Splines) describe curves with full mathematical exactness.
Where a Bézier curve merely approximates its target—a Bézier "circle," for instance, only comes close to a real circle—
a NURBS form reproduces the precise shape.

See the Wikipedia page for more.

NURBS points carry a unique weight property setting their influence on the curve.
This weight differs from Goal Weight used in soft body settings.
Adjust weights in the W field of the Transform panel.

Note

When all points share the same weight, their effects balance out.
Weight differences make the curve shift toward or away from specific points.

[Related references](INDEX.md).
