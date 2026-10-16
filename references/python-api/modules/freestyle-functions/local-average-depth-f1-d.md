# freestyle.functions.LocalAverageDepthF1D

class freestyle.functions. LocalAverageDepthF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > LocalAverageDepthF1D
__init__ ( sigma , integration_type = IntegrationType.MEAN ) 

Builds a LocalAverageDepthF1D object.

Parameters :

- sigma ( float ) – The same sigma that DensityF0D uses, fixing the window size applied on each density lookup.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the mean depth measured for an Interface1D. Points are sampled along the Interface1D (through the freestyle.functions.LocalAverageDepthF0D functor) at a sampling rate you choose, and the results are then folded into one figure by an integration method you choose.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The average depth evaluated for the Interface1D.

Return type :

float

[Related references](INDEX.md).
