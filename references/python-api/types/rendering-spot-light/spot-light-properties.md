# bpy.types.SpotLight: properties

energy

Power this light would radiate across its whole area if the spot angle did not constrain it, in radiant power (W) (in [-inf, inf], default 10.0)

Type :

float
shadow_buffer_clip_start

Start of the shadow map clip; objects nearer than this cast no shadows (in [1e-06, inf], default 0.05)

Type :

float
shadow_filter_radius

Soften shadow aliasing through Percentage Closer Filtering (in [0, inf], default 1.0)

Type :

float
shadow_jitter_overblur

Run shadow tracing on every jittered sample to cut down under-sampling artifacts (in [0, 100], default 10.0)

Type :

float
shadow_maximum_resolution

Smallest size of a shadow-map pixel. Larger values save memory but lower shadow quality. (in [0, inf], default 0.001)

Type :

float
shadow_soft_size

Size of the light used when sampling ray shadows (Raytraced shadows) (in [0, inf], default 0.0)

Type :

float
show_cone

Draw a transparent cone in the 3D view so you can see which objects fall inside it (default False)

Type :

bool
spot_blend

How soft the edge of the spotlight is (in [0, 1], default 0.15)

Type :

float
spot_size

Angular width of the spotlight beam (in [0.0174533, 3.14159], default 0.785398)

Type :

float
use_absolute_resolution

Cap resolution at 1 unit out from the light origin rather than relative to the shadowed pixel (default False)

Type :

bool
use_shadow_jitter

Turn on jittered soft shadows for greater shadow precision (off in the viewport unless enabled in render settings). Costs a lot of performance. (default False)

Type :

bool
use_soft_falloff

Use falloff to soften sharp edges where the light geometry crosses other objects (default True)

Type :

bool
use_square

Project a square-shaped spot light (default False)

Type :

bool

[Related references](INDEX.md).
