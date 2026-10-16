# bpy.types.StucciTexture: noise_basis, noise_scale, noise_type

noise_basis

Noise basis used for turbulence (default '`BLENDER_ORIGINAL`' )

- `BLENDER_ORIGINAL`
Blender Original – Noise algorithm - Blender original: Smooth interpolated noise.

- `ORIGINAL_PERLIN`
Original Perlin – Noise algorithm - Original Perlin: Smooth interpolated noise.

- `IMPROVED_PERLIN`
Improved Perlin – Noise algorithm - Improved Perlin: Smooth interpolated noise.

- `VORONOI_F1`
Voronoi F1 – Noise algorithm - Voronoi F1: Returns distance to the closest feature point.

- `VORONOI_F2`
Voronoi F2 – Noise algorithm - Voronoi F2: Returns distance to the 2nd closest feature point.

- `VORONOI_F3`
Voronoi F3 – Noise algorithm - Voronoi F3: Returns distance to the 3rd closest feature point.

- `VORONOI_F4`
Voronoi F4 – Noise algorithm - Voronoi F4: Returns distance to the 4th closest feature point.

- `VORONOI_F2_F1`
Voronoi F2-F1 – Noise algorithm - Voronoi F1-F2.

- `VORONOI_CRACKLE`
Voronoi Crackle – Noise algorithm - Voronoi Crackle: Voronoi tessellation with sharp edges.

- `CELL_NOISE`
Cell Noise – Noise algorithm - Cell Noise: Square cell tessellation.

Type :

Literal[‘`BLENDER_ORIGINAL`’, ‘`ORIGINAL_PERLIN`’, ‘`IMPROVED_PERLIN`’, ‘`VORONOI_F1`’, ‘`VORONOI_F2`’, ‘`VORONOI_F3`’, ‘`VORONOI_F4`’, ‘`VORONOI_F2_F1`’, ‘`VORONOI_CRACKLE`’, ‘`CELL_NOISE`’]
noise_scale

Scaling for noise input (in [0.0001, inf], default 0.25)

Type :

float
noise_type

(default '`SOFT_NOISE`' )

- `SOFT_NOISE`
Soft – Generate soft noise (smooth transitions).

- `HARD_NOISE`
Hard – Generate hard noise (sharp transitions).

Type :

Literal[‘`SOFT_NOISE`’, ‘`HARD_NOISE`’]

[Related references](INDEX.md).
