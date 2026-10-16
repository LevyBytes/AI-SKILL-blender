# bpy.ops.font.text_paste_from_file

bpy.ops.font.text_paste_from_file(*, filepath='', hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=True, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, display_type='DEFAULT', sort_method='')

Restore material from a record

Parameters:

- filepath (str) – File Path, Course to source (optional, never None)
- hide_props_region (bool) – Hide Operator Properties, Fold the pane showing the task configuration (optional)
- check_existing (bool) – Check Existing, Inspect and notify if over-writing current materials (optional)
- filter_blender (bool) – Filter .blend files, (optional)
- filter_backup (bool) – Filter backup .blend files, (optional)
- filter_image (bool) – Filter image files, (optional)
- filter_movie (bool) – Filter movie files, (optional)
- filter_python (bool) – Filter Python files, (optional)
- filter_font (bool) – Filter font files, (optional)
- filter_sound (bool) – Filter sound files, (optional)
- filter_text (bool) – Filter text files, (optional)
- filter_archive (bool) – Filter archive files, (optional)
- filter_btx (bool) – Filter btx files, (optional)
- filter_alembic (bool) – Filter Alembic files, (optional)
- filter_usd (bool) – Filter USD files, (optional)
- filter_obj (bool) – Filter OBJ files, (optional)
- filter_volume (bool) – Filter OpenVDB volume files, (optional)
- filter_folder (bool) – Filter folders, (optional)
- filter_blenlib (bool) – Filter Blender IDs, (optional)
- filemode (int) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
- display_type (Literal['DEFAULT', '`LIST_VERTICAL`', '`LIST_HORIZONTAL`', 'THUMBNAIL']) – Display Type, (optional)

- DEFAULT
Default – Automatically determine display type for files.

- `LIST_VERTICAL`
Short List – Display files as short list.

- `LIST_HORIZONTAL`
Long List – Display files as a detailed list.

- THUMBNAIL
Thumbnails – Display files as thumbnails.

- sort_method (str) – File sorting mode, (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
