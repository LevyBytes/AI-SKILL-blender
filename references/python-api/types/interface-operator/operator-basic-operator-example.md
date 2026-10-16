# bpy.types.Operator: Basic Operator Example

### Basic Operator Example 

A small operator that just prints a message.

Because this operator supplies only an Operator.execute function, it accepts no user input.

That function ought to give back {'FINISHED'} or {'CANCELLED'} ; the latter signals that the operator stopped without altering anything, so no undo step is recorded (the following example covers undo in more detail).

Note

You have to register Operator subclasses before Blender lets you reach them.

```python
import bpy

class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Minimal Operator"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(HelloWorldOperator.bl_idname, text="Hello World Operator")

### Register and add to the view menu (required to also use F3 search "Hello World Operator" for quick access).
bpy.utils.register_class(HelloWorldOperator)
bpy.types.VIEW3D_MT_view.append(menu_func)

### Test call to the newly defined operator.
bpy.ops.wm.hello_world()
```

[Related references](INDEX.md).
