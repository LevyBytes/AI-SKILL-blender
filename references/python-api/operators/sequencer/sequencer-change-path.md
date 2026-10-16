# bpy.ops.sequencer.change_path

bpy.ops.sequencer.change_path(*, filepath='', directory='', files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_placeholders=False)

Change the file reference for a sequencer strip.

Parameters:

- filepath (str) – File Path, Source to the file (optional, never None)
- directory (str) – Directory, Containing folder of the file (optional, never None)
- files (bpy_prop_collection[OperatorFileListElement]) – Files, (optional)
- hide_props_region (bool) – Hide Operator Properties, Collapse the panel with operator options (optional)
- check_existing (bool) – Check Existing, Notify user before overwriting (optional)
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
- filemode (int) – File Browser Mode, Setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
- relative_path (bool) – Relative Path, Use path relative to the .blend file (optional)
- display_type (Literal['DEFAULT', '`LIST_VERTICAL`', '`LIST_HORIZONTAL`', 'THUMBNAIL']) – Display Type, (optional)
  - DEFAULT
    Default – Infer presentation from file types.
  - `LIST_VERTICAL`
    Short List – Compact file list view.
  - `LIST_HORIZONTAL`
    Long List – Comprehensive file list view.
  - THUMBNAIL
    Thumbnails – Picture previews.
- sort_method (str) – File sorting mode, (optional)
- use_placeholders (bool) – Use Placeholders, Generate placeholder images for missing sequence frames (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
