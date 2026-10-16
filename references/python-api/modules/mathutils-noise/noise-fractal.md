# mathutils.noise: mathutils.noise. fractal ( position , H , lacunarity , octaves , / , * , noise_basis = 'PERLIN_ORIGINAL' )

mathutils.noise. fractal ( position , H , lacunarity , octaves , / , * , noise_basis = '`PERLIN_ORIGINAL`' ) 

Gives the fractal Brownian motion (fBm) reading for the chosen basis, sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- H ( float ) – The fractal increment parameter.

- lacunarity ( float ) – How far apart consecutive frequencies sit.

- octaves ( float ) – Count of separate noise frequencies stacked together.

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

Returns :

The fractal Brownian motion noise value.

Return type :

float

[Related references](INDEX.md).
