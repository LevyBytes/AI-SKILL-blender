# freestyle.predicates.ViewMapGradientNormBP1D

class freestyle.predicates. ViewMapGradientNormBP1D 

Class hierarchy: freestyle.types.BinaryPredicate1D > ViewMapGradientNormBP1D
__init__ ( level , integration_type = IntegrationType.MEAN , sampling = 2.0 ) 

Builds a ViewMapGradientNormBP1D object.

Parameters :

- level ( int ) – Which level of the pyramid the pixel gets read from.

- integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.

- sampling ( float ) – How finely the chain gets sampled: GetViewMapGradientNormF0D fires at every sample point and the per-point results are merged into one value via the scheme named by integration_type.
__call__ ( inter1 , inter2 ) 

Comes back true when the Gradient norm Function evaluates higher on inter1 than it does on inter2.

Parameters :

- inter1 (freestyle.types.Interface1D) – The first Interface1D object.

- inter2 (freestyle.types.Interface1D) – The second Interface1D object.

Returns :

True or false.

Return type :

bool

[Related references](INDEX.md).
