# freestyle.functions.GetCompleteViewMapDensityF1D

class freestyle.functions. GetCompleteViewMapDensityF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetCompleteViewMapDensityF1D
__init__ ( level , integration_type = IntegrationType.MEAN , sampling = 2.0 ) 

Builds a GetCompleteViewMapDensityF1D object.

Parameters :

- level ( int ) – Which level of the pyramid the pixel gets read from.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.

- sampling ( float ) – How finely the chain gets sampled: the matching 0D function fires at every sample point and the per-point results are merged into one value via the scheme named by integration_type.
__call__ ( inter ) 

Yields the density measured for an Interface1D within the complete viewmap image. Points are sampled along the Interface1D (through the freestyle.functions.ReadCompleteViewMapPixelF0D functor) and then folded into one figure by an integration method you choose.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The density evaluated for the Interface1D in the complete
viewmap image.

Return type :

float

[Related references](INDEX.md).
