# freestyle.functions.ShapeIdF0D

class freestyle.functions. ShapeIdF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DId > ShapeIdF0D
__init__ ( ) 

Builds a ShapeIdF0D object.
__call__ ( it ) 

Yields the freestyle.types.Id of the Shape that the freestyle.types.Interface0D referenced by the Interface0DIterator belongs to. That reading can be ambiguous (for a freestyle.types.TVertex, say). The functor tries to clear up the ambiguity by drawing on the context of the 1D element the Interface0DIterator sits on. Tricky cases can still occur, though, and anyone needing to handle them a particular way should write their own getShapeIdF0D functor.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The Id of the Shape the pointed Interface0D belongs to.

Return type :

[Related references](INDEX.md).
