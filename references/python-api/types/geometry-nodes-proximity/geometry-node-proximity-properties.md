# bpy.types.GeometryNodeProximity: properties

## GeometryNodeProximity(GeometryNode)

### GeometryNodeProximity(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeProximity ( GeometryNode )

Work out, on the target geometry, the nearest location to each input
target_element

Which kind of element on the target the distance is measured against (default 'FACES' )

- POINTS
Points – Measure how near the input is to the target's points; this option runs faster than the rest.

- EDGES
Edges – Measure how near the input is to the target's edges.

- FACES
Faces – Measure how near the input is to the target's faces.

Type :

Literal[‘POINTS’, ‘EDGES’, ‘FACES’]

[Related references](INDEX.md).
