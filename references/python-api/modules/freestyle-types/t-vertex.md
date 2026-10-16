# freestyle.types.TVertex

class freestyle.types. TVertex 

Class hierarchy: Interface0D > ViewVertex > TVertex

Represents a T vertex, that is, a crossing of two edges. It references two SVertex and four ViewEdges. Of those ViewEdges, two are front and two are back, and a front edge conceals part of a back edge. Among the back pair, one carries invisibility N while the other carries invisibility N+1.
__init__ ( ) 

Default constructor.
get_mate ( viewedge ) 

Hands back the mate edge of the ViewEdge passed in. Given frontEdgeA the result is frontEdgeB; given frontEdgeB the result is frontEdgeA; the back edges work the same way.

Parameters :

viewedge (ViewEdge) – A ViewEdge object.

Returns :

The mate edge of the given ViewEdge.

Return type :

ViewEdge
get_svertex ( fedge ) 

Hands back whichever of the two SVertex is part of the supplied FEdge.

Parameters :

fedge (FEdge) – An FEdge object.

Returns :

The SVertex belonging to the given FEdge.

Return type :

SVertex
back_svertex 

The SVertex positioned further from the viewpoint.

Type :

SVertex
front_svertex 

The SVertex positioned nearer to the viewpoint.

Type :

SVertex
id 

The Id of this TVertex.

Type :

Id

[Related references](INDEX.md).
