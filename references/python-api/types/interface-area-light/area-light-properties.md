# bpy.types.AreaLight: properties

## AreaLight(Light)

A light source emitting from a rectangular surface.

base classes — bpy_struct, ID, Light
class bpy.types. AreaLight ( Light )

A light emitting from a rectangular plane.
energy

Light energy emitted over the entire area of the light in all directions, in units of radiant power (W) (in [-inf, inf], default 10.0)

Type :

float
shadow_buffer_clip_start

Shadow map clip start, below which objects will not generate shadows (in [1e-06, inf], default 0.05)

Type :

float
shadow_filter_radius

Blur shadow aliasing using Percentage Closer Filtering (in [0, inf], default 1.0)

Type :

float
shadow_jitter_overblur

Apply shadow tracing to each jittered sample to reduce under-sampling artifacts (in [0, 100], default 10.0)

Type :

float
shadow_maximum_resolution

Minimum size of a shadow map pixel. Higher values use less memory at the cost of shadow quality. (in [0, inf], default 0.001)

Type :

float
shadow_soft_size

Light size for ray shadow sampling (Raytraced shadows) (in [0, inf], default 0.0)

Type :

float
shape

Shape of the area Light (default 'SQUARE' )

Type :

Literal['SQUARE', 'RECTANGLE', 'DISK', 'ELLIPSE']
size

Size of the area of the area light, X direction size for rectangle shapes (in [0, inf], default 0.25)

Type :

float
size_y

Size of the area of the area light in the Y direction for rectangle shapes (in [0, inf], default 0.25)

Type :

float
spread

How widely the emitted light fans out, as in the case of a gridded softbox (in [0, 3.14159], default 3.14159)

Type :

float
use_absolute_resolution

Limit the resolution at 1 unit from the light origin instead of relative to the shadowed pixel (default False)

Type :

bool
use_shadow_jitter

Enable jittered soft shadows to increase shadow precision (disabled in viewport unless enabled in the render settings). Has a high performance impact. (default False)

Type :

bool

[Related references](INDEX.md).
