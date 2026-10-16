# bpy.types.Brush: jitter, jitter_absolute, jitter_unit

jitter

Randomly offset the brush position as you paint (in [0, 1000], default 0.0)

Type :

float
jitter_absolute

Randomly offset the brush position in pixels as you paint (in [0, 1000000], default 0)

Type :

int
jitter_unit

Whether jitter is measured in screen space or relative to brush size (default 'VIEW' )

- VIEW
View – Jitter is measured in screen-space pixels.

- BRUSH
Brush – Jitter is measured relative to the brush size.

Type :

Literal['VIEW', 'BRUSH']

[Related references](INDEX.md).
