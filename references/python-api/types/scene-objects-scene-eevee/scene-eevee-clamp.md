# bpy.types.SceneEEVEE: clamp_surface_direct, clamp_surface_indirect, clamp_volume_direct, clamp_volume_indirect

clamp_surface_direct

When non-zero, caps how much lights may contribute to a surface; larger values are scaled back to avoid heavy noise and slow convergence, trading accuracy. Applies to light objects. (in [0, inf], default 0.0)

Type :

float
clamp_surface_indirect

When non-zero, caps indirect lighting on a surface; larger values are scaled back to avoid heavy noise and slow convergence, trading accuracy. Applies to ray-tracing and light-probes. (in [0, inf], default 10.0)

Type :

float
clamp_volume_direct

When non-zero, caps how much lights may contribute within volumes; larger values are scaled back to avoid heavy noise and slow convergence, trading accuracy. Applies to light objects. (in [0, inf], default 0.0)

Type :

float
clamp_volume_indirect

When non-zero, caps indirect lighting within volumes; larger values are scaled back to avoid heavy noise and slow convergence, trading accuracy. Applies to light-probes. (in [0, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
