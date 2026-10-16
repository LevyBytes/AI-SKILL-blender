# freestyle.types.ViewVertex

class freestyle.types. ViewVertex 

Class hierarchy: Interface0D > ViewVertex

Represents a view vertex. A view vertex is a feature vertex matching a point of the image graph where an edge's traits (such as nature and visibility) may shift. A ViewVertex comes in two forms: a TVertex marks where two ViewEdges cross, whereas a NonTVertex maps onto one of the original input mesh's own vertices (as happens with features like corners). The class therefore branches into two subclasses, TVertex and NonTVertex.
edges_begin ( ) 

Hands back an iterator over the ViewEdges arriving at or leaving this ViewVertex, sitting on the list's first ViewEdge. The orientedViewEdgeIterator lets you walk these ViewEdges in CCW order and read the orientation (incoming or outgoing) of each one.

Returns :

An orientedViewEdgeIterator pointing to the first ViewEdge.

Return type :

orientedViewEdgeIterator
edges_end ( ) 

Hands back an orientedViewEdgeIterator over the ViewEdges around this ViewVertex, sitting just past the last ViewEdge.

Returns :

An orientedViewEdgeIterator pointing after the last ViewEdge.

Return type :

orientedViewEdgeIterator
edges_iterator ( edge ) 

Hands back an orientedViewEdgeIterator sitting on the ViewEdge supplied as the argument.

Parameters :

edge (ViewEdge) – A ViewEdge object.

Returns :

An orientedViewEdgeIterator pointing to the given ViewEdge.

Return type :

orientedViewEdgeIterator
nature 

The nature of this ViewVertex.

Type :

Nature

[Related references](INDEX.md).
