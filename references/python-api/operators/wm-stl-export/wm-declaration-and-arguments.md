# bpy.ops.wm.stl_export: declaration-and-arguments

bpy.ops.wm. stl_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , ascii_format = False , use_batch = False , export_selected_objects = False , collection = '' , global_scale = 1.0 , use_scene_unit = False , forward_axis = 'Y' , up_axis = 'Z' , apply_modifiers = True , filter_glob = '*.stl' )
Saves the scene to an STL file.
Parameters:
- filepath ( str ) – File Path, Path to file (optional, never None)
- check_existing ( bool ) – Check Existing, Check and warn on overwriting existing files (optional)
- filter_blender ( bool ) – Filter .blend files, (optional)
- filter_backup ( bool ) – Filter backup .blend files, (optional)
- filter_image ( bool ) – Filter image files, (optional)
- filter_movie ( bool ) – Filter movie files, (optional)
- filter_python ( bool ) – Filter Python files, (optional)
- filter_font ( bool ) – Filter font files, (optional)
- filter_sound ( bool ) – Filter sound files, (optional)
- filter_text ( bool ) – Filter text files, (optional)
- filter_archive ( bool ) – Filter archive files, (optional)
- filter_btx ( bool ) – Filter btx files, (optional)
- filter_alembic ( bool ) – Filter Alembic files, (optional)
- filter_usd ( bool ) – Filter USD files, (optional)
- filter_obj ( bool ) – Filter OBJ files, (optional)
- filter_volume ( bool ) – Filter OpenVDB volume files, (optional)
- filter_folder ( bool ) – Filter folders, (optional)
- filter_blenlib ( bool ) – Filter Blender IDs, (optional)
- filemode ( int ) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file (in [1, 9], optional)
- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)
- DEFAULT — Default: automatically determine the display type for files.
- `LIST_VERTICAL` — Short List: display files as a short list.
- `LIST_HORIZONTAL` — Long List: display files as a detailed list.
- THUMBNAIL — Thumbnails: display files as thumbnails.
- sort_method ( str ) – File sorting mode, (optional)
- ascii_format ( bool ) – ASCII Format, Export file in ASCII format, export as binary otherwise (optional)
- use_batch ( bool ) – Batch Export, Export each object to a separate file (optional)
- export_selected_objects ( bool ) – Export Selected Objects, Export only selected objects instead of all supported objects (optional)
- collection ( str ) – Source Collection, Export only objects from this collection (and its children) (optional, never None)
- global_scale ( float ) – Scale, (in [1e-06, 1e+06], optional)
- use_scene_unit ( bool ) – Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data (optional)
- forward_axis ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Forward Axis, (optional)
- X — X: positive X axis.
- Y — Y: positive Y axis.
- Z — Z: positive Z axis.
- `NEGATIVE_X` — -X: negative X axis.
- `NEGATIVE_Y` — -Y: negative Y axis.
- `NEGATIVE_Z` — -Z: negative Z axis.
- up_axis ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Up Axis, (optional)
- X — X: positive X axis.
- Y — Y: positive Y axis.
- Z — Z: positive Z axis.
- `NEGATIVE_X` — -X: negative X axis.
- `NEGATIVE_Y` — -Y: negative Y axis.
- `NEGATIVE_Z` — -Z: negative Z axis.
- apply_modifiers ( bool ) – Apply Modifiers, Apply modifiers to exported meshes (optional)
- filter_glob ( str ) – Extension Filter, (optional, never None)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
