# bpy.types.GeometryNodeTrimCurve: properties

## GeometryNodeTrimCurve(GeometryNode)

### GeometryNodeTrimCurve(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeTrimCurve ( GeometryNode )

Cuts curves down by discarding sections from either their start or their end.
mode

Which method locates the cut points on each trimmed spline (default 'FACTOR' )

- FACTOR
Factor – Locate the new endpoints as a fraction of how long each spline is.

- LENGTH
Length – Locate the new endpoints by measuring a distance from where each spline begins.

Type :

Literal[‘FACTOR’, ‘LENGTH’]

[Related references](INDEX.md).
