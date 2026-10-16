# freestyle.functions.DensityF0D

class freestyle.functions. DensityF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > DensityF0D
__init__ ( sigma = 2.0 ) 

Builds a DensityF0D object.

Parameters :

sigma ( float ) – The gaussian sigma, i.e. the X position at which the gaussian drops to 0.5; this in turn fixes the window size (larger means smoother).
__call__ ( it ) 

Yields the density of the resulting image taken at the freestyle.types.Interface0D referenced by the Interface0DIterator. The measurement uses a square window of pixels centred on the sample point, integrating those values with a gaussian.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The density of the image evaluated at the pointed
Interface0D.

Return type :

float

[Related references](INDEX.md).
