# bpy.ops.object.empty_image_add: empty_image_add declaration and file selection

bpy.ops.object. empty_image_add ( * , filepath = '' , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , name = '' , session_uid = 0 , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) , background = False ) 

Introduce a blank visual representation asset to environment with matter

Parameters :

- filepath ( str ) – File Path, Path to file (optional, never None)

- hide_props_region ( bool ) – Hide Operator Properties, Collapse the region displaying the operator settings (optional)

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

- relative_path ( bool ) – Relative Path, Select the file relative to the blend file (optional)

[Related references](INDEX.md).
