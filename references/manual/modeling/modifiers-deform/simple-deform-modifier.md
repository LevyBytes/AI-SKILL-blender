# Simple Deform Modifier

## Simple Deform Modifier

The Simple Deform modifier applies rotation (Twist, Bend) or scaling (Taper, Stretch) deformation to meshes, lattices, curves, surfaces, and text.

Deformation is calculated in local space; the object's local axes may differ from global axes. In the example above, global Z points up while local Z points at 45°.

A Deform axis (X, Y, or Z) specifies the deformation direction. The Limits field restricts influence to a portion of that axis. All distances are measured from the object origin; the vertices furthest from origin along the Deform axis define upper and lower bounds.

An external Deform object (typically an empty) can control the origin and local axis orientation.

Mode selects the deformation type. The examples show all four applied to text with origin at the left edge:

Twist rotates the mesh around the Deform axis. Each vertex is rotated around the origin based on its distance along that axis. For origins inside the object, this produces a twist. Below origin: negative rotation. Above origin: positive rotation. Vertices at the origin plane: no rotation. Rotation is weighted by vertex distance; furthest vertices experience maximum rotation, positive or negative.

Bend bends the mesh over the Deform axis. This is more complex. With Deform axis X or Y applied to a plane, no bending appears—the ambiguity of which perpendicular axis to bend around prevents automatic resolution. Setting Deform and Bending axes as opposite pairs (X with Z, Y with Z, Z with X) resolves this. For example, Deform axis X pairs with Bending axis Z; vertices with identical Z are not bent (at the origin). Bending increases with Z distance. Deform axis Z pairs with Bending axis X; rotation occurs along X coordinate—negative X rotates counterclockwise.

Taper scales linearly along the Deform axis. Scaling is weighted by origin distance; no scaling at the origin plane, maximum at the furthest vertices. This creates tapered shapes when the origin is interior.

Stretch stretches along the Deform axis. For interior origins, stretching resembles pulling rubber. Positive Factor makes the mesh longer in the Deform axis, wider at edges, thinner at origin. Negative Factor compresses, thickening the origin and thinning edges.

Angle (Twist & Bend) or Factor (Taper & Stretch) sets deformation magnitude. Negative values reverse it.

Axis, Origin specifies an object (typically an empty) defining the deformation origin and axis:

Rotation controls the Deform axis (the object's local axis becomes the deformation axis).

Translation controls the origin.

Scaling adjusts the deformation magnitude.

Limits sets the lower and upper deformation bounds on the Deform axis. Upper cannot be less than lower.

Lock (Twist, Taper, Stretch only) controls whether coordinates along the other two axes can change. For example, Stretching along Z can squash X without squashing Y by locking Y.

Vertex Group determines per-vertex influence, read from the Weight Paint map.

[Related references](INDEX.md).
