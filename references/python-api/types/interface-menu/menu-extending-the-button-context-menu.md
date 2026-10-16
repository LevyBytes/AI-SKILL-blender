# bpy.types.Menu: Extending the Button Context Menu

### Extending the Button Context Menu

With this approach you can add a custom entry to the right-click menu that pops up whenever the cursor is over a UI button (an operator, a value field, a color, a string, and so on).

For the example to run, select an object first, then right-click on some interface widget — perhaps a color in the material properties — and pick Execute Custom Action.

Running the operator prints every value out.

```python
import bpy

def dump(obj, text):
    for attr in dir(obj):
        print("{!r}.{:s} = {!s}".format(obj, attr, getattr(obj, attr)))

class WM_OT_button_context_test(bpy.types.Operator):
    """Right click entry test"""
    bl_idname = "wm.button_context_test"
    bl_label = "Run Context Test"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        value = getattr(context, "button_pointer", None)
        if value is not None:
            dump(value, "button_pointer")

        value = getattr(context, "button_prop", None)
        if value is not None:
            dump(value, "button_prop")

        value = getattr(context, "button_operator", None)
        if value is not None:
            dump(value, "button_operator")

        return {'FINISHED'}

def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(WM_OT_button_context_test.bl_idname)

def register():
    bpy.utils.register_class(WM_OT_button_context_test)
    bpy.types.UI_MT_button_context_menu.append(draw_menu)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_menu)
    bpy.utils.unregister_class(WM_OT_button_context_test)

if __name__ == "__main__":
    register()
```

base class — bpy_struct

[Related references](INDEX.md).
