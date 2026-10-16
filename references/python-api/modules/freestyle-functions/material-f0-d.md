# freestyle.functions.MaterialF0D

class freestyle.functions. MaterialF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DMaterial > MaterialF0D
__init__ ( ) 

Builds a MaterialF0D object.
__call__ ( it ) 

Yields the material of the object taken at the freestyle.types.Interface0D referenced by the Interface0DIterator. That reading can be ambiguous (for a freestyle.types.TVertex, say). To resolve it, the functor leans on the context supplied by the 1D element that the Interface0DIterator sits on, and when two distinct materials sit on either side of the point it arbitrarily picks the material of the face lying to the left as the 1D element is followed. Tricky cases can still arise, however, and anyone needing to handle them a particular way should write their own getMaterial functor.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The material of the object evaluated at the pointed
Interface0D.

Return type :

[Related references](INDEX.md).
