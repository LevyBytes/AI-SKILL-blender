# bpy.types.Depsgraph: to_mesh

### Dependency graph: Object.to_mesh()

A helper that pulls a mesh out of any object carrying geometry. Exporters, render engines, and
tools that want the evaluated mesh as it appears in the viewport reach for it.

Object.to_mesh() is tightly bound to the dependency graph: whether you call it on an original or
an evaluated object changes what you get back.

Called on the original object, the mesh is built without animation or modifiers folded in:

- A mesh comes back roughly as if the source had been duplicated.

- A curve turns off its own modifiers along with those on the objects acting as its bevel and taper.

- A meta-ball yields nothing but an empty mesh, since the polygonization step runs as part of modifier evaluation.

Called on the evaluated object, every modifier is included.

Note

The object owns the resulting mesh. Release it with to_mesh_clear().

Note

Treat the returned mesh as throwaway; it can’t be linked from objects in the main database. For
something that needs to stick around, reach for new_from_object()
instead.

Note

When the object carries no geometry (a camera, say), the function hands back None.

```python
import bpy

class OBJECT_OT_object_to_mesh(bpy.types.Operator):
    """Convert selected object to mesh and show number of vertices"""
    bl_label = "DEG Object to Mesh"
    bl_idname = "object.object_to_mesh"

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
        ### Invoke to_mesh() for original object.
        mesh_from_orig = obj.to_mesh()
        self.report({'INFO'}, f"{len(mesh_from_orig.vertices)} in new mesh without modifiers.")
        ### Remove temporary mesh.
        obj.to_mesh_clear()
        ### Invoke to_mesh() for evaluated object.
        object_eval = obj.evaluated_get(depsgraph)
        mesh_from_eval = object_eval.to_mesh()
        self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh with modifiers.")
        ### Remove temporary mesh.
        object_eval.to_mesh_clear()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_to_mesh)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_to_mesh)

if __name__ == "__main__":
    register()
```

[Related references](INDEX.md).
