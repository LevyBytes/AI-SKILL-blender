# Volume Properties: Render

### Render

Space
How the volume's density and step size get worked out.

Object :

Holds volume Density and Detail steady no matter how the object is scaled.

World :

Lets you set Step Size and Density in world space.

Clipping Cycles Only
The cutoff below which voxels count as empty space, used to speed rendering up.

Precision Cycles Only
How precise the volume data is. Drop this down to use less memory, at the price of detail.

Full :

Full float — every value stored at 32 bit.

Half :

Half float — every value stored at 16 bit.

Variable :

Quietly drops to lower precision wherever the result is harder to notice.

Velocity Grid Cycles Only
The name of the grid that holds per-voxel velocities, used to compute motion blur.
It can either be the name of one grid carrying 3D vectors,
or the prefix shared by three separate grids carrying scalar values.
For the three-grid case, the X grid's name should end in x , .x or _x ,
and the Y and Z grids follow the same pattern.

Velocity Unit Cycles Only
Whether the velocity grid(s) are expressed in distance per frame or per second.

Velocity Scale Cycles Only
A multiplier of your own that gets applied to the velocities held in the VDB.

[Related references](INDEX.md).
