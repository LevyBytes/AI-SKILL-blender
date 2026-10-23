# bpy.types.VolumeGrid: properties

## VolumeGrid(bpy_struct)

### VolumeGrid(bpy_struct)

base class: bpy_struct
class bpy.types. VolumeGrid ( bpy_struct )

A single 3D volume grid.
channels

How many dimensions the grid's data type has (in [0, inf], default 0, readonly)

Type :

int
data_type

The data type stored for each voxel (default 'UNKNOWN' , readonly)

Type :

Literal[Volume Grid Data Type Items]
is_loaded

Whether the grid tree currently sits in memory (default False, readonly)

Type :

bool
matrix_object

Transform that maps voxel index coordinates into object space (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

Type :

mathutils.Matrix
name

Volume grid name (default "", readonly, never None)

Type :

str

[Related references](INDEX.md).
