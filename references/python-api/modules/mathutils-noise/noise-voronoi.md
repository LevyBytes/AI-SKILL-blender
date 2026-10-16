# mathutils.noise: mathutils.noise. voronoi ( position , / , * , distance_metric = 'DISTANCE' , exponent = 2.5 )

mathutils.noise. voronoi ( position , / , * , distance_metric = 'DISTANCE' , exponent = 2.5 ) 

Gives the distances out to the four nearest features along with where each one sits.

Parameters :

- position (mathutils.Vector) – Where in space the picked noise function gets sampled.

- distance_metric ( Literal [ 'DISTANCE' , '`DISTANCE_SQUARED`' , 'MANHATTAN' , 'CHEBYCHEV' , 'MINKOVSKY' , '`MINKOVSKY_HALF`' , '`MINKOVSKY_FOUR`' ] ) – A distance metric string.

- exponent ( float ) – The exponent for Minkowski distance metric.

Returns :

A list of distances to the four closest features and their locations.

Return type :

list[list[float] | list[mathutils.Vector]]

[Related references](INDEX.md).
