# bpy.ops.mesh.edge_split

bpy.ops.mesh. edge_split ( * , type = 'EDGE' )

Partition chosen edges such that each neighboring polygon receives its own copy

Parameters :

type ( Literal [ 'EDGE' , 'VERT' ] ) – Type, Method to use for splitting (optional)

- EDGE
Faces by Edges – Split faces along selected edges.

- VERT
Faces & Edges by Vertices – Split faces and edges connected to selected vertices.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
