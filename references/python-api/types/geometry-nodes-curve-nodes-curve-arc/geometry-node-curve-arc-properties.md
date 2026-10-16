# bpy.types.GeometryNodeCurveArc: properties

## GeometryNodeCurveArc(GeometryNode)

### GeometryNodeCurveArc(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurveArc ( GeometryNode )

Build an arc as a poly spline.
mode

Selects how the radius and position of the arc are worked out (default 'RADIUS' )

- POINTS
Points – Lay the arc through 3 points on a circle; the curve runs between the start and end of those points.

- RADIUS
Radius – Set the radius from a float value.

Type :

Literal[‘POINTS’, ‘RADIUS’]

[Related references](INDEX.md).
