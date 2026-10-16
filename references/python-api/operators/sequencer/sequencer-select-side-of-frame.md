# bpy.ops.sequencer.select_side_of_frame

bpy.ops.sequencer.select_side_of_frame(*, extend=False, side='LEFT')

Pick pieces in relation to the current picture.

Parameters:

- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- side (Literal['LEFT', 'RIGHT', 'CURRENT']) – Side, (optional)
  - LEFT
    Left – Pick to the left of the current picture.
  - RIGHT
    Right – Pick to the right of the current picture.
  - CURRENT
    Current Frame – Pick crossing the current picture.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select_side_of_frame(*, extend=False, side='LEFT')

Pick pieces in relation to the current picture.

Parameters:

- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- side (Literal['LEFT', 'RIGHT', 'CURRENT']) – Side, (optional)
  - LEFT
    Left – Pick to the left of the current picture.
  - RIGHT
    Right – Pick to the right of the current picture.
  - CURRENT
    Current Frame – Pick crossing the current picture.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
