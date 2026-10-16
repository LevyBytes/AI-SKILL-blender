# bpy.types.Operator: Custom Drawing

### Custom Drawing 

Out of the box, operator properties lay themselves out automatically. For finer control you can supply your own layout through an Operator.draw function.

It behaves the same way as the Panel and Menu draw functions, and is used for dialogs and file selectors.

```python
import bpy

class CustomDrawOperator(bpy.types.Operator):
    bl_idname = "object.custom_draw"
    bl_label = "Simple Modal Operator"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    my_float: bpy.props.FloatProperty(name="Float")
    my_bool: bpy.props.BoolProperty(name="Toggle Option")
    my_string: bpy.props.StringProperty(name="String Value")

    def execute(self, context):
        print("Test", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Custom Interface!")

        row = col.row()
        row.prop(self, "my_float")
        row.prop(self, "my_bool")

        col.prop(self, "my_string")

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(CustomDrawOperator.bl_idname, text="Custom Draw Operator")

### Register and add to the object menu (required to also use F3 search "Custom Draw Operator" for quick access).
bpy.utils.register_class(CustomDrawOperator)
bpy.types.VIEW3D_MT_object.append(menu_func)

### Test call.
bpy.ops.object.custom_draw('INVOKE_DEFAULT')
```

[Related references](INDEX.md).
