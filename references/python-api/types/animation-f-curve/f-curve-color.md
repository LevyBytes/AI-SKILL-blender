# bpy.types.FCurve: color, color_mode

color

The curve's display color in the Graph Editor (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
color_mode

How the F-Curve's Graph Editor color is chosen (default '`AUTO_RAINBOW`' )

- `AUTO_RAINBOW`
Auto Rainbow – Step through the rainbow so that every curve tends to get its own color.

- `AUTO_RGB`
Auto XYZ to RGB – Apply axis colors to transform and color properties, falling back to auto-rainbow elsewhere.

- `AUTO_YRGB`
Auto WXYZ to YRGB – Apply WXYZ axis colors to quaternion/axis-angle rotations, XYZ axis colors to other transform and color properties, and auto-rainbow for everything else.

- CUSTOM
User Defined – Apply a color you picked yourself for the F-Curve.

Type :

Literal[‘`AUTO_RAINBOW`’, ‘`AUTO_RGB`’, ‘`AUTO_YRGB`’, ‘CUSTOM’]

[Related references](INDEX.md).
