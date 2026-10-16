# freestyle.types.Interface0D

class freestyle.types. Interface0D 

Serves as the parent type for every 0D element.
__init__ ( ) 

Default constructor.
get_fedge ( inter ) 

Hands back the FEdge sitting between this 0D element and the one passed in as the argument.

Parameters :

inter (Interface0D) – A 0D element.

Returns :

The FEdge lying between the two 0D elements.

Return type :

FEdge
id 

The Id of this 0D element.

Type :

Id
name 

The name string carried by this 0D element.

Type :

str
nature 

The nature of this 0D element.

Type :

Nature
point_2d 

The 2D point of this 0D element.

Type :
point_3d 

The 3D point of this 0D element.

Type :
projected_x 

The X coordinate of this 0D element's projected 3D point.

Type :

float
projected_y 

The Y coordinate of this 0D element's projected 3D point.

Type :

float
projected_z 

The Z coordinate of this 0D element's projected 3D point.

Type :

float

[Related references](INDEX.md).
