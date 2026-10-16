# freestyle.functions.ReadCompleteViewMapPixelF0D

class freestyle.functions. ReadCompleteViewMapPixelF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > ReadCompleteViewMapPixelF0D
__init__ ( level ) 

Builds a ReadCompleteViewMapPixelF0D object.

Parameters :

level ( int ) – Which level of the pyramid the pixel gets read from.
__call__ ( it ) 

Fetches a pixel from one of the levels of the complete viewmap.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

A pixel in one of the level of the complete viewmap.

Return type :

float

[Related references](INDEX.md).
