# bpy.types.ParticleSettings: kink, kink_amplitude, kink_amplitude_clump, kink_amplitude_random, kink_axis, kink_axis_random, kink_extra_steps, kink_flat, kink_frequency, kink_shape

kink

Type of periodic offset on the path (default 'NO' )

Type :

Literal[‘NO’, ‘CURL’, ‘RADIAL’, ‘WAVE’, ‘BRAID’, ‘SPIRAL’]
kink_amplitude

The amplitude of the offset (in [-100000, 100000], default 0.2)

Type :

float
kink_amplitude_clump

Degree to which clump influences the kink amplitude (in [0, 1], default 1.0)

Type :

float
kink_amplitude_random

Random variation of the amplitude (in [0, 1], default 0.0)

Type :

float
kink_axis

Which axis to use for offset (default 'Z' )

Type :

Literal[Axis Xyz Items]
kink_axis_random

Random variation of the orientation (in [0, 1], default 0.0)

Type :

float
kink_extra_steps

Additional steps to resolve special kink features (in [1, inf], default 4)

Type :

int
kink_flat

How flat the hairs are (in [0, 1], default 0.0)

Type :

float
kink_frequency

The frequency of the offset (1/total length) (in [-100000, 100000], default 2.0)

Type :

float
kink_shape

Bias the offset toward the start or end (in [-0.999, 0.999], default 0.0)

Type :

float

[Related references](INDEX.md).
