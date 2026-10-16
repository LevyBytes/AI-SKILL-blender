# freestyle.shaders.IncreasingThicknessShader

class freestyle.shaders. IncreasingThicknessShader 

Class hierarchy: freestyle.types.StrokeShader > IncreasingThicknessShader

[Thickness shader]
__init__ ( thickness_A , thickness_B ) 

Builds an IncreasingThicknessShader object.

Parameters :

- thickness_A ( float ) – The first thickness value.

- thickness_B ( float ) – The second thickness value.
shade ( stroke ) 

Sets thicknesses that climb from value A up to value B between the first vertex and the midpoint vertex, then drop back from B to A between that midpoint and the last vertex, with thickness interpolated linearly from A to B.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
