# freestyle.types.StrokeVertexIterator

class freestyle.types. StrokeVertexIterator 

Class hierarchy: Iterator > StrokeVertexIterator

Provides an iterator built to traverse the StrokeVertex of a Stroke. You get a StrokeVertexIterator instance from a Stroke by calling iter(), stroke_vertices_begin() or stroke_vertices_begin(). It covers the very same vertices an Interface0DIterator would; the distinction lies in object access, since an Interface0DIterator only reaches an Interface0D while you may need the more specific StrokeVertex type. For that case a StrokeVertexIterator is the right choice. To call UnaryFuntion0D-type functions, a StrokeVertexIterator can be turned into an Interface0DIterator by calling Interface0DIterator(it).
__init__ ( ) 

__init__ ( brother )

Constructs a StrokeVertexIterator with either the default constructor or the copy constructor.

Parameters :

brother (StrokeVertexIterator) – A StrokeVertexIterator object.
decremented ( ) 

Hands back a copy of a StrokeVertexIterator that has been stepped back.

Returns :

A StrokeVertexIterator pointing the previous StrokeVertex.

Return type :

StrokeVertexIterator
incremented ( ) 

Hands back a copy of a StrokeVertexIterator that has been stepped forward.

Returns :

A StrokeVertexIterator pointing the next StrokeVertex.

Return type :

StrokeVertexIterator
reversed ( ) 

Hands back a StrokeVertexIterator that runs through the stroke vertices in reverse order.

Returns :

A StrokeVertexIterator traversing stroke vertices backward.

Return type :

StrokeVertexIterator
at_last 

Set to True while the iterator sits on the final valid element. To test the opposite end (the first valid element), check it.is_begin instead.

Type :

bool
object 

Whatever StrokeVertex this iterator is sitting on right now.

Type :

StrokeVertex
t 

The curvilinear abscissa of the current point.

Type :

float
u 

The point parameter at the current point in the stroke (0 <= u <= 1).

Type :

float

[Related references](INDEX.md).
