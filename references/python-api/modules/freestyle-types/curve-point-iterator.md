# freestyle.types.CurvePointIterator

class freestyle.types. CurvePointIterator 

Class hierarchy: Iterator > CurvePointIterator

Provides an iterator that walks along a curve and can step past the original vertices. At each position a CurvePoint is created and exposed through the .object attribute.
__init__ ( ) 

__init__ ( brother )
__init__ ( step = 0.0 )

Constructs a CurvePointIterator with the default constructor, the copy constructor, or the overload taking a step.

Parameters :

- brother (CurvePointIterator) – A CurvePointIterator object.

- step ( float ) – The spacing at which the curve gets resampled. A value of zero turns resampling off, so the iterator only visits the original vertices.
object 

Whatever CurvePoint this iterator is sitting on right now.

Type :

CurvePoint
t 

The curvilinear abscissa of the current point.

Type :

float
u 

The point parameter at the current point in the stroke (0 <= u <= 1).

Type :

float

[Related references](INDEX.md).
