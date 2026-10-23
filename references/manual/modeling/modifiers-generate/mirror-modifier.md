# Mirror Modifier

## Mirror Modifier

The Mirror modifier mirrors a mesh along its local X, Y, and/or Z axes, across the Object Origin. It can also use another object as the mirror center, then use that object's local axes instead of its own.

Options:
Axis — the X, Y, Z axis to mirror along, i.e. the axis perpendicular to the mirror plane of symmetry. To picture how the axis maps to direction: mirroring on the X axis turns the original mesh's positive X values into negative X values on the mirrored side. You can select more than one axis for more copies — one axis gives a single mirror, two axes four mirrors, and all three axes eight mirrors.
Bisect: if the mesh already sits on both sides of the mirror plane, cut it by that plane and keep only one side (the "positive" one by default) to perform the mirror.
Flip: when Bisect is enabled on an axis, switch which side is kept and mirrored (enabled, the "negative" side is kept instead of the "positive").
Mirror Object: an Object Selector to pick an object (usually an empty) whose position and rotation define the mirror planes (instead of those of the modified object); you can animate it to move the mirror axis.
Clipping: stop vertices from moving through the mirror plane(s) when you transform them in Edit Mode. If it's enabled while vertices are beyond the plane and outside the Merge Distance, they won't merge, but once within Merge Distance they snap together and can't move past the plane.
Note: vertices on the mirror plane can't move away from it while Clipping is enabled — disable it to move them along the mirror axis again.
Merge: where a vertex sits in the same place (within Merge Distance) as its mirror, merge it with the mirrored vertex.
Merge Distance: the maximum distance between a vertex and its mirror copy at which they merge (snapping onto the mirror plane); needs Merge enabled.
Bisect Distance: the distance from the bisect plane within which vertices are removed.

Data:
Flip UV: mirror the UV texture coordinates across the middle of the image; e.g. a vertex with UV coordinates of (0.3, 0.9) gets a mirror copy with UV coordinates of (0.7, 0.1).
UV Offsets: how far to shift mirrored UVs on the U/V axes; useful for baking (since overlapping UVs can cause artifacts in the baked map), so the UVs can be moved outside the image and left out of baking while still used for display.
Vertex Groups: try to mirror existing vertex groups, given these prerequisites: the groups must be named with the usual left/right pattern (suffixes like ".R", ".right", ".L", etc.), and the mirror-side group must already exist (it isn't created automatically) and be completely empty (no vertices assigned to it).
Flip UDIM: mirror the texture coordinates around each tile center.

Hints: many modeling tasks involve symmetrical objects, and this modifier offers a simple, efficient way to make them, with real-time mirror updates as you edit; once modeling is done, click Apply to make a real version of the mesh, or leave it as-is for future editing.
Accurately Positioning the Mirror Plane: applying a Mirror modifier often means moving the object's origin onto the edge or face that will be the mirror axis, which is tricky to do visually. For an exact position, select the edge, then snap Cursor to Selection (placing the 3D Cursor at the edge's center), then use the Set Origin menu and choose Origin to 3D Cursor, which moves the object's origin (and thus the mirror plane) to the cursor for an exact mirror. An alternative is to use an empty as a Mirror Object that you move to the correct position.

[Related references](INDEX.md).
