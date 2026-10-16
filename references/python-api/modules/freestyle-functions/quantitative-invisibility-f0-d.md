# freestyle.functions.QuantitativeInvisibilityF0D

class freestyle.functions. QuantitativeInvisibilityF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DUnsigned > QuantitativeInvisibilityF0D
__init__ ( ) 

Builds a QuantitativeInvisibilityF0D object.
__call__ ( it ) 

Yields the quantitative invisibility of the freestyle.types.Interface0D referenced by the Interface0DIterator. That reading can be ambiguous (for a freestyle.types.TVertex, say). The functor tries to clear up the ambiguity by drawing on the context of the 1D element the Interface0D belongs to. Tricky cases can still occur, though, and anyone needing to handle them a particular way should write their own getQIF0D functor.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The quantitative invisibility of the pointed Interface0D.

Return type :

int

[Related references](INDEX.md).
