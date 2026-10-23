# bpy.types.VolumeGrids: properties

## VolumeGrids(bpy_prop_collection)

### VolumeGrids(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types. VolumeGrids ( bpy_prop_collection )

A set of 3D volume grids.
active_index

Index of active volume grid (in [0, inf], default 0)

Type :

int
error_message

When grid loading fails, the detailed error text (default "", readonly, never None)

Type :

str
frame

Frame the volume grids are loaded at, derived from scene time and the volume parameters (in [-inf, inf], default 0, readonly)

Type :

int
frame_filepath

Volume file used to load the current frame. Blank when nothing has loaded yet or the frame lives only in memory. (default "", readonly, never None, blend relative // prefix supported)

Type :

str
is_loaded

Whether the grid list and metadata are held in memory (default False, readonly)

Type :

bool

[Related references](INDEX.md).
