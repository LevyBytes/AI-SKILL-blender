# bpy.ops.sequencer.strip_modifier_set_active

bpy.ops.sequencer.strip_modifier_set_active(*, modifier='')

Enable the piece modifier to employ as the reference.

Parameters:

modifier (str) – Modifier, Name of the piece modifier to manage (optional, never None)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.strip_modifier_set_active(*, modifier='')

Enable the piece modifier to employ as the reference.

Parameters:

modifier (str) – Modifier, Name of the piece modifier to manage (optional, never None)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

- `ASSET_CATALOG`
Asset Catalog – Group the asset list by catalog so that assets sharing a catalog stay together; within one catalog they run in name order, and the catalogs follow the order of the flattened catalog hierarchy.

- move_strips ( bool ) – Move Strips, Once strips are dropped on the timeline, immediately pick them up for mouse translation (optional)

- frame_start ( int ) – Start Frame, The strip's first frame (in [-inf, inf], optional)

- channel ( int ) – Channel, Which channel the strip is placed on (in [1, 128], optional)

- replace_sel ( bool ) – Replace Selection, After the add completes, drop the previously selected strips (optional)

- overlap ( bool ) – Allow Overlap, Leave any overlap on the new strips uncorrected (optional)

- overlap_shuffle_override ( bool ) – Override Overlap Shuffle Behavior, Defer to the overlap_mode tool setting for how overlapping strips are shuffled (optional)

- skip_locked_or_muted_channels ( bool ) – Skip Locked or Muted Channels, Permit movie strips to be added onto muted or locked channels (optional)

- cache ( bool ) – Cache, Keep the sound resident in memory (optional)

- mono ( bool ) – Mono, Fold all of the sound's channels down to one (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.sequencer. strip_modifier_set_active ( * , modifier = '' ) 

Make a strip modifier the active one so it acts as the context

Parameters :

modifier ( str ) – Modifier, The strip modifier to edit, by name (optional, never None)

Returns :

Result of the operator call.

Return type :

[Related references](INDEX.md).
