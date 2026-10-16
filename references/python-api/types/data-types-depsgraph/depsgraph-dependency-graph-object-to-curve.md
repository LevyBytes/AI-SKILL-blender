# bpy.types.Depsgraph: to_curve

### Dependency graph: Object.to_curve()

A helper that pulls a curve out of text and curve objects. Exporters, render engines, and tools
that need the curve standing in for the object typically use it.

It expects the evaluated dependency graph as a mandatory argument, plus an optional boolean
apply_modifiers that defaults to false. With apply_modifiers set and a curve object, the spline
deform modifiers act on the control points. Bear in mind that constructive modifiers and ones that
aren’t spline-enabled stay off — so Array won’t run, nor will deform modifiers whose Apply On Spline
option is switched off.

Given a text object, the text becomes a 3D curve and is returned. apply_modifiers carries no weight
for text objects since modifiers never run on them. Hand in anything other than a curve or a text
object and the call reports an error.

Note

The object owns the curve that comes back. Release it through to_curve_clear().

Note

Treat the resulting curve as throwaway; it can’t be referenced from objects in the main
database.

```python
import bpy

class OBJECT_OT_object_to_curve(bpy.types.Operator):
    """Convert selected object to curve and show number of splines"""
    bl_label = "DEG Object to Curve"
    bl_idname = "object.object_to_curve"

    def execute(self, context):
        ### Access input original object.
        obj = context.object
        if obj is None:
            self.report({'INFO'}, "No active object to convert to curve")
            return {'CANCELLED'}
        if obj.type not in {'CURVE', 'FONT'}:
            self.report({'INFO'}, "Object cannot be converted to curve")
            return {'CANCELLED'}
        depsgraph = context.evaluated_depsgraph_get()
        ### Invoke to_curve() without applying modifiers.
        curve_without_modifiers = obj.to_curve(depsgraph)
        self.report({'INFO'}, f"{len(curve_without_modifiers.splines)} splines in a new curve without modifiers.")
        ### Remove temporary curve.
        obj.to_curve_clear()
        ### Invoke to_curve() with applying modifiers.
        curve_with_modifiers = obj.to_curve(depsgraph, apply_modifiers=True)
        self.report({'INFO'}, f"{len(curve_with_modifiers.splines)} splines in new curve with modifiers.")
        ### Remove temporary curve.
        obj.to_curve_clear()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_to_curve)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_to_curve)

if __name__ == "__main__":
    register()
```

base class — bpy_struct

[Related references](INDEX.md).
