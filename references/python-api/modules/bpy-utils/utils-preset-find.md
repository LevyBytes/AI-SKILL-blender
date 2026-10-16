# bpy.utils: bpy.utils. preset_find ( name , preset_path , * , display_name = False , ext = '.py' )

bpy.utils. preset_find ( name , preset_path , * , display_name = False , ext = '.py' ) 

Look up a preset by its name.

Parameters :

- name ( str ) – The preset name.

- preset_path ( str ) – The preset subdirectory (e.g. "keyconfig" ).

- display_name ( bool ) – If True, match against the display name rather than the filename.

- ext ( str ) – The file extension for the preset.

Returns :

The file path of the preset or None if not found.

Return type :

str | None

[Related references](INDEX.md).
