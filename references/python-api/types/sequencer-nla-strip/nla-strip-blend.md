# bpy.types.NlaStrip: blend_in, blend_out, blend_type

blend_in

Count of frames at the strip start over which influence fades up (in [-inf, inf], default 0.0)

Type :

float
blend_out

(in [-inf, inf], default 0.0)

Type :

float
blend_type

How this strip's output is merged into the running result (default 'REPLACE' )

- REPLACE
Replace – The strip values replace the accumulated results by amount specified by influence.

- COMBINE
Combine – The strip values are combined with accumulated results by appropriately using addition, multiplication, or quaternion math, based on channel type.

- ADD
Add – Weighted result of strip is added to the accumulated results.

- SUBTRACT
Subtract – Weighted result of strip is removed from the accumulated results.

- MULTIPLY
Multiply – Weighted result of strip is multiplied with the accumulated results.

Type :

Literal[‘REPLACE’, ‘COMBINE’, ‘ADD’, ‘SUBTRACT’, ‘MULTIPLY’]

[Related references](INDEX.md).
