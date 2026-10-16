# freestyle.shaders.CalligraphicShader

class freestyle.shaders. CalligraphicShader 

Class hierarchy: freestyle.types.StrokeShader > CalligraphicShader

[Thickness Shader]
__init__ ( thickness_min , thickness_max , orientation , clamp ) 

Builds a CalligraphicShader object.

Parameters :

- thickness_min ( float ) – The thinnest thickness, taken along the direction at right angles to the main one.

- thickness_max ( float ) – The thickest thickness, taken along the main direction.

- orientation (mathutils.Vector) – A 2D vector that points along the principal direction.

- clamp ( bool ) – When true, strokes come out black wherever their direction lands within -90 to 90 degrees of that principal direction and white elsewhere; when false, they stay black throughout.
shade ( stroke ) 

Sets thicknesses on the stroke's vertices so the line looks calligraphic — at its heaviest along one chosen direction, at its lightest along the direction square to it, and blended through the range in between.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
