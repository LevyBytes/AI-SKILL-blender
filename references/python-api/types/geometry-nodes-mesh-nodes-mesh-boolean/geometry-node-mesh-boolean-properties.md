# bpy.types.GeometryNodeMeshBoolean: properties

## GeometryNodeMeshBoolean(GeometryNode)

### GeometryNodeMeshBoolean(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMeshBoolean ( GeometryNode ) 

Carve, subtract, or combine two or more mesh inputs against each other.
operation 

(default 'INTERSECT' )

- INTERSECT
Intersect – Retain only the region shared by every operand.

- UNION
Union – Bring the meshes together additively.

- DIFFERENCE
Difference – Bring the meshes together subtractively.

Type :

Literal[‘INTERSECT’, ‘UNION’, ‘DIFFERENCE’]
solver 

(default 'FLOAT' )

- EXACT
Exact – A slower option that handles coplanar faces most accurately.

- FLOAT
Float – A lightweight, fast option that cannot handle overlapping geometry.

- MANIFOLD
Manifold – The quickest option, limited to manifold meshes but producing cleaner output.

Type :

Literal[‘EXACT’, ‘FLOAT’, ‘MANIFOLD’]

[Related references](INDEX.md).
