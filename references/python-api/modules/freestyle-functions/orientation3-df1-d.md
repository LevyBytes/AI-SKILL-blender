# freestyle.functions.Orientation3DF1D

class freestyle.functions. Orientation3DF1D 

Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec3f > Orientation3DF1D
__init__ ( integration_type = IntegrationType.MEAN ) 

Builds an Orientation3DF1D object.

Parameters :

integration_type (freestyle.types.IntegrationType) – Which integration scheme collapses a collection of values down to one.
__call__ ( inter ) 

Yields the 3D orientation of the Interface1D.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

The 3D orientation of the Interface1D.

Return type :

[Related references](INDEX.md).
