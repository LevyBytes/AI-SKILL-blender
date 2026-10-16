# bpy.types.Depsgraph: Dependency graph: Iterate over all object instances

### Dependency graph: Iterate over all object instances

There are times you need every instance together with its matrix — writing an exporter or a
custom render engine, for instance.
The example walks through every object and instance present in the scene.

```python
import bpy

class OBJECT_OT_object_instances(bpy.types.Operator):
    """Access original object and do something with it"""
    bl_label = "DEG Iterate Object Instances"
    bl_idname = "object.object_instances"

    def execute(self, context):
        depsgraph = context.evaluated_depsgraph_get()
        for object_instance in depsgraph.object_instances:
            ### This is an object which is being instanced.
            obj = object_instance.object
            ### `is_instance` denotes whether the object is coming from instances (as an opposite of
            ### being an emitting object. )
            if not object_instance.is_instance:
                print(f"Object {obj.name} at {object_instance.matrix_world}")
            else:
                ### Instanced will additionally have fields like uv, random_id and others which are
                ### specific for instances. See Python API for DepsgraphObjectInstance for details,
                print(f"Instance of {obj.name} at {object_instance.matrix_world}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_instances)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_instances)

if __name__ == "__main__":
    register()
```

[Related references](INDEX.md).
