# freestyle.functions.ReadMapPixelF0D

class freestyle.functions. ReadMapPixelF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat > ReadMapPixelF0D
__init__ ( map_name , level ) 

Builds a ReadMapPixelF0D object.

Parameters :

- map_name ( str ) – Which map gets read, by name.

- level ( int ) – Which level of the pyramid the pixel gets read from.
__call__ ( it ) 

Fetches a pixel out of a map.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

A pixel in a map.

Return type :

float

[Related references](INDEX.md).
