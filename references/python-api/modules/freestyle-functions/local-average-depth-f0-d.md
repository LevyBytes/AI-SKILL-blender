# freestyle.functions.LocalAverageDepthF0D

class freestyle.functions. LocalAverageDepthF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > LocalAverageDepthF0D
__init__ ( mask_size = 5.0 ) 

Builds a LocalAverageDepthF0D object.

Parameters :

mask_size ( float ) – How large the mask is.
__call__ ( it ) 

Yields the mean depth in the neighbourhood of the freestyle.types.Interface0D referenced by the Interface0DIterator. It comes from sampling the depth buffer across a window around that point.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.
Returns :

The average depth around the pointed Interface0D.

Return type :

float

[Related references](INDEX.md).
