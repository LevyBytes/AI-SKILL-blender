# freestyle.functions.GetXF1D

class freestyle.functions. GetXF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetXF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a GetXF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the X 3D coordinate of an Interface1D.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The X 3D coordinate of the Interface1D.

Return type :

float

[Related references](INDEX.md).
