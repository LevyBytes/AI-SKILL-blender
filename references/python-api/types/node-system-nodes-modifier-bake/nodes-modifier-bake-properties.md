# bpy.types.NodesModifierBake: properties

## NodesModifierBake(bpy_struct)

### NodesModifierBake(bpy_struct)

base class — bpy_struct
class bpy.types. NodesModifierBake ( bpy_struct )
bake_id

Identifier for this bake which remains unchanged even when the bake node is renamed, grouped or ungrouped (in [-inf, inf], default 0, readonly)

Type :

int
bake_mode

(default 'ANIMATION' )

- ANIMATION
Animation – Bake a frame range.

- STILL
Still – Bake a single frame.

Type :

Literal[‘ANIMATION’, ‘STILL’]
bake_target

Where to store the baked data (default 'INHERIT' )

- INHERIT
Inherit from Modifier – Use setting from the modifier.

- PACKED
Packed – Pack the baked data into the .blend file.

- DISK
Disk – Store the baked data in a directory on disk.

Type :

Literal[‘INHERIT’, ‘PACKED’, ‘DISK’]
data_blocks

(default None, readonly)

Type :

NodesModifierBakeDataBlocks[NodesModifierDataBlock]
directory

Location on disk where the bake data is stored (default “”, never None, blend relative // prefix supported)

Type :

str
frame_end

Frame where the baking ends (in [-inf, inf], default 0)

Type :

int
frame_start

Frame where the baking starts (in [-inf, inf], default 0)

Type :

int
node

Bake node or simulation output node that corresponds to this bake. This node may be deeply nested in the modifier node group. It can be none in some cases like missing linked data blocks. (readonly)

Type :

Node
use_custom_path

Set a custom location for the baked data by hand (default False)

Type :

bool
use_custom_simulation_frame_range

Replace the scene's simulation frame range with a custom one (default False)

Type :

bool

[Related references](INDEX.md).
