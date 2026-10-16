# bpy.types.TextureNodeBricks: properties

## TextureNodeBricks(TextureNode)

### TextureNodeBricks(TextureNode)

base classes — bpy_struct, Node, NodeInternal, TextureNode
class bpy.types. TextureNodeBricks ( TextureNode )
offset

Sets how far each set of rows is shifted sideways (in [0, 1], default 0.0)

Type :

float
offset_frequency

Apply the offset once every N rows (in [2, 99], default 0)

Type :

int
squash

Multiplier that widens bricks on the rows picked out by Offset Frequency (in [0, 99], default 0.0)

Type :

float
squash_frequency

Apply the squash once every N rows (in [2, 99], default 0)

Type :

int

[Related references](INDEX.md).
