# bpy.types.GeometryNodeDeleteGeometry: properties

## GeometryNodeDeleteGeometry(GeometryNode)

### GeometryNodeDeleteGeometry(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeDeleteGeometry ( GeometryNode )

Strip out the chosen elements from a geometry.
domain

Picks the domain the deletion runs on (default 'POINT' )

Type :

Literal[Attribute Domain Without Corner Items]
mode

Picks which parts of the mesh component get removed (default 'ALL' )

Type :

Literal[‘ALL’, ‘`EDGE_FACE`’, ‘`ONLY_FACE`’]

[Related references](INDEX.md).
