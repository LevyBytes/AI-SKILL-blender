# bpy.types.BlendDataWorlds

new(name)

Builds and stores a world in the main database.

Parameters:
- name (str) – World identifier (cannot be None)

Returns:
New world data-block

Return type:
World
remove(world, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Takes away a world from the blend file.

Parameters:
- world (World) – World to take away (cannot be None)
- do_unlink (bool) – Detach references before removal (optional)
- do_id_user (bool) – Lower user totals in all dependent items (optional)
- do_ui_user (bool) – Sever UI associations (optional)
tag(value)

Attach metadata.

Parameters:
- value (bool) – Tag flag
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – Designation of the RNA type.
- default (bpy.types.Struct | None) – Alternative if absent.

Returns:
The RNA type or alternative.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – Designation of the RNA type.
- default (type | None) – Alternative if absent.

Returns:
The class or alternative.

Return type:
type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| BlendData.worlds | |
## BlendDataWorlds(bpy_prop_collection)

### BlendDataWorlds(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types.BlendDataWorlds(bpy_prop_collection)

Manages the collection of world environment data.

[Related references](INDEX.md).
