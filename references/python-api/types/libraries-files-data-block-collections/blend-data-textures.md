# bpy.types.BlendDataTextures

new(name, type)

Instantiates and stores a texture in the main database.

Parameters:
- name (str) – Texture identifier (cannot be None)
- type (Literal[Texture Type Items]) – Texture category; determines the texture subtype to instantiate

Returns:
New texture data-block

Return type:
Texture
remove(texture, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Purges a texture from the blend file.

Parameters:
- texture (Texture) – Texture to purge (cannot be None)
- do_unlink (bool) – Sever all references before removal (optional)
- do_id_user (bool) – Decrement user counts across linked items (optional)
- do_ui_user (bool) – Expunge UI associations (optional)
tag(value)

Stamp with metadata.

Parameters:
- value (bool) – Tag indicator
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – The RNA class identifier.
- default (bpy.types.Struct | None) – Alternate when not found.

Returns:
The RNA type or alternate.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – The RNA class identifier.
- default (type | None) – Alternate when not found.

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
| BlendData.textures | |
## BlendDataTextures(bpy_prop_collection)

### BlendDataTextures(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types.BlendDataTextures(bpy_prop_collection)

Manages texture data blocks within Blender.

[Related references](INDEX.md).
