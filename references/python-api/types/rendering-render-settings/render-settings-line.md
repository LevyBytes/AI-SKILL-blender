# bpy.types.RenderSettings: line_thickness, line_thickness_mode

line_thickness

Thickness of lines, measured in pixels (in [0, 10000], default 1.0)

Type :

float
line_thickness_mode

How Freestyle line drawing interprets line thickness (default 'ABSOLUTE' )

- ABSOLUTE
Absolute – Treat the line thickness value as a literal pixel count.

- RELATIVE
Relative – Scale the unit line thickness by how the current vertical image resolution compares to 480 pixels.

Type :

Literal[‘ABSOLUTE’, ‘RELATIVE’]

[Related references](INDEX.md).
