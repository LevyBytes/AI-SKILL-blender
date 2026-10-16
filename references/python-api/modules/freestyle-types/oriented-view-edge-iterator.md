# freestyle.types.orientedViewEdgeIterator

class freestyle.types. orientedViewEdgeIterator 

Class hierarchy: Iterator > orientedViewEdgeIterator

Provides an iterator over the oriented ViewEdges surrounding a ViewVertex. It supports a CCW walk within the image plane. An orientedViewEdgeIterator instance can come only from a ViewVertex, obtained by calling edges_begin() or edges_end().
__init__ ( ) 

__init__ ( iBrother )

Constructs an orientedViewEdgeIterator with either the default constructor or the copy constructor.

Parameters :

iBrother (orientedViewEdgeIterator) – An orientedViewEdgeIterator object.
object 

The oriented ViewEdge this iterator is sitting on right now, given as a tuple pairing the pointed ViewEdge with a boolean. A true boolean marks the ViewEdge as incoming.

Type :

tuple[ViewEdge, bool]

[Related references](INDEX.md).
