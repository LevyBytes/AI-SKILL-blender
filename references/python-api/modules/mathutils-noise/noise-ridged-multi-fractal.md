# mathutils.noise: mathutils.noise. ridged_multi_fractal ( position , H , lacunarity , octaves , offset , gain , / , * , noise_basis = 'PERLIN_ORIGINAL' )

mathutils.noise. ridged_multi_fractal ( position , H , lacunarity , octaves , offset , gain , / , * , noise_basis = '`PERLIN_ORIGINAL`' ) 

Gives the ridged multifractal reading for the chosen basis, sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- H ( float ) – Controls how rough the bumpiest areas become.

- lacunarity ( float ) – How far apart consecutive frequencies sit.

- octaves ( float ) – Count of separate noise frequencies stacked together.

- offset ( float ) – Height the terrain rises over its ‘sea level’.

- gain ( float ) – Scaling applied to the values.

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

Returns :

The ridged multifractal value.

Return type :

float

[Related references](INDEX.md).
