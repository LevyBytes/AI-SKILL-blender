# freestyle.types.FEdgeSharp

class freestyle.types. FEdgeSharp 

Class hierarchy: Interface1D > FEdge > FEdgeSharp

Describes a sharp FEdge. A sharp FEdge maps onto one of the original edges of the input mesh and may be a silhouette, a crease, or a border. When it is a crease edge it is flanked by two mesh faces, with Face a on its right and Face b on its left. When it is a border edge nothing lies on its right, so Face a comes back as None.
__init__ ( ) 

__init__ ( brother )
__init__ ( first_vertex , second_vertex )

Constructs an FEdgeSharp using the default constructor, the copy constructor, or from a pair of SVertex objects.

Parameters :

- brother (FEdgeSharp) – An FEdgeSharp object.

- first_vertex (SVertex) – The first SVertex object.

- second_vertex (SVertex) – The second SVertex object.
face_mark_left 

The face mark belonging to the face on the left-hand side of the FEdge.

Type :

bool
face_mark_right 

The face mark belonging to the face on the right-hand side of the FEdge. When the FEdge is a border there is no face on the right, so this property comes back as false.

Type :

bool
material_index_left 

The material index of the face on the left-hand side of the FEdge.

Type :

int
material_index_right 

The material index of the face on the right-hand side of the FEdge. When the FEdge is a border there is no Face on its right, so it carries no material.

Type :

int
material_left 

The material of the face on the left-hand side of the FEdge.

Type :

Material
material_right 

The material of the face on the right-hand side of the FEdge. When the FEdge is a border there is no Face on its right, so it carries no material.

Type :

Material
normal_left 

The normal vector of the face on the left-hand side of the FEdge.

Type :
normal_right 

The normal vector of the face on the right-hand side of the FEdge. When the FEdge is a border there is no Face on its right, so it carries no normal.

Type :

[Related references](INDEX.md).
