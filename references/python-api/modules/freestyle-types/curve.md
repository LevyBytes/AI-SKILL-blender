# freestyle.types.Curve

class freestyle.types. Curve 

Class hierarchy: Interface1D > Curve

Serves as the parent type for curves assembled from CurvePoints. The vertices a curve starts from are SVertex instances, and a Chain is simply a particular kind of Curve.
__init__ ( ) 

__init__ ( brother )
__init__ ( id )

Constructs a FrsCurve, either with the default constructor, by copying another, or starting from an Id.

Parameters :

- brother (Curve) – A Curve object.

- id (Id) – An Id object.
push_vertex_back ( vertex ) 

Appends one vertex onto the tail end of the Curve.

Parameters :

vertex (SVertex | CurvePoint) – A vertex object.
push_vertex_front ( vertex ) 

Prepends one vertex at the head of the Curve.

Parameters :

vertex (SVertex | CurvePoint) – A vertex object.
is_empty 

Reports True while the Curve still holds no Vertex.

Type :

bool
segments_size 

How many segments the polyline forming the Curve is divided into.

Type :

int

[Related references](INDEX.md).
