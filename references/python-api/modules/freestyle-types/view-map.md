# freestyle.types.ViewMap

class freestyle.types. ViewMap 

Represents the ViewMap.
__init__ ( ) 

Default constructor.
get_closest_fedge ( x , y ) 

Fetches the FEdge closest to the 2D point given as the arguments.

Parameters :

- x ( float ) – X coordinate of a 2D point.

- y ( float ) – Y coordinate of a 2D point.

Returns :

The FEdge nearest to the specified 2D point.

Return type :

FEdge
get_closest_viewedge ( x , y ) 

Fetches the ViewEdge closest to the 2D point given as the arguments.

Parameters :

- x ( float ) – X coordinate of a 2D point.

- y ( float ) – Y coordinate of a 2D point.

Returns :

The ViewEdge nearest to the specified 2D point.

Return type :

ViewEdge
scene_bbox 

The 3D bounding box of the scene.

Type :

BBox

[Related references](INDEX.md).
