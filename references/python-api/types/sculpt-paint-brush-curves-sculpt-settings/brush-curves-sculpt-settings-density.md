# bpy.types.BrushCurvesSculptSettings: density_add_attempts, density_mode

density_add_attempts

How many tries the Density brush makes at adding a new curve (in [0, inf], default 0)

Type :

int
density_mode

Whether the brush is adding or removing curves (default 'AUTO' )

- AUTO
Auto – Adds or removes curves based on the smallest spacing among the curves beneath the cursor.

- ADD
Add – Inserts new curves between existing ones, respecting the minimum distance.

- REMOVE
Remove – Strips out curves whose roots sit too close together.

Type :

Literal['AUTO', 'ADD', 'REMOVE']

[Related references](INDEX.md).
