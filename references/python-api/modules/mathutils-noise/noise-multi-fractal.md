# mathutils.noise: mathutils.noise. multi_fractal ( position , H , lacunarity , octaves , / , * , noise_basis = 'PERLIN_ORIGINAL' )

mathutils.noise. multi_fractal ( position , H , lacunarity , octaves , / , * , noise_basis = '`PERLIN_ORIGINAL`' ) 

Gives the multifractal noise reading for the chosen basis, sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- H ( float ) – Sets the upper bound on the fractal dimension.

- lacunarity ( float ) – How far apart consecutive frequencies sit.

- octaves ( float ) – Count of separate noise frequencies stacked together.

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

Returns :

The multifractal noise value.

Return type :

float

[Related references](INDEX.md).
