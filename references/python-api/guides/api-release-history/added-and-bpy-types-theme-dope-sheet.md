# API release history: Added, bpy.types.ThemeDopeSheet, Renamed, bpy.types.ThemePreferences, Added, bpy.types.ThemeView3D, Added, bpy.types.UILayout, Added, Function Arguments, bpy.types.UserAssetLibrary, Added, bpy.types.VIEWLAYER_UL_aov, Added, bpy.types.View3DOverlay, Added, bpy.types.Window, Added, bpy.types.WindowManager

#### Added 

- bpy.types.Strip.content_duration

- bpy.types.Strip.content_end

- bpy.types.Strip.content_start

- bpy.types.Strip.duration

- bpy.types.Strip.left_handle

- bpy.types.Strip.left_handle_offset

- bpy.types.Strip.right_handle

- bpy.types.Strip.right_handle_offset

### bpy.types.ThemeDopeSheet 

#### Renamed 

- interpolation_line -> bpy.types.ThemeDopeSheet.anim_interpolation_constant

- interpolation_line -> bpy.types.ThemeDopeSheet.anim_interpolation_linear

- interpolation_line -> bpy.types.ThemeDopeSheet.anim_interpolation_other

### bpy.types.ThemePreferences 

#### Added 

- bpy.types.ThemePreferences.match

### bpy.types.ThemeView3D 

#### Added 

- bpy.types.ThemeView3D.gp_wire_edit

- bpy.types.ThemeView3D.grid_major

### bpy.types.UILayout 

#### Added 

- bpy.types.UILayout.template_ID_session_uid

- bpy.types.UILayout.template_node_operator_registration_errors

#### Function Arguments 

- bpy.types.UILayout.popover (panel, text, text_ctxt, translate, icon, icon_value, direction), was (panel, text, text_ctxt, translate, icon, icon_value)

- bpy.types.UILayout.prop_tabs_enum (data, property, data_highlight, property_highlight, icon_only, expand_as), was (data, property, data_highlight, property_highlight, icon_only)

### bpy.types.UserAssetLibrary 

#### Added 

- bpy.types.UserAssetLibrary.enabled

### bpy.types.`VIEWLAYER_UL`_aov 

#### Added 

- bpy.types.`VIEWLAYER_UL`_aov.aov_icon

### bpy.types.View3DOverlay 

#### Added 

- bpy.types.View3DOverlay.show_performance

### bpy.types.Window 

#### Added 

- bpy.types.Window.find_playing_scene

### bpy.types.WindowManager

[Related references](INDEX.md).
