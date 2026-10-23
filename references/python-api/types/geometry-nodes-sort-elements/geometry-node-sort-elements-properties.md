# bpy.types.GeometryNodeSortElements: properties

## GeometryNodeSortElements(GeometryNode)

### GeometryNodeSortElements(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSortElements ( GeometryNode ) 

Reorders the elements of a geometry, giving them new indices.
domain 

(default 'POINT' )

- POINT
Point – An attribute carried on points.

- EDGE
Edge – An attribute carried on mesh edges.

- FACE
Face – An attribute carried on mesh faces.

- CURVE
Spline – An attribute carried on splines.

- INSTANCE
Instance – An attribute carried on instances.

Type :

Literal[‘POINT’, ‘EDGE’, ‘FACE’, ‘CURVE’, ‘INSTANCE’]

[Related references](INDEX.md).
