# bpy.types.Macro: overview

class bpy.types. Macro ( bpy_struct )

Holds a macro operator while it runs, or after it has been registered post-execution.
## Macro(bpy_struct)

### Macro(bpy_struct)
### Example Macro

The snippet below builds a small macro operator that first translates the active object and then spins it.
It shows:

- Defining a macro operator class.

- Registering it and defining sub-operators.

- Setting property values for each step.

```python
import bpy

class OBJECT_OT_simple_macro(bpy.types.Macro):
    bl_idname = "object.simple_macro"
    bl_label = "Simple Transform Macro"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

def register():
    bpy.utils.register_class(OBJECT_OT_simple_macro)

    ### Define steps after registration and set operator values via .properties
    step = OBJECT_OT_simple_macro.define("transform.translate")
    props = step.properties
    props.value = (1.0, 0.0, 0.0)
    props.constraint_axis = (True, False, False)

    step = OBJECT_OT_simple_macro.define("transform.rotate")
    props = step.properties
    props.value = 0.785398  # 45 degrees in radians
    props.orient_axis = 'Z'

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_simple_macro)

if __name__ == "__main__":
    register()

    ### To run the macro:
    bpy.ops.object.simple_macro()
```

base class: bpy_struct

[Related references](INDEX.md).
