# freestyle.shaders.TipRemoverShader

class freestyle.shaders. TipRemoverShader 

Class hierarchy: freestyle.types.StrokeShader > TipRemoverShader

[Geometry shader]
__init__ ( tip_length ) 

Builds a TipRemoverShader object.

Parameters :

tip_length ( float ) – How long a piece of stroke to strip off at each end.
shade ( stroke ) 

Strips off the stroke's ends.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
