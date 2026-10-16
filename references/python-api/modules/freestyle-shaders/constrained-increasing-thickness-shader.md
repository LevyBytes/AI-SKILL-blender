# freestyle.shaders.ConstrainedIncreasingThicknessShader

class freestyle.shaders. ConstrainedIncreasingThicknessShader 

Class hierarchy: freestyle.types.StrokeShader > ConstrainedIncreasingThicknessShader

[Thickness shader]
__init__ ( thickness_min , thickness_max , ratio ) 

Builds a ConstrainedIncreasingThicknessShader object.

Parameters :

- thickness_min ( float ) – The minimum thickness.

- thickness_max ( float ) – The maximum thickness.

- ratio ( float ) – The largest thickness/length ratio that should not be passed.
shade ( stroke ) 

Works like the IncreasingThicknessShader, except it lets you cap the thickness/length ratio so short lines don't come out fat.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
