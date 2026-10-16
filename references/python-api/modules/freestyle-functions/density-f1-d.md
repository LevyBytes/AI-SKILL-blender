# freestyle.functions.DensityF1D

class freestyle.functions. DensityF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > DensityF1D
__init__ ( sigma = 2.0 , integration_type = IntegrationType.MEAN , sampling = 2.0 ) 

Builds a DensityF1D object.

Parameters :

- sigma ( float ) – The same sigma that DensityF0D takes, fixing the window size applied on each density lookup.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.

- sampling ( float ) – How finely the chain gets sampled: the matching 0D function fires at every sample point and the per-point results are merged into one value via the scheme named by integration_type.
__call__ ( inter ) 

Yields the density measured for an Interface1D. Points are sampled along the Interface1D (through the freestyle.functions.DensityF0D functor) at a sampling rate you choose, and the per-point densities are then folded into one figure by an integration method you choose.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The density evaluated for an Interface1D.

Return type :

float

[Related references](INDEX.md).
