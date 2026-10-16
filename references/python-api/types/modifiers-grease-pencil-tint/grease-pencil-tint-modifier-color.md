# bpy.types.GreasePencilTintModifier: color, color_mode, color_ramp

color

Color used for tinting (array of 3 items, in [0, 1], default (1.0, 1.0, 1.0))

Type :

mathutils.Color
color_mode

Attributes to modify (default 'BOTH' )

- BOTH
Stroke & Fill – Affect the colors of both fill and stroke.

- STROKE
Stroke – Affect the stroke color alone.

- FILL
Fill – Affect the fill color alone.

Type :

Literal['BOTH', 'STROKE', 'FILL']
color_ramp

Gradient tinting colors (readonly)

Type :

ColorRamp

[Related references](INDEX.md).
