# bpy.ops.sequencer.box_blade

bpy.ops.sequencer.box_blade(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', type='SOFT', ignore_selection=True, ignore_connections=False, remove_gaps=True)

Use a rectangular marquee to define portions of strips to excise.

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
- type (Literal['SOFT', 'HARD']) – Type, How the cut is performed on selected pieces (optional)
- ignore_selection (bool) – Ignore Selection, In box blade mode, apply cuts to all pieces, ignoring selection state (optional)
- ignore_connections (bool) – Ignore Connections, Keep cuts isolated to individual strips (optional)
- remove_gaps (bool) – Remove Gaps, In box blade mode, join cut segments together, shifting later pieces forward (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
