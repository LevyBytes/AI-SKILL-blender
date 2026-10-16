# freestyle.functions.VertexOrientation3DF0D

class freestyle.functions. VertexOrientation3DF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec3f > VertexOrientation3DF0D
__init__ ( ) 

Builds a VertexOrientation3DF0D object.
__call__ ( it ) 

Yields a 3-component vector holding the 3D oriented tangent of the 1D element that the freestyle.types.Interface0D referenced by the Interface0DIterator belongs to. That oriented tangent is taken at the pointed Interface0D.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The 3D oriented tangent to the 1D element evaluated at the
pointed Interface0D.

Return type :

[Related references](INDEX.md).
