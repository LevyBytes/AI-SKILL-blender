# freestyle.types.StrokeVertex

class freestyle.types. StrokeVertex 

Class hierarchy: Interface0D > CurvePoint > StrokeVertex

Represents a stroke vertex.
__init__ ( ) 

__init__ ( brother )
__init__ ( first_vertex , second_vertex , t3d )

__init__ ( point )
__init__ ( svertex )

__init__ ( svertex , attribute )

Constructs a StrokeVertex with the default constructor, the copy constructor, from a pair of StrokeVertex plus an interpolation parameter, from a CurvePoint, from an SVertex, or from an SVertex together with a StrokeAttribute object.

Parameters :

- brother (StrokeVertex) – A StrokeVertex object.

- first_vertex (StrokeVertex) – The first StrokeVertex.

- second_vertex (StrokeVertex) – The second StrokeVertex.

- t3d ( float ) – An interpolation parameter.

- point (CurvePoint) – A CurvePoint object.

- svertex (SVertex) – An SVertex object.

- svertex – An SVertex object.

- attribute (StrokeAttribute) – A StrokeAttribute object.
attribute 

StrokeAttribute for this StrokeVertex.

Type :

StrokeAttribute
curvilinear_abscissa 

Curvilinear abscissa of this StrokeVertex in the Stroke.

Type :

float
point 

2D point coordinates.

Type :
stroke_length 

Stroke length, though it is merely a figure cached by the StrokeVertex and altering it leaves the actual stroke length untouched.

Type :

float
u 

Curvilinear abscissa of this StrokeVertex in the Stroke.

Type :

float

[Related references](INDEX.md).
