# bpy.types.RaytraceEEVEE: properties

## RaytraceEEVEE(bpy_struct)

### RaytraceEEVEE(bpy_struct) 

base class: bpy_struct
class bpy.types. RaytraceEEVEE ( bpy_struct ) 

Settings controlling the quality of the raytracing pipeline
denoise_bilateral 

Soften the resolved radiance with a bilateral filter (default True)

Type :

bool
denoise_spatial 

Borrow rays from adjacent pixels (default True)

Type :

bool
denoise_temporal 

Build up samples by reprojecting the previous tracing results (default True)

Type :

bool
resolution_scale 

Sets how many rays are cast per pixel. Greater resolution consumes more memory. (default '2' )

- 1
1:1 – Full resolution.

- 2
1:2 – Render this effect at 50% render resolution.

- 4
1:4 – Render this effect at 25% render resolution.

- 8
1:8 – Render this effect at 12.5% render resolution.

- 16
1:16 – Render this effect at 6.25% render resolution.

Type :

Literal[‘1’, ‘2’, ‘4’, ‘8’, ‘16’]
screen_trace_quality 

How precise the screen-space ray-tracing is (in [0, 1], default 0.25)

Type :

float
screen_trace_thickness 

Assumed surface thickness used to find intersections during screen-tracing (in [1e-06, inf], default 0.2)

Type :

float
trace_max_roughness 

Highest roughness that still routes through the tracing pipeline. Rougher surfaces fall back to the fast GI approximation, and a value of 1 turns that approximation off. (in [0, 1], default 0.5)

Type :

float
use_denoise 

Apply noise-reduction methods to raytraced effects (default True)

Type :

bool

[Related references](INDEX.md).
