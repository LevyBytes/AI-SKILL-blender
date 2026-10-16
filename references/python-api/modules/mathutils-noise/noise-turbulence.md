# mathutils.noise: mathutils.noise. turbulence ( position , octaves , hard , / , * , noise_basis = 'PERLIN_ORIGINAL' , amplitude_scale = 0.5 , frequency_scale = 2.0 )

mathutils.noise. turbulence ( position , octaves , hard , / , * , noise_basis = '`PERLIN_ORIGINAL`' , amplitude_scale = 0.5 , frequency_scale = 2.0 ) 

Gives the turbulence reading for the chosen basis, sampled at the given position.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- octaves ( int ) – Count of separate noise frequencies stacked together.

- hard ( bool ) – Picks hard turbulence (abrupt edges) versus soft turbulence (gentle blending).

- noise_basis ( Literal [ 'BLENDER' , '`PERLIN_ORIGINAL`' , '`PERLIN_NEW`' , '`VORONOI_F1`' , '`VORONOI_F2`' , '`VORONOI_F3`' , '`VORONOI_F4`' , '`VORONOI_F2F1`' , '`VORONOI_CRACKLE`' , 'CELLNOISE' ] ) – A noise basis string.

- amplitude_scale ( float ) – The amplitude scaling factor.

- frequency_scale ( float ) – The frequency scaling factor.

Returns :

The turbulence value.

Return type :

float

[Related references](INDEX.md).
