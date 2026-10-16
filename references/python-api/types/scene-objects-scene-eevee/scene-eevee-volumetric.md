# bpy.types.SceneEEVEE: volumetric_end, volumetric_light_clamp, volumetric_ray_depth, volumetric_sample_distribution, volumetric_samples, volumetric_shadow_samples, volumetric_start, volumetric_tile_size

volumetric_end

Far distance at which the volumetric effect stops (in [1e-06, inf], default 100.0)

Type :

float
volumetric_light_clamp

Cap on light contribution that lowers noise (in [0, inf], default 0.0)

Type :

float
volumetric_ray_depth

Largest number of surface intersections the accurate volume intersection method handles; going over it produces artifacts, and a higher count raises VRAM usage. (in [1, 16], default 16)

Type :

int
volumetric_sample_distribution

Bias more samples toward the camera (in [0, 1], default 0.8)

Type :

float
volumetric_samples

How many steps compute the volumetric effects; a higher step count raises VRAM usage and quality. (in [1, 256], default 64)

Type :

int
volumetric_shadow_samples

How many samples compute volumetric shadowing (in [1, 128], default 16)

Type :

int
volumetric_start

Near distance at which the volumetric effect begins (in [1e-06, inf], default 0.1)

Type :

float
volumetric_tile_size

Sets the quality of the volumetric effects; higher resolution costs more memory. (default '8' )

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

[Related references](INDEX.md).
