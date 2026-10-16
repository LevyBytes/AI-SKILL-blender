# freestyle.types.FEdgeSmooth

class freestyle.types. FEdgeSmooth 

Class hierarchy: Interface1D > FEdge > FEdgeSmooth

Describes a smooth edge. Edges of this sort usually cut straight across a face of the input mesh and may be a silhouette, a ridge or valley, or a suggestive contour.
__init__ ( ) 

__init__ ( brother )
__init__ ( first_vertex , second_vertex )

Constructs an FEdgeSmooth using the default constructor, the copy constructor, or from a pair of SVertex.

Parameters :

- brother (FEdgeSmooth) – An FEdgeSmooth object.

- first_vertex (SVertex) – The first SVertex object.

- second_vertex (SVertex) – The second SVertex object.
face_mark 

The face mark of the face that this FEdge cuts across.

Type :

bool
material 

The material of the face that this FEdge cuts across.

Type :

Material
material_index 

The material index of the face that this FEdge cuts across.

Type :

int
normal 

The normal vector of the face that this FEdge cuts across.

Type :

[Related references](INDEX.md).
