# freestyle.types.SVertex

class freestyle.types. SVertex 

Class hierarchy: Interface0D > SVertex

Represents a vertex of the embedding.
__init__ ( ) 

__init__ ( brother )
__init__ ( point_3d , id )

Constructs an SVertex with the default constructor, the copy constructor, or the overload that builds one from a set of 3D coordinates plus an Id.

Parameters :

- brother (SVertex) – A SVertex object.

- point_3d (mathutils.Vector) – A three-dimensional vector.

- id (Id) – An Id object.
add_fedge ( fedge ) 

Appends an FEdge onto the list of edges leaving this SVertex.

Parameters :

fedge (FEdge) – An FEdge.
add_normal ( normal ) 

Adds a normal into the SVertex's collection of normals. Nothing happens if that same normal is already present.

Parameters :

normal (mathutils.Vector | tuple[float, float, float] | list[float]) – A three-dimensional vector.
curvatures 

Curvature data given as a seven-entry tuple (K1, e1, K2, e2, Kr, er, dKr). Here K1 and K2 are scalars holding the first (maximum) and second (minimum) principal curvatures at this SVertex; e1 and e2 are 3D vectors holding the first and second principal directions, that is, the directions within the normal plane where curvature reaches its largest and smallest values; and Kr, er, and dKr hold this SVertex's radial curvature, radial direction, and the derivative of the radial curvature.

Type :

tuple
id 

The Id of this SVertex.

Type :

Id
normals 

This Vertex's normals as a list. On a sharp surface an SVertex carries precisely one normal, whereas on a smooth surface it may carry any count of normals.

Type :

list of mathutils.Vector
normals_size 

How many distinct normals this SVertex has.

Type :

int
point_2d 

The SVertex's 3D coordinates after projection.

Type :
point_3d 

The SVertex's 3D coordinates.

Type :
viewvertex 

When this SVertex doubles as a ViewVertex, this property points at that ViewVertex; otherwise it is None.

Type :

ViewVertex

[Related references](INDEX.md).
