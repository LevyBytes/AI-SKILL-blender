# bpy.ops.sequencer.scene_strip_add_new

bpy.ops.sequencer.scene_strip_add_new(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, type='NEW')

Insert a piece that uses a fresh scene as source media.

Parameters:

- move_strips (bool) – Move Strips, Automatically initiate mouse-driven translation of strips after insertion (optional)
- frame_start (int) – Start Frame, Where on the timeline the strip begins (in [-inf, inf], optional)
- channel (int) – Channel, Sequencer track for placement (in [1, 128], optional)
- replace_sel (bool) – Replace Selection, Clear prior selections once the operation finishes (optional)
- overlap (bool) – Allow Overlap, Permit new strips to overlap without correction (optional)
- overlap_shuffle_override (bool) – Override Overlap Shuffle Behavior, Use overlap mode from tool configuration (optional)
- skip_locked_or_muted_channels (bool) – Skip Locked or Muted Channels, Bypass muted or protected tracks when inserting (optional)
- type (Literal['NEW', 'EMPTY', '`LINK_COPY`', '`FULL_COPY`']) – Type, (optional)
  - NEW
    New – Insert new piece with a fresh bare scene using defaults.
  - EMPTY
    Copy Settings – Insert a piece with a bare scene, and replicate parameters from the active scene.
  - `LINK_COPY`
    Linked Copy – Insert a piece and bring in the groups from the active scene (shallow copy).
  - `FULL_COPY`
    Full Copy – Insert a piece and produce a complete duplicate of the active scene.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.scene_strip_add_new(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, type='NEW')

Insert a piece that uses a fresh scene as source media.

Parameters:

- move_strips (bool) – Move Strips, Automatically initiate mouse-driven translation of strips after insertion (optional)
- frame_start (int) – Start Frame, Where on the timeline the strip begins (in [-inf, inf], optional)
- channel (int) – Channel, Sequencer track for placement (in [1, 128], optional)
- replace_sel (bool) – Replace Selection, Clear prior selections once the operation finishes (optional)
- overlap (bool) – Allow Overlap, Permit new strips to overlap without correction (optional)
- overlap_shuffle_override (bool) – Override Overlap Shuffle Behavior, Use overlap mode from tool configuration (optional)
- skip_locked_or_muted_channels (bool) – Skip Locked or Muted Channels, Bypass muted or protected tracks when inserting (optional)
- type (Literal['NEW', 'EMPTY', '`LINK_COPY`', '`FULL_COPY`']) – Type, (optional)
  - NEW
    New – Insert new piece with a fresh bare scene using defaults.
  - EMPTY
    Copy Settings – Insert a piece with a bare scene, and replicate parameters from the active scene.
  - `LINK_COPY`
    Linked Copy – Insert a piece and bring in the groups from the active scene (shallow copy).
  - `FULL_COPY`
    Full Copy – Insert a piece and produce a complete duplicate of the active scene.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
