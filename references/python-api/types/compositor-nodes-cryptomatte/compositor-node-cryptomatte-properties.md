# bpy.types.CompositorNodeCryptomatte: properties

## CompositorNodeCryptomatte(CompositorNode)

### CompositorNodeCryptomatte(CompositorNode)

base classes: bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeCryptomatte ( CompositorNode )

No longer maintained: switch to the Cryptomatte Node in its place.
add

Picks a color from the Pick output to bring an object or material into the matte (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Color
matte_id

Set of object and material crypto IDs that the matte should cover (default “”, never None)

Type :

str
remove

Picks a color from the Pick output to take an object or material back out of the matte (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Color

[Related references](INDEX.md).
