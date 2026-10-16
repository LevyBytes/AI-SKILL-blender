# bpy.types.FieldSettings: guide_clump_amount, guide_clump_shape, guide_free, guide_kink_amplitude, guide_kink_axis, guide_kink_frequency, guide_kink_shape, guide_kink_type, guide_minimum

guide_clump_amount

How much clumping is applied (in [-1, 1], default 0.0)

Type :

float
guide_clump_shape

The profile of the clumping (in [-0.999, 0.999], default 0.0)

Type :

float
guide_free

Span of guide-free time measured back from the end of particle life (in [0, 0.99], default 0.0)

Type :

float
guide_kink_amplitude

Size of the offset (in [0, 10], default 0.0)

Type :

float
guide_kink_axis

Axis along which the offset is applied (default 'X' )

Type :

Literal[Axis Xyz Items]
guide_kink_frequency

How often the offset repeats (1/total length) (in [0, 10], default 0.0)

Type :

float
guide_kink_shape

Bias the offset toward the start or the end (in [-0.999, 0.999], default 0.0)

Type :

float
guide_kink_type

Variety of periodic offset placed on the curve (default 'NONE' )

Type :

Literal[‘NONE’, ‘BRAID’, ‘CURL’, ‘RADIAL’, ‘ROLL’, ‘ROTATION’, ‘WAVE’]
guide_minimum

Distance beyond which particles feel the full effect (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
