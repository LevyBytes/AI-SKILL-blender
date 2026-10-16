# bpy.types.Operator: Calling a File Selector

### Calling a File Selector 

Here is how an operator can bring up the file selector.

Observe that the invoke function calls a window manager method and gives back {'`RUNNING_MODAL`'} , so the file selector remains open and the operator doesn't quit the moment invoke finishes.

When the user confirms, the file selector runs the operator and triggers Operator.execute .

Operator.poll is optional and is there to verify whether the operator may run.

```python
import bpy

class ExportSomeData(bpy.types.Operator):
    """Test exporter which just writes hello world"""
    bl_idname = "export.some_data"
    bl_label = "Export Some Data"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        file = open(self.filepath, 'w')
        file.write("Hello World " + context.object.name)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportSomeData.bl_idname, text="Text Export Operator")

### Register and add to the file selector (required to also use F3 search "Text Export Operator" for quick access).
bpy.utils.register_class(ExportSomeData)
bpy.types.TOPBAR_MT_file_export.append(menu_func)

### Test call.
bpy.ops.export.some_data('INVOKE_DEFAULT')
```

[Related references](INDEX.md).
