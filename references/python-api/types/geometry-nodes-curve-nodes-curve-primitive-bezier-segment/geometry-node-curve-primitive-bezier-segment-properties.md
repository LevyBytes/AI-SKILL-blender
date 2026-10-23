# bpy.types.GeometryNodeCurvePrimitiveBezierSegment: properties

## GeometryNodeCurvePrimitiveBezierSegment(GeometryNode)

### GeometryNodeCurvePrimitiveBezierSegment(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurvePrimitiveBezierSegment ( GeometryNode )

Produce a 2D Bézier spline out of the supplied control points and their handles.
mode

Selects how the control handles are worked out (default 'POSITION' )

- POSITION
Position – Treat the start and end handles as fixed positions.

- OFFSET
Offset – Treat the start and end handles as offsets measured from the spline's control points.

Type :

Literal[‘POSITION’, ‘OFFSET’]

[Related references](INDEX.md).
