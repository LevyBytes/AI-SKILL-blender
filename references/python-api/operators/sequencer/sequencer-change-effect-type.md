# bpy.ops.sequencer.change_effect_type

bpy.ops.sequencer.change_effect_type(*, type='CROSS')

Substitute an effect strip with another that accepts the same count of inputs.

Parameters:

type (Literal['CROSS', 'ADD', 'SUBTRACT', '`ALPHA_OVER`', '`ALPHA_UNDER`', '`GAMMA_CROSS`', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', '`GAUSSIAN_BLUR`', 'TEXT', 'COLORMIX']) – Type, Which effect to apply (optional)

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

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
