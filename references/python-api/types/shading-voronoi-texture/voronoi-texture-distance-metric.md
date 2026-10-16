# bpy.types.VoronoiTexture: distance_metric

distance_metric

Which algorithm measures distance from sample points to feature points (default 'DISTANCE' )

- DISTANCE
Actual Distance – sqrt(x*x+y*y+z*z).

- `DISTANCE_SQUARED`
Distance Squared – (x*x+y*y+z*z).

- MANHATTAN
Manhattan – The length of the distance in axial directions.

- CHEBYCHEV
Chebychev – The length of the longest Axial journey.

- `MINKOVSKY_HALF`
Minkowski 1/2 – Set Minkowski variable to 0.5.

- `MINKOVSKY_FOUR`
Minkowski 4 – Set Minkowski variable to 4.

- MINKOVSKY
Minkowski – Use the Minkowski function to calculate distance (exponent value determines the shape of the boundaries).

Type :

Literal['DISTANCE', '`DISTANCE_SQUARED`', 'MANHATTAN', 'CHEBYCHEV', '`MINKOVSKY_HALF`', '`MINKOVSKY_FOUR`', 'MINKOVSKY']

[Related references](INDEX.md).
