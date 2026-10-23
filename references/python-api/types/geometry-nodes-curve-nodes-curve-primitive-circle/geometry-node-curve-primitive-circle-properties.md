# bpy.types.GeometryNodeCurvePrimitiveCircle: properties

## GeometryNodeCurvePrimitiveCircle(GeometryNode)

### GeometryNodeCurvePrimitiveCircle(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurvePrimitiveCircle ( GeometryNode )

Build a circle as a poly spline.
mode

Selects how the radius and position of the circle are worked out (default 'RADIUS' )

- POINTS
Points – Establish both the radius and the location from three points.

- RADIUS
Radius – Set the radius from a float value.

Type :

Literal[‘POINTS’, ‘RADIUS’]

[Related references](INDEX.md).
