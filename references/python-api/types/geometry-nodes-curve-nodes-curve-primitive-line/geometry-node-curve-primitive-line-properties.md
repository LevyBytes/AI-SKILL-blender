# bpy.types.GeometryNodeCurvePrimitiveLine: properties

## GeometryNodeCurvePrimitiveLine(GeometryNode)

### GeometryNodeCurvePrimitiveLine(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurvePrimitiveLine ( GeometryNode )

Build a two-point line as a poly spline.
mode

Selects how the radius and position of the line are worked out (default 'POINTS' )

- POINTS
Points – Set the line from its start and end points.

- DIRECTION
Direction – Set the line from a start point plus a direction and a length.

Type :

Literal[‘POINTS’, ‘DIRECTION’]

[Related references](INDEX.md).
