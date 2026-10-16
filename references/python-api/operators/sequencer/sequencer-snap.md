# bpy.ops.sequencer.snap

bpy.ops.sequencer.snap(*, frame=0, side='LEFT', keep_offset=True)

Shift pieces to the current picture, employing the active piece as the pivot, and the pointer location in relation to the playhead to establish which direction of the playhead to snap to.

Parameters:

- frame (int) – Frame, Picture where chosen pieces will be shifted (in [-inf, inf], optional)
- side (Literal['LEFT', 'RIGHT']) – Snap Side, Which direction of the playhead pieces should snap to when no locations are picked (optional)
- keep_offset (bool) – Keep Offset, Whether the choice should be shifted completely or by each individual piece (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.snap(*, frame=0, side='LEFT', keep_offset=True)

Shift pieces to the current picture, employing the active piece as the pivot, and the pointer location in relation to the playhead to establish which direction of the playhead to snap to.

Parameters:

- frame (int) – Frame, Picture where chosen pieces will be shifted (in [-inf, inf], optional)
- side (Literal['LEFT', 'RIGHT']) – Snap Side, Which direction of the playhead pieces should snap to when no locations are picked (optional)
- keep_offset (bool) – Keep Offset, Whether the choice should be shifted completely or by each individual piece (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
