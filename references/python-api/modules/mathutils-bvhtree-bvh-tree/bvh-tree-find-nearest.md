# mathutils.bvhtree.BVHTree: find_nearest ( origin , distance = 1.84467e+19 , / )

find_nearest ( origin , distance = 1.84467e+19 , / )

Locate the element nearest a given point (usually a face index).

Parameters :

- origin ( Vector ) – Find nearest element to this point.

- distance ( float ) – Maximum distance threshold.

Returns :

Returns a tuple: (position, normal, index, distance),
Values will all be None if no hit is found.

Return type :

tuple[ Vector | None, Vector | None, int | None, float | None]

[Related references](INDEX.md).
