# bpy.types.GeometryNodeMeshToCurve: properties

## GeometryNodeMeshToCurve(GeometryNode)

### GeometryNodeMeshToCurve(GeometryNode) 

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMeshToCurve ( GeometryNode ) 

Turn a mesh into a curve.
mode 

(default 'EDGES' )

- EDGES
Edges – Turn the mesh's edges into curve segments, carrying attributes over to the curve points..

- FACES
Faces – Turn every mesh face into a closed curve, carrying face attributes over to the curves..

Type :

Literal[‘EDGES’, ‘FACES’]

[Related references](INDEX.md).
