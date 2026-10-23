# bpy.types.BlendDataWorkSpaces

tag(value)

Assign metadata.

Parameters:
- value (bool) – Tag status
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – Name of the RNA type.
- default (bpy.types.Struct | None) – Return if not discovered.

Returns:
The RNA type or return value.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – Name of the RNA type.
- default (type | None) – Return if not discovered.

Returns:
The class or return value.

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
| BlendData.workspaces | |
## BlendDataWorkSpaces(bpy_prop_collection)

### BlendDataWorkSpaces(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types.BlendDataWorkSpaces(bpy_prop_collection)

Provides access to workspace data structures.

[Related references](INDEX.md).
