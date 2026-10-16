# bpy.ops.sequencer.add_scene_strip_from_scene_asset

bpy.ops.sequencer.add_scene_strip_from_scene_asset(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, asset_library_type='LOCAL', asset_library_identifier='', relative_asset_identifier='')

Creates a sequencer strip using a duplicate of a scene asset as its source media.

Parameters:

- move_strips (bool) – Move Strips, Automatically initiate mouse-driven translation of strips after insertion (optional)
- frame_start (int) – Start Frame, Where on the timeline the strip begins (in [-inf, inf], optional)
- channel (int) – Channel, Sequencer track for placement (in [1, 128], optional)
- replace_sel (bool) – Replace Selection, Clear prior selections once the operation finishes (optional)
- overlap (bool) – Allow Overlap, Permit new strips to overlap without correction (optional)
- overlap_shuffle_override (bool) – Override Overlap Shuffle Behavior, Use overlap mode from tool configuration (optional)
- skip_locked_or_muted_channels (bool) – Skip Locked or Muted Channels, Bypass muted or protected tracks when inserting (optional)
- asset_library_type (Literal[Asset Library Type Items]) – Asset Library Type, (optional)
- asset_library_identifier (str) – Asset Library Identifier, (optional, never None)
- relative_asset_identifier (str) – Relative Asset Identifier, (optional, never None)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
