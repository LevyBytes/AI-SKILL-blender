# bpy.types.GeometryNodeSampleIndex: properties

## GeometryNodeSampleIndex(GeometryNode)

### GeometryNodeSampleIndex(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSampleIndex ( GeometryNode )

Read values out of particular elements of a geometry
clamp

Restrict indices to the bounds of the attribute domain rather than returning a default value when an index is invalid (default False)

Type :

bool
data_type

(default 'FLOAT' )

Type :

Literal[Attribute Type Items]
domain

(default 'POINT' )

Type :

Literal[Attribute Domain Items]

[Related references](INDEX.md).
