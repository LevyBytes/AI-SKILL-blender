# freestyle.functions.GetOccludersF0D

class freestyle.functions. GetOccludersF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVectorViewShape > GetOccludersF0D
__init__ ( ) 

Builds a GetOccludersF0D object.
__call__ ( it ) 

Yields the set of freestyle.types.ViewShape that occlude the freestyle.types.Interface0D referenced by the Interface0DIterator.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

A list of ViewShape objects occluding the pointed
Interface0D.

Return type :

list[freestyle.types.ViewShape]

[Related references](INDEX.md).
