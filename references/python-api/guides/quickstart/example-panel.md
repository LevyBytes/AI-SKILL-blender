# Quickstart: Example Panel

```python
import bpy

def main(context):
    for ob in context.scene.objects:
        print(ob)

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)

### Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()

    ### Test call.
    bpy.ops.object.simple_operator()
```

Run this script and Blender then knows about SimpleOperator, which from there you can reach via Operator Search or drop onto the toolbar.

To run the script:

- Start Blender and switch to the Scripting workspace.

- Click the New button in the text editor to create a new text data-block.

- Copy the code from above and paste it into the text editor.

- Click on the Run Script button.

- Move your cursor into the 3D Viewport, open the Operator Search menu, and type "Simple".

- Click on the "Simple Operator" item found in search.

See also

Those class members carrying the bl_ prefix have their documentation in the API reference under bpy.types.Operator.

Note

Whatever the main function prints lands in the terminal; to actually see it, make sure you're running with a terminal open.

### Example Panel

Like operators, panels get registered as a class. Note the additional bl_ variables, which pin down the context where the panel appears.

[Related references](INDEX.md).
