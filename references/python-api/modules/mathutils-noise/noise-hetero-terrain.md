# mathutils.noise: mathutils.noise. hetero_terrain ( position , H , lacunarity , octaves , offset , / , * , noise_basis = 'PERLIN_ORIGINAL' )

mathutils.noise. hetero_terrain ( position , H , lacunarity , octaves , offset , / , * , noise_basis = '`PERLIN_ORIGINAL`' ) 

Gives the heterogeneous-terrain reading for the chosen basis, sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- H ( float ) – Controls how rough the bumpiest areas become.

- lacunarity ( float ) – How far apart consecutive frequencies sit.

- octaves ( float ) – Count of separate noise frequencies stacked together.

- offset ( float ) – Height the terrain rises over its ‘sea level’.

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

Returns :

The heterogeneous terrain value.

Return type :

float

[Related references](INDEX.md).
