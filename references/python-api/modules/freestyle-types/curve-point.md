# freestyle.types.CurvePoint

class freestyle.types. CurvePoint 

Class hierarchy: Interface0D > CurvePoint

Represents one point sitting on a curve. Such a point need not coincide with a curve vertex; it can fall anywhere along a 1D curve. Since every Interface1D rests on ViewEdges, which in turn rest on FEdges, a curve amounts to a polyline strung together from SVertex objects. A CurvePoint is therefore produced by linearly blending two SVertex instances, which lets it act as a virtual point when 0D data is sampled along a curve at some chosen resolution.
__init__ ( ) 

__init__ ( brother )
__init__ ( first_vertex , second_vertex , t2d )

__init__ ( first_point , second_point , t2d )

Constructs a CurvePoint via the default constructor, the copy constructor, or one of the extra overloads. Those overloads accept either a pair of SVertex or a pair of CurvePoint objects together with an interpolation factor.

Parameters :

- brother (CurvePoint) – A CurvePoint object.

- first_vertex (SVertex) – The first SVertex.

- second_vertex (SVertex) – The second SVertex.

- first_point (CurvePoint) – The first CurvePoint.

- second_point (CurvePoint) – The second CurvePoint.

- t2d ( float ) – A 2D interpolation parameter used to linearly interpolate
first_vertex and second_vertex or first_point and second_point.
fedge 

Retrieves the FEdge spanning the two SVertices that the given CurvePoints are made of. This is shorthand for CurvePoint.first_svertex.get_fedge(CurvePoint.second_svertex).

Type :

FEdge
first_svertex 

The first of the two SVertex on which this CurvePoint rests.

Type :

SVertex
second_svertex 

The second of the two SVertex on which this CurvePoint rests.

Type :

SVertex
t2d 

The 2D interpolation parameter.

Type :

float

[Related references](INDEX.md).
