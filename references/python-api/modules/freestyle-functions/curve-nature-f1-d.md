# freestyle.functions.CurveNatureF1D

class freestyle.functions. CurveNatureF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DEdgeNature > CurveNatureF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds a CurveNatureF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the nature of the Interface1D — silhouette, ridge, crease, and the like. Unless the Interface1D happens to be a freestyle.types.ViewEdge, the answer can be ambiguous, because the Interface1D may have been assembled from several 1D elements of differing natures, and an integration scheme such as MEAN can then produce a meaningless figure.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The nature of the Interface1D.

Return type :

[Related references](INDEX.md).
