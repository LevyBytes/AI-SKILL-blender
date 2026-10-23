# bpy.types.NodeTree: overview

class bpy.types. NodeTree ( ID ) 

A tree of connected nodes that drives shading, texturing, and compositing.
## NodeTree(ID)

### NodeTree(ID)
### Poll Function 

Through NodeTree.poll, a node tree decides whether it should appear within a
given context: the same role Panel.poll and Menu.poll play for their own
visibility. When the function yields False, that node tree type stays out of
the picker in the node editor.

For shader node trees, a common check inspects the scene's currently active
render engine, exposing only the nodes that target that specific renderer.

```python
import bpy

class CyclesNodeTree(bpy.types.NodeTree):
    """ This operator is only visible when Cycles is the selected render engine"""
    bl_label = "Cycles Node Tree"
    bl_icon = 'NONE'

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'CYCLES'

bpy.utils.register_class(CyclesNodeTree)
```

base classes: bpy_struct, ID

subclasses —
CompositorNodeTree, GeometryNodeTree, ShaderNodeTree, TextureNodeTree

[Related references](INDEX.md).
