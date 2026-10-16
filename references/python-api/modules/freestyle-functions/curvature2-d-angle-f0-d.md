# freestyle.functions.Curvature2DAngleF0D

class freestyle.functions. Curvature2DAngleF0D 

Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble > Curvature2DAngleF0D
__init__ ( ) 

Builds a Curvature2DAngleF0D object.
__call__ ( it ) 

Yields a real number expressing, as an angle, the 2D curvature of the 1D element that the freestyle.types.Interface0D referenced by the Interface0DIterator sits on. That 2D curvature is measured at the Interface0D itself.

Parameters :

it (freestyle.types.Interface0DIterator) – An Interface0DIterator object.

Returns :

The 2D curvature of the 1D element evaluated at the
pointed Interface0D.

Return type :

float

[Related references](INDEX.md).
