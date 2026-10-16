# bpy.types.SunLight: properties

angle

Angular diameter of the Sun as seen from the Earth (in [0, 3.14159], default 0.00918043)

Type :

float
energy

Sunlight strength in watts per meter squared (W/m²) (in [-inf, inf], default 10.0)

Type :

float
shadow_buffer_clip_start

Near plane of the shadow map; anything closer than this casts no shadow (in [1e-06, inf], default 0.05)

Type :

float
shadow_cascade_count

Number of texture used by the cascaded shadow map (in [1, 4], default 4)

Type :

int
shadow_cascade_exponent

Higher value increase resolution towards the viewpoint (in [0, 1], default 0.8)

Type :

float
shadow_cascade_fade

How smooth is the transition between each cascade (in [0, 1], default 0.1)

Type :

float
shadow_cascade_max_distance

End distance of the cascaded shadow map (only in perspective view) (in [0, inf], default 200.0)

Type :

float
shadow_filter_radius

Blur shadow aliasing using Percentage Closer Filtering (in [0, inf], default 1.0)

Type :

float
shadow_jitter_overblur

Trace shadows per jittered sample so under-sampling artifacts are reduced (in [0, 100], default 10.0)

Type :

float
shadow_maximum_resolution

Smallest a shadow map pixel may get; raising it trades shadow quality for lower memory use. (in [0, inf], default 0.001)

Type :

float
shadow_soft_size

Light size for ray shadow sampling (Raytraced shadows) (in [0, inf], default 0.0)

Type :

float
use_shadow_jitter

Turn on jittered soft shadows for finer shadow precision; off in the viewport unless switched on in render settings, and costly to performance. (default False)

Type :

bool

[Related references](INDEX.md).
