# bpy.types.FileAssetSelectParams: methods

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
| bpy_struct.id_data FileSelectParams.title FileSelectParams.directory FileSelectParams.filename FileSelectParams.use_library_browsing FileSelectParams.display_type FileSelectParams.recursion_level FileSelectParams.show_details_size FileSelectParams.show_details_datetime FileSelectParams.use_filter FileSelectParams.show_hidden FileSelectParams.sort_method FileSelectParams.use_sort_invert FileSelectParams.use_filter_image FileSelectParams.use_filter_blender FileSelectParams.use_filter_backup | FileSelectParams.use_filter_movie FileSelectParams.use_filter_script FileSelectParams.use_filter_font FileSelectParams.use_filter_sound FileSelectParams.use_filter_text FileSelectParams.use_filter_volume FileSelectParams.use_filter_folder FileSelectParams.use_filter_blendid FileSelectParams.use_filter_asset_only FileSelectParams.filter_id FileSelectParams.filter_glob FileSelectParams.filter_search FileSelectParams.display_size FileSelectParams.display_size_discrete FileSelectParams.list_display_size FileSelectParams.list_column_size |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values FileSelectParams.bl_rna_get_subclass FileSelectParams.bl_rna_get_subclass_py |

[Related references](INDEX.md).
