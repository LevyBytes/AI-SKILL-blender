# freestyle.functions.Curvature2DAngleF1D

class freestyle.functions. Curvature2DAngleF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > Curvature2DAngleF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a Curvature2DAngleF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields, for an Interface1D, the 2D curvature expressed as an angle.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The 2D curvature as an angle.

Return type :

float

[Related references](INDEX.md).
