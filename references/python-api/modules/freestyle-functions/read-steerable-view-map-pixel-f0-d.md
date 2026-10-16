# freestyle.functions.ReadSteerableViewMapPixelF0D

class freestyle.functions. ReadSteerableViewMapPixelF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > ReadSteerableViewMapPixelF0D
__init__ ( orientation , level ) 

Builds a ReadSteerableViewMapPixelF0D object.

Parameters :

- orientation ( int ) – An integer in [0, 4] picking the orientation (E, NE, N, NW) of interest.

- level ( int ) – Which level of the pyramid the pixel gets read from.
__call__ ( it ) 

Fetches a pixel from one of the levels of one of the steerable viewmaps.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

A pixel in one of the level of one of the steerable viewmaps.

Return type :

float

[Related references](INDEX.md).
