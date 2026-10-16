# freestyle.functions.GetDirectionalViewMapDensityF1D

class freestyle.functions. GetDirectionalViewMapDensityF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetDirectionalViewMapDensityF1D
__init__ ( orientation , level , integration_type = IntegrationType.MEAN , sampling = 2.0 ) 

Builds a GetDirectionalViewMapDensityF1D object.

Parameters :

- orientation ( int ) – Which directional map (by its number) is to be used.

- level ( int ) – Which level of the pyramid the pixel gets read from.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.

- sampling ( float ) – How finely the chain gets sampled: the matching 0D function fires at every sample point and the per-point results are merged into one value via the scheme named by integration_type.
__call__ ( inter ) 

Yields the density measured for an Interface1D inside the steerable viewmaps image. You name explicitly which Directional map applies via the direction. Points are sampled along the Interface1D (through the freestyle.functions.ReadSteerableViewMapPixelF0D functor) and then folded into one figure by an integration method you choose.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

the density evaluated for an Interface1D in of the
steerable viewmaps image.

Return type :

float

[Related references](INDEX.md).
