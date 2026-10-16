# bpy.ops.sequencer.preview_duplicate_move_linked

bpy.ops.sequencer.preview_duplicate_move_linked(*, `SEQUENCER_OT`_duplicate={}, `TRANSFORM_OT`_translate={})

Reproduce chosen strips in the preview window without duplicating their media, then slide them.

Parameters:

- `SEQUENCER_OT`_duplicate (dict[str, Any]) – Duplicate Strips, Copy the chosen strips (optional, bpy.ops.sequencer.duplicate() keyword arguments)
- `TRANSFORM_OT`_translate (dict[str, Any]) – Move, Translate chosen items (optional, bpy.ops.transform.translate() keyword arguments)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
