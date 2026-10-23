# bpy.types.GeometryNodeMeshToPoints: properties

## GeometryNodeMeshToPoints(GeometryNode)

### GeometryNodeMeshToPoints(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMeshToPoints ( GeometryNode ) 

Build a point cloud out of the vertices of a mesh.
mode 

(default 'VERTICES' )

- VERTICES
Vertices – Spawn one point in the cloud for every chosen vertex.

- EDGES
Edges – Spawn one point in the cloud for every chosen edge.

- FACES
Faces – Spawn one point in the cloud for every chosen face.

- CORNERS
Corners – Spawn one point in the cloud for every chosen face corner.

Type :

Literal[‘VERTICES’, ‘EDGES’, ‘FACES’, ‘CORNERS’]

[Related references](INDEX.md).
