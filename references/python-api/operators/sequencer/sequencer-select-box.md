# bpy.ops.sequencer.select_box

bpy.ops.sequencer.select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False, ignore_connections=False)

Pick pieces via rectangular selection.

Parameters:

- xmin (int) – X Min, (in [-inf, inf], optional)
- xmax (int) – X Max, (in [-inf, inf], optional)
- ymin (int) – Y Min, (in [-inf, inf], optional)
- ymax (int) – Y Max, (in [-inf, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.
- tweak (bool) – Tweak, Permit box pick to pass through to sequence slide when the pointer is over a piece (optional)
- include_handles (bool) – Select Handles, Pick the pieces and their locations (optional)
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False, ignore_connections=False)

Pick pieces via rectangular selection.

Parameters:

- xmin (int) – X Min, (in [-inf, inf], optional)
- xmax (int) – X Max, (in [-inf, inf], optional)
- ymin (int) – Y Min, (in [-inf, inf], optional)
- ymax (int) – Y Max, (in [-inf, inf], optional)
- wait_for_input (bool) – Wait for Input, (optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.
- tweak (bool) – Tweak, Permit box pick to pass through to sequence slide when the pointer is over a piece (optional)
- include_handles (bool) – Select Handles, Pick the pieces and their locations (optional)
- ignore_connections (bool) – Ignore Connections, Pick pieces independently regardless of connection state (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
