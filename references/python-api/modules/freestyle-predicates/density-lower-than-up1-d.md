# freestyle.predicates.DensityLowerThanUP1D

class freestyle.predicates. DensityLowerThanUP1D 

Class hierarchy: freestyle.types.UnaryPredicate1D > DensityLowerThanUP1D
__init__ ( threshold , sigma = 2.0 ) 

Builds a DensityLowerThanUP1D object.

Parameters :

- threshold ( float ) – The threshold density value. An Interface1D whose density falls under it is a match.

- sigma ( float ) – The sigma that sets the size of the density evaluation window used by the freestyle.functions.DensityF0D functor.
__call__ ( inter ) 

Comes back true when the density measured for the Interface1D falls below a density value you specify.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

True if the density is lower than a threshold.

Return type :

bool

[Related references](INDEX.md).
