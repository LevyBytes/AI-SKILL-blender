# freestyle.types.Interface0DIterator

class freestyle.types. Interface0DIterator 

Class hierarchy: Iterator > Interface0DIterator

Supplies an iterator that runs over Interface0D elements. Such an iterator is always handed back from a 1D element.
__init__ ( brother ) 

__init__ ( it )

Constructs a nested Interface0DIterator from either the copy constructor or the constructor accepting a Function0D argument.

Parameters :

- brother (Interface0DIterator) – An Interface0DIterator object.

- it (SVertexIterator | CurvePointIterator | StrokeVertexIterator) – An iterator object to be nested.
at_last 

Set to True while the iterator sits on the final valid element. To test the opposite end (the first valid element), check it.is_begin instead.

Type :

bool
object 

Whatever 0D object this iterator is sitting on right now. Keep in mind it may actually be an instance of an Interface0D subclass; for example, when the iterator originated from the Stroke class's vertices_begin() method, the .object property gives back a StrokeVertex object.

Type :

Interface0D or one of its subclasses.
t 

The curvilinear abscissa of the current point.

Type :

float
u 

The point parameter at the current point in the 1D element (0 <= u <= 1).
Type :

float

[Related references](INDEX.md).
