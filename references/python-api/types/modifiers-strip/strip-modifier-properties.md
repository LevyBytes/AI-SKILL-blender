# bpy.types.StripModifier: properties

## StripModifier(bpy_struct)

### StripModifier(bpy_struct)

base class — bpy_struct

subclasses —
BrightContrastModifier, ColorBalanceModifier, CurvesModifier, EchoModifier, HueCorrectModifier, MaskStripModifier, PitchModifier, SequencerCompositorModifierData, SequencerTonemapModifierData, SoundEqualizerModifier, WhiteBalanceModifier
class bpy.types. StripModifier ( bpy_struct )

A modifier applied to a sequence strip.
enable

Enable this modifier (default True)

Type :

bool
input_mask_id

Mask ID used as mask input for the modifier

Type :

Mask
input_mask_strip

Strip used as mask input for the modifier

Type :

Strip
input_mask_type

Type of input data used for mask (default 'STRIP' )

- STRIP
Strip – Use sequencer strip as mask input.

- ID
Mask – Use mask ID as mask input.

Type :

Literal[‘STRIP’, ‘ID’]
is_active

This modifier is active (default False)

Type :

bool
mask_time

Time to use for the Mask animation (default 'RELATIVE' )

- RELATIVE
Relative – Shift the mask animation so it begins at the strip’s start.

- ABSOLUTE
Absolute – Keep the mask animation locked to the scene frame.

Type :

Literal[‘RELATIVE’, ‘ABSOLUTE’]
mute

Mute this modifier (default False)

Type :

bool
name

(default “”, never None)

Type :

str
show_expanded

Mute expanded settings for the modifier (default False)

Type :

bool
type

(default '`BRIGHT_CONTRAST`' , readonly)

Type :

Literal[Strip Modifier Type Items]

[Related references](INDEX.md).
