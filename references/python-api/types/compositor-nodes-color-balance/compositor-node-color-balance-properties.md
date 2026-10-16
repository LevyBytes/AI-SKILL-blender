# bpy.types.CompositorNodeColorBalance: properties

## CompositorNodeColorBalance(CompositorNode)

### CompositorNodeColorBalance(CompositorNode)

base classes — bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeColorBalance ( CompositorNode )

Tune color and values
input_whitepoint

The color taken as white; temperature and tint are derived back and forth from it without manual steps (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
output_whitepoint

The color that white is remapped onto; temperature and tint are derived back and forth from it without manual steps (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color

[Related references](INDEX.md).
