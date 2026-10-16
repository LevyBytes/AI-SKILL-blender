# bpy.types.PointLight: properties

## PointLight(Light)

### PointLight(Light)

base classes — bpy_struct, ID, Light
class bpy.types. PointLight ( Light )

A point Light that radiates in every direction.
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
energy

Radiant power (W) the light puts out across its whole surface in all directions (in [-inf, inf], default 10.0)

Type :

float
shadow_buffer_clip_start

Near limit of the shadow map; geometry nearer than this casts no shadow (in [1e-06, inf], default 0.05)

Type :

float
shadow_filter_radius

Soften shadow stair-stepping through Percentage Closer Filtering (in [0, inf], default 1.0)

Type :

float
shadow_jitter_overblur

Run shadow tracing on every jittered sample to cut down on under-sampling noise (in [0, 100], default 10.0)

Type :

float
shadow_maximum_resolution

Smallest allowed size for a shadow-map pixel. Raising it trades shadow detail for lower memory use. (in [0, inf], default 0.001)

Type :

float
shadow_soft_size

Size of the light used when sampling ray-traced shadows (Raytraced shadows) (in [0, inf], default 0.0)

Type :

float
use_absolute_resolution

Cap the resolution at one unit out from the light origin rather than scaling it with the shaded pixel (default False)

Type :

bool
use_shadow_jitter

Turn on jittered soft shadows for finer shadow precision (off in the viewport unless switched on in the render settings). Carries a heavy performance cost. (default False)

Type :

bool
use_soft_falloff

Fade the light off near contact so edges stay smooth where its geometry overlaps other objects (default True)

Type :

bool

[Related references](INDEX.md).
