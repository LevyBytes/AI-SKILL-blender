# bpy.types.GeometryNodeMeshLine: properties

## GeometryNodeMeshLine(GeometryNode)

### GeometryNodeMeshLine(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMeshLine ( GeometryNode ) 

Lay out a row of vertices and link them together with edges.
count_mode 

(default 'TOTAL' )

- TOTAL
Count – Give the total vertex count to produce.

- RESOLUTION
Resolution – Give the spacing to leave between vertices.

Type :

Literal[‘TOTAL’, ‘RESOLUTION’]
mode 

(default 'OFFSET' )

- OFFSET
Offset – Give the step taken from one vertex to the following one.

- `END_POINTS`
End Points – Give where the line begins and where it ends.

Type :

Literal[‘OFFSET’, ‘`END_POINTS`’]

[Related references](INDEX.md).
