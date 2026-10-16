# freestyle.types.SVertexIterator

class freestyle.types. SVertexIterator 

Class hierarchy: Iterator > SVertexIterator

Provides an iterator over the SVertex of a ViewEdge. You obtain an SVertexIterator instance from a ViewEdge by calling verticesBegin() or verticesEnd().
__init__ ( ) 

__init__ ( brother )
__init__ ( vertex , begin , previous_edge , next_edge , t )

Constructs an SVertexIterator with the default constructor, the copy constructor,

or the overload that begins iterating from a given SVertex object vertex.

Parameters :

- brother (SVertexIterator) – An SVertexIterator object.

- vertex (SVertex) – The SVertex from which the iterator starts iteration.

- begin (SVertex) – The first SVertex of a ViewEdge.

- previous_edge (FEdge) – The previous FEdge coming to vertex.

- next_edge (FEdge) – The next FEdge going out from vertex.

- t ( float ) – The curvilinear abscissa at vertex.
object 

Whatever SVertex this iterator is sitting on right now.

Type :

SVertex
t 

The curvilinear abscissa of the current point.

Type :

float
u 

The point parameter at the current point in the 1D element (0 <= u <= 1).

Type :

float

[Related references](INDEX.md).
