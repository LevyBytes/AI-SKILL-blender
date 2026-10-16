# bpy.types.ThemeFontStyle: properties

## ThemeFontStyle(bpy_struct)

### ThemeFontStyle(bpy_struct)

base class — bpy_struct
class bpy.types. ThemeFontStyle ( bpy_struct )

Styling for Font
character_weight

How heavy the glyphs are drawn; the 100-900 scale puts 400 at regular weight. (in [100, 900], default 400)

Type :

int
points

Size of the font, measured in points (in [6, 32], default 0.0)

Type :

float
shadow

Which shadow style to use (0 disables it, 3 and 5 blur, 6 outlines) (in [0, 6], default 0)

Type :

int
shadow_alpha

(in [0, 1], default 0.0)

Type :

float
shadow_offset_x

How far the shadow shifts, in pixels (in [-10, 10], default 0)

Type :

int
shadow_offset_y

How far the shadow shifts, in pixels (in [-10, 10], default 0)

Type :

int
shadow_value

Gray level used for the shadow color (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
