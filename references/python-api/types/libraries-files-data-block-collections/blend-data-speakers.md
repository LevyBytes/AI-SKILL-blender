# bpy.types.BlendDataSpeakers

new(name)

Generates a speaker object and registers it in the main database.

Parameters:
- name (str) – Speaker identifier (cannot be None)

Returns:
New speaker data-block

Return type:
Speaker
remove(speaker, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Discards a speaker object from the blend file.

Parameters:
- speaker (Speaker) – Speaker to discard (cannot be None)
- do_unlink (bool) – Break all connections before disposal (WARNING: will also delete objects instancing that speaker data) (optional)
- do_id_user (bool) – Update user totals in dependent structures (optional)
- do_ui_user (bool) – Wipe interface references (optional)
tag(value)

Append a tag.

Parameters:
- value (bool) – Tag state
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – RNA class designation.
- default (bpy.types.Struct | None) – Alternate if missing.

Returns:
The RNA type or alternate.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – RNA class designation.
- default (type | None) – Alternate if missing.

Returns:
The class or alternate.

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
| BlendData.speakers | |
## BlendDataSpeakers(bpy_prop_collection)

### BlendDataSpeakers(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types.BlendDataSpeakers(bpy_prop_collection)

Manages speaker object data within the database.

[Related references](INDEX.md).
