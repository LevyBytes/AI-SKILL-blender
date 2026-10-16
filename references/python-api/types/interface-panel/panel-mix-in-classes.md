# bpy.types.Panel: Mix-in Classes

### Mix-in Classes

Shared properties together with a common Menu.poll can be factored out into a mix-in parent that several panels inherit from.

```python
import bpy

class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

class PanelOne(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_1"
    bl_label = "Panel One"

    def draw(self, context):
        self.layout.label(text="Small Class")

class PanelTwo(View3DPanel, bpy.types.Panel):
    bl_idname = "VIEW3D_PT_test_2"
    bl_label = "Panel Two"

    def draw(self, context):
        self.layout.label(text="Also Small Class")

bpy.utils.register_class(PanelOne)
bpy.utils.register_class(PanelTwo)
```

base class — bpy_struct

[Related references](INDEX.md).
