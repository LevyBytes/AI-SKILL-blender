# bpy.types.VectorFont

filepath 

(default "", never None, blend relative // prefix supported)

Type :

str
packed_file 

(readonly)

Type :

PackedFile
pack ( ) 

Embed the font inside the current blend file
unpack ( * , method = '`USE_LOCAL`' ) 

Extract the font to the samples filename

Parameters :

method (Literal[Unpack Method Items]) – method, The unpacking strategy (optional)
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data ID.name ID.name_full ID.id_type ID.session_uid ID.is_evaluated ID.original ID.users ID.use_fake_user ID.use_extra_user ID.is_embedded_data | ID.is_linked_packed ID.is_missing ID.is_runtime_data ID.is_editable ID.tag ID.is_library_indirect ID.library ID.library_weak_reference ID.asset_data ID.override_library ID.preview |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors | bpy_struct.type_recast bpy_struct.values ID.bl_system_properties_get ID.rename ID.evaluated_get ID.copy ID.asset_mark ID.asset_clear ID.asset_generate_preview ID.override_create ID.override_hierarchy_create ID.user_clear ID.user_remap ID.make_local ID.user_of_id ID.animation_data_create ID.animation_data_clear ID.update_tag ID.preview_ensure ID.bl_rna_get_subclass ID.bl_rna_get_subclass_py |
### References 

| Description | Description |
| --- | --- |
| BlendData.fonts BlendDataFonts.load BlendDataFonts.remove NodeSocketFont.default_value NodeTreeInterfaceSocketFont.default_value | TextCurve.font TextCurve.font_bold TextCurve.font_bold_italic TextCurve.font_italic TextStrip.font |
## VectorFont(ID)

### VectorFont(ID) 

base classes — bpy_struct, ID
class bpy.types. VectorFont ( ID ) 

A vector typeface used by Text objects
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)

[Related references](INDEX.md).
