# bpy.types.GeometryNodeScaleElements: properties

## GeometryNodeScaleElements(GeometryNode)

### GeometryNodeScaleElements(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeScaleElements ( GeometryNode )

Resize connected groups of edges and faces
domain

Element type to transform (default 'FACE' )

- FACE
Face – Resize faces one at a time, or as connected face islands.

- EDGE
Edge – Resize edges one at a time, or as connected edge islands.

Type :

Literal[‘FACE’, ‘EDGE’]

[Related references](INDEX.md).
