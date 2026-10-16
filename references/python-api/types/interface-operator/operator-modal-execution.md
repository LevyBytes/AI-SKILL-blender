# bpy.types.Operator: Modal Execution

### Modal Execution 

This operator supplies an Operator.modal function that keeps getting run to process events until it returns {'FINISHED'} or {'CANCELLED'} .

A modal operator fires each time a fresh event arrives, like a mouse click or a key press; when nothing new comes in, it stays idle. They shine in interactive tools, where the operator can hold its own state and let keys flip options while it runs. Grab, Rotate, Scale, and Fly-Mode are all modal operators.

Operator.invoke kicks the operator into its active state by returning {'`RUNNING_MODAL`'} , which starts the modal loop.

Observe that __init__() and __del__() are declared. They aren't worth much for other operator kinds, but for modal operators they run before Operator.invoke and again once the operator wraps up. The class construction and destruction section has more on this.

```python
import bpy

class ModalOperator(bpy.types.Operator):
    bl_idname = "object.modal_operator"
    bl_label = "Simple Modal Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Start")

    def __del__(self):
        print("End")
        super().__del__()

    def execute(self, context):
        context.object.location.x = self.value / 100.0
        return {'FINISHED'}

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':  # Apply.
            self.value = event.mouse_x
            self.execute(context)
        elif event.type == 'LEFTMOUSE':  # Confirm.
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:  # Cancel.
            ### Revert all changes that have been made
            context.object.location.x = self.init_loc_x
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.init_loc_x = context.object.location.x
        self.value = event.mouse_x
        self.execute(context)

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(ModalOperator.bl_idname, text="Modal Operator")

### Register and add to the object menu (required to also use F3 search "Modal Operator" for quick access).
bpy.utils.register_class(ModalOperator)
bpy.types.VIEW3D_MT_object.append(menu_func)

### Test call.
bpy.ops.object.modal_operator('INVOKE_DEFAULT')
```

[Related references](INDEX.md).
