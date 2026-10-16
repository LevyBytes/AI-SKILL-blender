# bpy.types.FluidDomainSettings: slice_axis, slice_depth, slice_per_voxel

slice_axis

(default 'AUTO' )

- AUTO
Auto – Adjust slice direction according to the view direction.

- X
X – Slice along the X axis.

- Y
Y – Slice along the Y axis.

- Z
Z – Slice along the Z axis.

Type :

Literal[‘AUTO’, ‘X’, ‘Y’, ‘Z’]
slice_depth

Position of the slice (in [0, 1], default 0.5)

Type :

float
slice_per_voxel

How many slices per voxel should be generated (in [0, 100], default 5.0)

Type :

float

[Related references](INDEX.md).
