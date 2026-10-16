# bpy.types.Collection: lineart_intersection_mask, lineart_intersection_priority, lineart_usage, lineart_use_intersection_mask

lineart_intersection_mask

Mask value carried by intersections this collection produces (array of 8 items, default (False, False, False, False, False, False, False, False))

Type :

bpy_prop_array[bool]
lineart_intersection_priority

When intersection lines overlap, the object whose priority value is greater wins inclusion (in [0, 255], default 0)

Type :

int
lineart_usage

Sets the role this collection plays during Line Art computation (default 'INCLUDE' )

- INCLUDE
Include – Produce feature lines from this collection.

- `OCCLUSION_ONLY`
Occlusion Only – Let the collection contribute occlusion only.

- EXCLUDE
Exclude – Leave this collection out of Line Art entirely.

- `INTERSECTION_ONLY`
Intersection Only – Emit just intersection lines for this collection.

- `NO_INTERSECTION`
No Intersection – Keep the collection but skip generating intersection lines.

- `FORCE_INTERSECTION`
Force Intersection – Emit intersection lines even against objects that turned intersection off.

Type :

Literal[‘INCLUDE’, ‘`OCCLUSION_ONLY`’, ‘EXCLUDE’, ‘`INTERSECTION_ONLY`’, ‘`NO_INTERSECTION`’, ‘`FORCE_INTERSECTION`’]
lineart_use_intersection_mask

Apply a custom intersection mask to the faces belonging to this collection (default False)

Type :

bool

[Related references](INDEX.md).
