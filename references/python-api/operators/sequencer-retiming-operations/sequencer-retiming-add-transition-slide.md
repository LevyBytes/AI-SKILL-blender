# bpy.ops.sequencer.retiming_add_transition_slide

bpy.ops.sequencer.retiming_add_transition_slide(*, `SEQUENCER_OT`_retiming_transition_add={}, `TRANSFORM_OT`_seq_slide={})

Create smooth interpolation between 2 speed-adjusted sections and adjust its period.

Parameters:

- `SEQUENCER_OT`_retiming_transition_add (dict[str, Any]) – Add Speed Transition, Create smooth interpolation between 2 speed-adjusted sections (optional, bpy.ops.sequencer.retiming_transition_add() keyword arguments)
- `TRANSFORM_OT`_seq_slide (dict[str, Any]) – Sequence Slide, Move a clip across the timeline (optional, bpy.ops.transform.seq_slide() keyword arguments)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
