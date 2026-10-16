# freestyle.shaders.IncreasingColorShader

class freestyle.shaders. IncreasingColorShader 

Class hierarchy: freestyle.types.StrokeShader > IncreasingColorShader

[Color shader]
__init__ ( red_min , green_min , blue_min , alpha_min , red_max , green_max , blue_max , alpha_max ) 

Builds an IncreasingColorShader object.

Parameters :

- red_min ( float ) – The first color red component.

- green_min ( float ) – The first color green component.

- blue_min ( float ) – The first color blue component.

- alpha_min ( float ) – The first color alpha value.

- red_max ( float ) – The second color red component.

- green_max ( float ) – The second color green component.

- blue_max ( float ) – The second color blue component.

- alpha_max ( float ) – The second color alpha value.
shade ( stroke ) 

Paints the stroke with a shifting color. You give two colors, A and B; the stroke's color moves linearly from A to B across the span from the first vertex to the last.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
