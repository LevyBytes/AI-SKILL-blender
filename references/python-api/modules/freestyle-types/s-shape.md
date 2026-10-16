# freestyle.types.SShape

class freestyle.types. SShape 

Represents a feature shape. It is the collection of feature elements drawn from one identified input shape.
__init__ ( ) 

__init__ ( brother )

Constructs an SShape with either the default constructor or the copy constructor.

Parameters :

brother (SShape) – An SShape object.
add_edge ( edge ) 

Appends an FEdge onto the list of FEdges.

Parameters :

edge (FEdge) – An FEdge object.
add_vertex ( vertex ) 

Appends an SVertex onto this Shape's list of SVertex. The SVertex's SShape attribute is also pointed at this SShape.

Parameters :

vertex (SVertex) – An SVertex object.
compute_bbox ( ) 

Compute the bbox of the SShape.
bbox 

The bounding box of the SShape.

Type :

BBox
edges 

The list of edges that make up this SShape.

Type :

List of FEdge
id 

The Id of this SShape.

Type :

Id
name 

The name of the SShape.

Type :

str
vertices 

The list of vertices that make up this SShape.

Type :

List of SVertex

[Related references](INDEX.md).
