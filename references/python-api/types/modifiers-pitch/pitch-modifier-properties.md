# bpy.types.PitchModifier: properties

## PitchModifier(StripModifier)

### PitchModifier(StripModifier)

base classes: bpy_struct, StripModifier
class bpy.types. PitchModifier ( StripModifier )

Adjusts the pitch of an audio strip
cents

A cent is one one-hundredth of a semi-tone. (in [-100, 100], default 0)

Type :

int
mode

Mode of the pitch shift (default 'SEMITONES' )

- SEMITONES
Semitones – Shift pitch using semitones and cents.

- RATIO
Ratio – Shift pitch using a direct ratio.

Type :

Literal[‘SEMITONES’, ‘RATIO’]
preserve_formant

Whether to preserve the vocal formants when shifting the pitch. (default False)

Type :

bool
quality

Quality of the pitch shifting (default 'HIGH' )

- HIGH
High – Prioritize high-quality pitch processing.

- FAST
Fast – Prioritize speed over audio quality.

- CONSISTENT
Consistent – Prioritize consistency for dynamic pitch changes.

Type :

Literal[‘HIGH’, ‘FAST’, ‘CONSISTENT’]
ratio

Factor by which the audio pitch is scaled. (in [0.5, 2], default 0.0)

Type :

float
semitones

Number of semitones to shift the pitch. (in [-12, 12], default 0)

Type :

int

[Related references](INDEX.md).
