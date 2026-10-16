# freestyle.functions.ZDiscontinuityF1D

class freestyle.functions. ZDiscontinuityF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > ZDiscontinuityF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a ZDiscontinuityF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields a real number for the gap between an Interface1D and the shape sitting behind it (the occludee). That gap is measured in camera space and rescaled into the 0-to-1 range, so when the shape the Interface1D belongs to occludes nothing, the result is 1.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The normalized distance between the Interface1D and the occludee.

Return type :

float

[Related references](INDEX.md).
