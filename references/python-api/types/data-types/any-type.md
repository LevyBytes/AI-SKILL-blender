# bpy.types.AnyType

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
| bpy_struct.id_data | |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References 

| Members | Members |
| --- | --- |
| bpy.context.property BoneCollection.assign BoneCollection.unassign FCurve.update_autoflags Gizmo.target_set_prop KeyingSetInfo.generate Region.data UILayout.context_pointer_set UILayout.enum_item_description UILayout.enum_item_icon UILayout.enum_item_name UILayout.icon UILayout.panel_prop UILayout.prop UILayout.prop_decorator UILayout.prop_enum UILayout.prop_menu_enum UILayout.prop_search UILayout.prop_search UILayout.prop_tabs_enum UILayout.prop_tabs_enum UILayout.prop_with_menu UILayout.prop_with_popover UILayout.props_enum UILayout.template_ID UILayout.template_ID_preview UILayout.template_ID_session_uid UILayout.template_ID_tabs UILayout.template_any_ID UILayout.template_cache_file UILayout.template_cache_file_layers UILayout.template_cache_file_time_settings UILayout.template_cache_file_velocity | UILayout.template_color_picker UILayout.template_color_ramp UILayout.template_colormanaged_view_settings UILayout.template_colorspace_settings UILayout.template_component_menu UILayout.template_curve_mapping UILayout.template_curveprofile UILayout.template_greasepencil_color UILayout.template_histogram UILayout.template_icon_view UILayout.template_image UILayout.template_layers UILayout.template_layers UILayout.template_light_linking_collection UILayout.template_list UILayout.template_list UILayout.template_marker UILayout.template_matrix UILayout.template_movieclip UILayout.template_movieclip_information UILayout.template_palette UILayout.template_path_builder UILayout.template_search UILayout.template_search UILayout.template_search_preview UILayout.template_search_preview UILayout.template_track UILayout.template_vectorscope UILayout.template_waveform UIList.draw_item UIList.draw_item UIList.draw_item UIList.filter_items |
## AnyType(bpy_struct)

A marker for any data type.

base class — bpy_struct
class bpy.types. AnyType ( bpy_struct )

RNA type that permits references to any data block.

[Related references](INDEX.md).
