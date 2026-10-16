# bpy.types.Operator: Modifying Blender Data & Undo

### Modifying Blender Data & Undo 

Whenever an operator changes Blender data it should switch on the 'UNDO' option. With that set, Blender records an undo step on its own once the operator's execute (or invoke , covered below) finishes and returns {'FINISHED'} .

Without it, no undo step gets recorded, which at minimum corrupts the undo stack and puzzles the user (since the operator's edits may be un-undoable, or may be rolled back along with unrelated earlier changes). In plenty of situations this even ends in data corruption and crashes.

Keep in mind that returning {'CANCELLED'} records no undo step. So when something goes wrong after data has already been changed, returning {'FINISHED'} is the safer choice — unless you can completely roll the changes back beforehand.

Note

Hardly any example on this page edits Blender data, which is why leaving the default bl_options value on these operators is safe.

Note

A few involved scenarios go beyond what the automatic exit-time undo step covers — for instance an operator that switches modes, or that fires off other operators which each need their own undo step.

You can issue such a manual undo push with the bpy.ops.ed.undo_push function. Tread carefully, though: it is an advanced feature that calls for some grasp of how Blender's undo system actually works internally.

```python
import bpy

class DataEditOperator(bpy.types.Operator):
    bl_idname = "object.data_edit"
    bl_label = "Data Editing Operator"
    ### The default value is only 'REGISTER', 'UNDO' is mandatory when Blender data is modified
    ### (and does require 'REGISTER' as well).
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.object.location.x += 1.0
        return {'FINISHED'}

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(DataEditOperator.bl_idname, text="Blender Data Editing Operator")

### Register.
bpy.utils.register_class(DataEditOperator)
bpy.types.VIEW3D_MT_view.append(menu_func)

### Test call to the newly defined operator.
bpy.ops.object.data_edit()
```

[Related references](INDEX.md).
