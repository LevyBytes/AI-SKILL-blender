# bpy.types.Depsgraph: new_from_object

### Dependency graph: bpy.data.meshes.new_from_object()

A helper that produces a fresh mesh copied from any object with geometry. The mesh joins the main
database and other objects may reference it. It’s the usual choice for tools that spawn new objects
or bake modifiers down.

Called on the original object, the mesh is built without animation or modifiers folded in:

- With a mesh, the outcome is close to making a copy of the original.

- With a curve, its own modifiers are skipped, as are the modifiers on whatever objects serve as bevel and taper.

- With a meta-ball, the result is empty, because turning it into polygons happens during modifier evaluation.

Called on the evaluated object, every modifier is included.

Every link the mesh holds — materials among them — is pointed back to the original, which keeps the
main database valid and coherent.

Note

When the object carries no geometry (a camera, say), the function hands back None.

```python
import bpy

class OBJECT_OT_mesh_from_object(bpy.types.Operator):
    """Convert selected object to mesh and show number of vertices"""
    bl_label = "DEG Mesh From Object"
    bl_idname = "object.mesh_from_object"

    def execute(self, context):
        ### Access input original object.
        obj = context.object
        if obj is None:
            self.report({'INFO'}, "No active mesh object to convert to mesh")
            return {'CANCELLED'}
        ### Avoid annoying None checks later on.
        if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
            self.report({'INFO'}, "Object cannot be converted to mesh")
            return {'CANCELLED'}
        depsgraph = context.evaluated_depsgraph_get()
        object_eval = obj.evaluated_get(depsgraph)
        mesh_from_eval = bpy.data.meshes.new_from_object(object_eval)
        self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh, and is ready for use!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_mesh_from_object)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_mesh_from_object)

if __name__ == "__main__":
    register()
```

[Related references](INDEX.md).
