# freestyle.functions.ZDiscontinuityF0D

class freestyle.functions. ZDiscontinuityF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > ZDiscontinuityF0D
__init__ ( ) 

Builds a ZDiscontinuityF0D object.
__call__ ( it ) 

Yields a real number for the gap between the freestyle.types.Interface0D referenced by the Interface0DIterator and the shape sitting behind it (the occludee). That gap is measured in camera space and rescaled into the 0-to-1 range, so when the shape the Interface0D belongs to occludes nothing, the result is 1.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The normalized distance between the pointed Interface0D
and the occludee.

Return type :

float

[Related references](INDEX.md).
