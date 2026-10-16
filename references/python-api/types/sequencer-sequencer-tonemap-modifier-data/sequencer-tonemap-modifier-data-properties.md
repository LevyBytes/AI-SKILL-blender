# bpy.types.SequencerTonemapModifierData: properties

## SequencerTonemapModifierData(StripModifier)

### SequencerTonemapModifierData(StripModifier)

base classes — bpy_struct, StripModifier
class bpy.types. SequencerTonemapModifierData ( StripModifier )

Tone mapping modifier
adaptation

A value of 0 keeps it global; a value of 1 ties it to pixel intensity (in [0, 1], default 0.0)

Type :

float
contrast

Leave at 0 to let the input image supply the estimate (in [0, 1], default 0.0)

Type :

float
correction

A value of 0 treats all channels alike; a value of 1 handles each on its own (in [0, 1], default 0.0)

Type :

float
gamma

Leave at 1 when this is not in use (in [0.001, 3], default 0.0)

Type :

float
intensity

Negative values darken the image while positive values brighten it (in [-8, 8], default 0.0)

Type :

float
key

The target value that the mean luminance maps onto (in [0, 1], default 0.0)

Type :

float
offset

Usually kept at 1, but available as a further handle on the brightness curve (in [0.001, 10], default 0.0)

Type :

float
open_mask_input_panel

(default False)

Type :

bool
tonemap_type

Which tone-mapping algorithm to run (default '`RH_SIMPLE`' )

Type :

Literal[‘`RD_PHOTORECEPTOR`’, ‘`RH_SIMPLE`’]

[Related references](INDEX.md).
