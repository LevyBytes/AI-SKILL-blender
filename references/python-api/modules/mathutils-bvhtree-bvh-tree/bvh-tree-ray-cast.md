# mathutils.bvhtree.BVHTree: ray_cast ( origin , direction , distance = sys.float_info.max , / )

ray_cast ( origin , direction , distance = sys.float_info.max , / )

Shoot a ray at the geometry.

Parameters :

- origin ( Vector ) – Start location of the ray.

- direction ( Vector ) – Direction of the ray (normalized internally).

- distance ( float ) – Maximum distance threshold.

Returns :

Returns a tuple: (position, normal, index, distance),
Values will all be None if no hit is found.

Return type :

tuple[ Vector | None, Vector | None, int | None, float | None]

[Related references](INDEX.md).
