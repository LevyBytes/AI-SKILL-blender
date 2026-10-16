# mathutils.noise: mathutils.noise. noise ( position , / , * , noise_basis = 'PERLIN_ORIGINAL' )

mathutils.noise. noise ( position , / , * , noise_basis = '`PERLIN_ORIGINAL`' ) 

Gives the scalar noise reading for the chosen basis, sampled at the supplied position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

Returns :

The noise value.

Return type :

float

[Related references](INDEX.md).
