# freestyle.functions.QuantitativeInvisibilityF1D

class freestyle.functions. QuantitativeInvisibilityF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DUnsigned > QuantitativeInvisibilityF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a QuantitativeInvisibilityF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the Quantitative Invisibility of an Interface1D element. When the Interface1D is a freestyle.types.ViewEdge the result is unambiguous, but when it comes out of a chaining operation (chain, stroke) it may comprise several 1D elements whose Quantitative Invisibilities differ.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The Quantitative Invisibility of the Interface1D.

Return type :

int

[Related references](INDEX.md).
