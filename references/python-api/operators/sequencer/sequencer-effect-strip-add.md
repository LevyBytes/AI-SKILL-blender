# bpy.ops.sequencer.effect_strip_add

bpy.ops.sequencer.effect_strip_add(*, type='CROSS', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, color=(0.0, 0.0, 0.0))

Insert an effect piece into the sequencer; many sit atop existing material.

Parameters:

- type (Literal['CROSS', 'ADD', 'SUBTRACT', '`ALPHA_OVER`', '`ALPHA_UNDER`', '`GAMMA_CROSS`', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', '`GAUSSIAN_BLUR`', 'TEXT', 'COLORMIX']) – Type, Which effect to insert (optional)
  - CROSS
    Crossfade – Transition out of one movie while transition into another.
  - ADD
    Add – Overlay color information from two clips.
  - SUBTRACT
    Subtract – Remove one strip's colors from another.
  - `ALPHA_OVER`
    Alpha Over – Layer alpha channel above other footage.
  - `ALPHA_UNDER`
    Alpha Under – Layer alpha channel below other footage.
  - `GAMMA_CROSS`
    Gamma Crossfade – Transition using color-corrected interpolation.
  - MULTIPLY
    Multiply – Scale color from two clips together.
  - WIPE
    Wipe – Push a cutting line across the image.
  - GLOW
    Glow – Intensify highlights and apply diffusion.
  - COLOR
    Color – Introduce a solid-color strip.
  - SPEED
    Speed – Adjust playback velocity of film clips.
  - MULTICAM
    Multicam Selector – Manage which camera feed is active.
  - ADJUSTMENT
    Adjustment Layer – Use non-permanent image processing.
  - `GAUSSIAN_BLUR`
    Gaussian Blur – Reduce sharpness along horizontal and vertical axes.
  - TEXT
    Text – Introduce a text-based strip.
  - COLORMIX
    Color Mix – Merge two strips via blend operations.
- move_strips (bool) – Move Strips, Automatically initiate mouse-driven translation of strips after insertion (optional)
- frame_start (int) – Start Frame, Where on the timeline the strip begins (in [-inf, inf], optional)
- length (int) – Length, Duration of the piece in frames, or length of each piece if adding multiple (in [-inf, inf], optional)
- channel (int) – Channel, Sequencer track for placement (in [1, 128], optional)
- replace_sel (bool) – Replace Selection, Clear prior selections once the operation finishes (optional)
- overlap (bool) – Allow Overlap, Permit new strips to overlap without correction (optional)
- overlap_shuffle_override (bool) – Override Overlap Shuffle Behavior, Use overlap mode from tool configuration (optional)
- skip_locked_or_muted_channels (bool) – Skip Locked or Muted Channels, Bypass muted or protected tracks when inserting (optional)
- color (mathutils.Color) – Color, Start the piece with this coloration (array of 3 items, in [0, 1], optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
