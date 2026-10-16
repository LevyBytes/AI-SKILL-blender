# bpy.types.AnimData: action_blend_type

action_blend_type

Approach for merging the Active Action's result with NLA stack output (default 'REPLACE')

- REPLACE
Replace – Stack values replace accumulated results based on influence.

- COMBINE
Combine – Stack values integrate with accumulated results using addition, multiplication, or quaternion operations per channel type.

- ADD
Add – Weighted stack result is summed with accumulated results.

- SUBTRACT
Subtract – Weighted stack result is subtracted from accumulated results.

- MULTIPLY
Multiply – Weighted stack result is multiplied into accumulated results.

Type: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']

[Related references](INDEX.md).
