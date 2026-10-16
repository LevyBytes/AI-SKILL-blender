# bpy.ops.sequencer.select_circle

bpy.ops.sequencer.select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', ignore_connections=False)

Pick pieces via circular selection.

Parameters:

- x (int) – X, (in [-inf, inf], optional)
- y (int) – Y, (in [-inf, inf], optional)
- radius (int) – Radius, (in [1, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', ignore_connections=False)

Pick pieces via circular selection.

Parameters:

- x (int) – X, (in [-inf, inf], optional)
- y (int) – Y, (in [-inf, inf], optional)
- radius (int) – Radius, (in [1, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
