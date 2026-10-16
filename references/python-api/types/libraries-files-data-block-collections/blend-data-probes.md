# bpy.types.BlendDataProbes

new(name, type)

Creates and adds a light probe to Blender's database.

Parameters:
- name (str) – Probe name (cannot be None)
- type (Literal[Lightprobes Type Items]) – Probe classification; specifies which probe subtype to instantiate

Returns:
New light probe data-block

Return type:
LightProbe
remove(lightprobe, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Destroys a light probe from the blend file.

Parameters:
- lightprobe (LightProbe) – Probe to destroy (cannot be None)
- do_unlink (bool) – Separate all connections before destruction (WARNING: will also delete objects instancing that light probe data) (optional)
- do_id_user (bool) – Update user counts in dependent structures (optional)
- do_ui_user (bool) – Remove interface linkages (optional)
tag(value)

Mark with a tag.

Parameters:
- value (bool) – Tag flag
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – RNA identifier.
- default (bpy.types.Struct | None) – Return if not found.

Returns:
The RNA type or return value.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – RNA identifier.
- default (type | None) – Return if not found.

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
| BlendData.lightprobes | |
## BlendDataProbes(bpy_prop_collection)

### BlendDataProbes(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types.BlendDataProbes(bpy_prop_collection)

Stores a collection of light probe instances.

[Related references](INDEX.md).
