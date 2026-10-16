# freestyle.predicates.QuantitativeInvisibilityUP1D

class freestyle.predicates. QuantitativeInvisibilityUP1D 

Class hierarchy: freestyle.types.UnaryPredicate1D > QuantitativeInvisibilityUP1D
__init__ ( qi = 0 ) 

Builds a QuantitativeInvisibilityUP1D object.

Parameters :

qi ( int ) – The Quantitative Invisibility you wish the Interface1D to carry.
__call__ ( inter ) 

Comes back true when the Quantitative Invisibility measured at an Interface1D, by way of the freestyle.functions.QuantitativeInvisibilityF1D functor, matches a value you specify.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

True if Quantitative Invisibility equals a user-defined
value.

Return type :

bool

[Related references](INDEX.md).
