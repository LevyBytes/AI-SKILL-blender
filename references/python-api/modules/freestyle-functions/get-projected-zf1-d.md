# freestyle.functions.GetProjectedZF1D

class freestyle.functions. GetProjectedZF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetProjectedZF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a GetProjectedZF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the projected Z 3D coordinate of an Interface1D.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The projected Z 3D coordinate of an Interface1D.

Return type :

float

[Related references](INDEX.md).
