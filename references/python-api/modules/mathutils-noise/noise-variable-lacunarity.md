# mathutils.noise: mathutils.noise. variable_lacunarity ( position , distortion , / , * , noise_type1 = 'PERLIN_ORIGINAL' , noise_type2 = 'PERLIN_ORIGINAL' )

mathutils.noise. variable_lacunarity ( position , distortion , / , * , noise_type1 = '`PERLIN_ORIGINAL`' , noise_type2 = '`PERLIN_ORIGINAL`' ) 

Gives a variable-lacunarity reading — a warped form of noise where noise type 1 is bent by noise type 2 — sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- distortion ( float ) – How strongly the warp is applied.

- noise_type1 ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise type string.

- noise_type2 ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise type string.

Returns :

The variable lacunarity noise value.

Return type :

float

[Related references](INDEX.md).
