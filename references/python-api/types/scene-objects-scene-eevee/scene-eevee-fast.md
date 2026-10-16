# bpy.types.SceneEEVEE: fast_gi_bias, fast_gi_distance, fast_gi_method, fast_gi_quality, fast_gi_ray_count, fast_gi_resolution, fast_gi_step_count, fast_gi_thickness_far, fast_gi_thickness_near

fast_gi_bias

Nudge the shading normal to cut down self-intersection artifacts (in [0, 1], default 0.05)

Type :

float
fast_gi_distance

When non-zero, the farthest range at which other surfaces still feed the fast GI approximation (in [0, 100000], default 0.0)

Type :

float
fast_gi_method

Which fast GI approximation is used (default '`GLOBAL_ILLUMINATION`' )

- `AMBIENT_OCCLUSION_ONLY`
Ambient Occlusion – Substitute ambient occlusion for full global illumination.

- `GLOBAL_ILLUMINATION`
Global Illumination – Work out global illumination, accounting for light bouncing off nearby objects.

Type :

Literal[‘`AMBIENT_OCCLUSION_ONLY`’, ‘`GLOBAL_ILLUMINATION`’]
fast_gi_quality

Precision of the fast GI ray marching (in [0, 1], default 0.25)

Type :

float
fast_gi_ray_count

How many GI rays are traced per pixel (in [1, 16], default 2)

Type :

int
fast_gi_resolution

Sets the quality of fast GI lighting; higher resolution costs more memory. (default '2' )

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
fast_gi_step_count

How many screen samples are taken per GI ray (in [1, 64], default 8)

Type :

int
fast_gi_thickness_far

Angular thickness given to surfaces while computing fast GI and ambient occlusion; trims energy loss and missing occlusion from distant geometry. (in [0.0174533, 3.14159], default 0.785398)

Type :

float
fast_gi_thickness_near

Geometric thickness given to surfaces while computing fast GI and ambient occlusion; trims light leaking and missing contact occlusion. (in [0, 100000], default 0.25)

Type :

float

[Related references](INDEX.md).
