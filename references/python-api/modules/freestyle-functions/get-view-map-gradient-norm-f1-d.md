# freestyle.functions.GetViewMapGradientNormF1D

class freestyle.functions. GetViewMapGradientNormF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble > GetViewMapGradientNormF1D
__init__ ( level , integration_type = IntegrationType.MEAN , sampling = 2.0 ) 

Builds a GetViewMapGradientNormF1D object.

Parameters :

- level ( int ) – Which level of the pyramid the pixel gets read from.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.

- sampling ( float ) – How finely the chain gets sampled: the matching 0D function fires at every sample point and the per-point results are merged into one value via the scheme named by integration_type.
__call__ ( inter ) 

Yields the ViewMap density for a supplied Interface1D. Each freestyle.types.FEdge has its density taken in whichever steerable freestyle.types.ViewMap matches its orientation.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The density of the ViewMap for a given Interface1D.

Return type :

float

[Related references](INDEX.md).
