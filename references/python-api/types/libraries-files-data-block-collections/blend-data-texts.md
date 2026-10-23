# bpy.types.BlendDataTexts

new(name)

Constructs a text block and adds it to the main database.

Parameters:
- name (str) – Block identifier (cannot be None)

Returns:
New text data-block

Return type:
Text
remove(text, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Removes a text block from the blend file.

Parameters:
- text (Text) – Text block to remove (cannot be None)
- do_unlink (bool) – Disconnect all usages before removal (optional)
- do_id_user (bool) – Reduce counts in linked data-blocks (optional)
- do_ui_user (bool) – Clear UI associations (optional)
load(filepath, *, internal=False)

Reads a text file into Blender's text block storage.

Parameters:
- filepath (str) – file system path (cannot be None, blend relative // prefix supported)
- internal (bool) – Store as internal; Embed file within the blend file (optional)

Returns:
New text data-block

Return type:
Text
tag(value)

Label with a tag.

Parameters:
- value (bool) – Tag flag
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – The RNA type name.
- default (bpy.types.Struct | None) – Fallback when not available.

Returns:
The RNA type or fallback.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – The RNA type name.
- default (type | None) – Fallback when not available.

Returns:
The class or fallback.

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
| BlendData.texts | |
## BlendDataTexts(bpy_prop_collection)

### BlendDataTexts(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types.BlendDataTexts(bpy_prop_collection)

Provides access to text block resources in the database.

[Related references](INDEX.md).
