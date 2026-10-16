# bpy.types.TransformConstraint: mix_mode, mix_mode_rot, mix_mode_scale

mix_mode 

How the new location is blended with the original (default 'ADD' )

- REPLACE
Replace – Replace component values.

- ADD
Add – Add component values together.

Type :

Literal[‘REPLACE’, ‘ADD’]
mix_mode_rot 

How the new rotation is blended with the original (default 'ADD' )

- REPLACE
Replace – Replace component values.

- ADD
Add – Add component values together.

- BEFORE
Before Original – Apply new rotation before original, as if it was on a parent.

- AFTER
After Original – Apply new rotation after original, as if it was on a child.

Type :

Literal[‘REPLACE’, ‘ADD’, ‘BEFORE’, ‘AFTER’]
mix_mode_scale 

How the new scale is blended with the original (default 'REPLACE' )

- REPLACE
Replace – Replace component values.

- MULTIPLY
Multiply – Multiply component values together.

Type :

Literal[‘REPLACE’, ‘MULTIPLY’]

[Related references](INDEX.md).
