# bpy.types.Operator: Invoke Function

### Invoke Function 

Operator.invoke serves to set the operator up from the context at the instant it is called. invoke() usually sets properties that execute() then consumes. Certain operators lack an execute() function, which strips away the ability to replay them from a script or macro.

Calling an operator through bpy.ops makes the execution context follow the argument handed to bpy.ops; the default is execute(). Triggering an operator from a button or menu item instead respects the UILayout.operator_context setting, and most of the time that means invoke(). A key shortcut always runs an operator through invoke(), and there's no way to alter that.

The example below builds an operator that reads mouse input to run a function, and that can be invoked or executed from the Python API alike.

Note as well that this operator declares properties of its own — distinct from ordinary class properties, because Blender registers them with the operator so they can serve as call arguments, be stored for operator undo/redo, and be added to the interface automatically.

```python
import bpy

class SimpleMouseOperator(bpy.types.Operator):
    """ This operator shows the mouse location,
        this string is used for the tooltip and API docs
    """
    bl_idname = "wm.mouse_position"
    bl_label = "Invoke Mouse Operator"

    x: bpy.props.IntProperty()
    y: bpy.props.IntProperty()

    def execute(self, context):
        ### Rather than printing, use the report function,
        ### this way the message appears in the header.
        self.report({'INFO'}, "Mouse coords are {:d} {:d}".format(self.x, self.y))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.x = event.mouse_x
        self.y = event.mouse_y
        return self.execute(context)

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(SimpleMouseOperator.bl_idname, text="Simple Mouse Operator")

### Register and add to the view menu (required to also use F3 search "Simple Mouse Operator" for quick access).
bpy.utils.register_class(SimpleMouseOperator)
bpy.types.VIEW3D_MT_view.append(menu_func)

### Test call to the newly defined operator.
### Here we call the operator and invoke it,
### meaning that the settings are taken from the mouse.
bpy.ops.wm.mouse_position('INVOKE_DEFAULT')

### Another test call, this time call execute() directly with pre-defined settings.
bpy.ops.wm.mouse_position('EXEC_DEFAULT', x=20, y=66)
```

[Related references](INDEX.md).
