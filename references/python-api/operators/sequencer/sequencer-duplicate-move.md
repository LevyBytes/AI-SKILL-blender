# bpy.ops.sequencer.duplicate_move

bpy.ops.sequencer.duplicate_move(*, `SEQUENCER_OT`_duplicate={}, `TRANSFORM_OT`_seq_slide={})

Reproduce chosen strips and slide them.

Parameters:

- `SEQUENCER_OT`_duplicate (dict[str, Any]) – Duplicate Strips, Copy the chosen strips (optional, bpy.ops.sequencer.duplicate() keyword arguments)
- `TRANSFORM_OT`_seq_slide (dict[str, Any]) – Sequence Slide, Move a clip across the timeline (optional, bpy.ops.transform.seq_slide() keyword arguments)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
