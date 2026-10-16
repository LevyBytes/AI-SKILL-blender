# freestyle.functions.GetViewMapGradientNormF0D

class freestyle.functions. GetViewMapGradientNormF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > GetViewMapGradientNormF0D
__init__ ( level ) 

Builds a GetViewMapGradientNormF0D object.

Parameters :

level ( int ) – Which level of the pyramid the pixel gets read from.
__call__ ( it ) 

Yields how large the gradient of the global viewmap density image is.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The norm of the gradient of the global viewmap density
image.

Return type :

float

[Related references](INDEX.md).
