# bpy.ops.wm.obj_export: declaration-and-arguments

bpy.ops.wm. obj_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , export_animation = False , start_frame = -2147483648 , end_frame = 2147483647 , forward_axis = '`NEGATIVE_Z`' , up_axis = 'Y' , global_scale = 1.0 , apply_modifiers = True , apply_transform = True , export_eval_mode = '`DAG_EVAL_VIEWPORT`' , export_selected_objects = False , export_uv = True , export_normals = True , export_colors = False , export_materials = True , export_pbr_extensions = False , path_mode = 'AUTO' , export_triangulated_mesh = False , export_curves_as_nurbs = False , export_object_groups = False , export_material_groups = False , export_vertex_groups = False , export_smooth_groups = False , smooth_group_bitflags = False , filter_glob = '*.obj;*.mtl' , collection = '' ) 

Exports the scene to a Wavefront OBJ file

Parameters :

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

- DEFAULT
Default – Automatically determine display type for files.

- `LIST_VERTICAL`
Short List – Display files as short list.

- `LIST_HORIZONTAL`
Long List – Display files as a detailed list.

- THUMBNAIL
Thumbnails – Display files as thumbnails.

- sort_method ( str ) – File sorting mode, (optional)

[Related references](INDEX.md).
