# bpy.types.Panel: Simple Object Panel

### Simple Object Panel

Here both a Panel.poll and a Panel.draw_header are supplied; despite the modest body, the layout mirrors how Blender's own panels are built.

```python
import bpy

class ObjectSelectPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_select"
    bl_label = "Select"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="My Select Panel")

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Selection Tools")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")

bpy.utils.register_class(ObjectSelectPanel)
```

[Related references](INDEX.md).
