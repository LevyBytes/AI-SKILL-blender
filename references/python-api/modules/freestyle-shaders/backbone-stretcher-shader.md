# freestyle.shaders.BackboneStretcherShader

class freestyle.shaders. BackboneStretcherShader 

Class hierarchy: freestyle.types.StrokeShader > BackboneStretcherShader

[Geometry shader]
__init__ ( amount = 2.0 ) 

Builds a BackboneStretcherShader object.

Parameters :

amount ( float ) – How much stretching to apply.
shade ( stroke ) 

Extends the stroke at each of its two ends, along the matching directions v(1)v(0) and v(n-1)v(n).

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
