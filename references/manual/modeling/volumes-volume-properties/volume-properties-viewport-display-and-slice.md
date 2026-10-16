# Volume Properties: Viewport Display, Slice

### Viewport Display

Wireframe
How the volume is drawn in wireframe shading mode.
When the volume data is heavy, you might prefer to keep the object locked to wireframe display the whole time.
Doing so keeps the 3D Viewport snappy while the volume still turns up in the final render.

None :

Leaves the volume out of wireframe mode entirely.

Bounds :

Draws the volume as one Bounding Box spanning the whole grid.

Boxes :

Draws a bounding box around each node of the volume tree.

Points :

Draws a point at each node of the volume tree.

Detail
How fine the Boxes or Points wireframe rendering gets.

Coarse :

Puts a single box or point at every intermediate node of the tree.

Fine :

Puts a box or point at each leaf node, which covers 8×8 voxels.

Density
How thick the volume looks in the 3D Viewport.
The volume's density at render time gets tuned through
Volume Shading instead.

Interpolation
Which interpolation method gets used when visualizing the fluid grid.

Linear :

Interpolates linearly from voxel to voxel — a good balance of smoothness and speed.

Cubic :

Interpolates cubically from voxel to voxel — smoother, higher quality, but heavier to compute.

Closest :

Skips interpolation between voxels, leaving the raw voxels as they are.

### Slice

Draws just one flat 2D cross-section of the domain object.

Axis

Auto :

Lets the slice direction follow whichever way you're looking.

X/Y/Z :

Cuts the slice along the X, Y, or Z axis.

Position
Where the slice sits, measured against the length of the matching side of the domain.

[Related references](INDEX.md).
