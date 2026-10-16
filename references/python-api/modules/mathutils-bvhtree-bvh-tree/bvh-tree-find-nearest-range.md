# mathutils.bvhtree.BVHTree: find_nearest_range ( origin , distance = 1.84467e+19 , / )

find_nearest_range ( origin , distance = 1.84467e+19 , / )

Locate the elements nearest a given point within the distance range (usually face indices).

Parameters :

- origin ( Vector ) – Find nearest elements to this point.

- distance ( float ) – Maximum distance threshold.

Returns :

Returns a list of tuples (position, normal, index, distance)

Return type :

list[tuple[ Vector , Vector , int, float]]

[Related references](INDEX.md).
