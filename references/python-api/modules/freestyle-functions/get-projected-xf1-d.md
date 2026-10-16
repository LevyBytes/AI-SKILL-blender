# freestyle.functions.GetProjectedXF1D

class freestyle.functions. GetProjectedXF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetProjectedXF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a GetProjectedXF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the projected X 3D coordinate of an Interface1D.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The projected X 3D coordinate of an Interface1D.

Return type :

float

[Related references](INDEX.md).
