# bpy.types.BlendDataVolumes

new(name)

Creates and registers a volume in the main database.

Parameters:
- name (str) – Volume identifier (cannot be None)

Returns:
New volume data-block

Return type:
Volume
remove(volume, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Destroys a volume from the blend file.

Parameters:
- volume (Volume) – Volume to destroy (cannot be None)
- do_unlink (bool) – Sever all connections before destruction (WARNING: will also delete objects instancing that volume data) (optional)
- do_id_user (bool) – Lower user counts in dependent blocks (optional)
- do_ui_user (bool) – Strip UI connections (optional)
tag(value)

Mark with metadata.

Parameters:
- value (bool) – Tag indicator
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – Name of the RNA type.
- default (bpy.types.Struct | None) – Substitute when absent.

Returns:
The RNA type or substitute.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – Name of the RNA type.
- default (type | None) – Substitute when absent.

Returns:
The class or substitute.

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
| BlendData.volumes | |
## BlendDataVolumes(bpy_prop_collection)

### BlendDataVolumes(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types.BlendDataVolumes(bpy_prop_collection)

Stores volume data structures in the database.

[Related references](INDEX.md).
