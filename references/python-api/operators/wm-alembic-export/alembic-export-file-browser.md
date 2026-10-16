# bpy.ops.wm.alembic_export: declaration and file browser options

bpy.ops.wm. alembic_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = True , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.abc' , start = -2147483648 , end = -2147483648 , xsamples = 1 , gsamples = 1 , sh_open = 0.0 , sh_close = 1.0 , selected = False , flatten = False , collection = '' , uvs = True , packuv = True , normals = True , vcolors = False , orcos = True , face_sets = False , subdiv_schema = False , apply_subdiv = False , curves_as_mesh = False , use_instancing = True , global_scale = 1.0 , triangulate = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , export_hair = True , export_particles = True , export_custom_properties = True , as_background_job = False , evaluation_mode = 'RENDER' , init_scene_frame_range = True ) 

Outputs the current scene as an Alembic archive

Parameters :

- filepath ( str ) - File Path, Destination file path (optional, never None)

- check_existing ( bool ) - Check Existing, Alerts and verifies before overwriting files (optional)

- filter_blender ( bool ) - Filter .blend files, (optional)

- filter_backup ( bool ) - Filter backup .blend files, (optional)

- filter_image ( bool ) - Filter image files, (optional)

- filter_movie ( bool ) - Filter movie files, (optional)

- filter_python ( bool ) - Filter Python files, (optional)

- filter_font ( bool ) - Filter font files, (optional)

- filter_sound ( bool ) - Filter sound files, (optional)

- filter_text ( bool ) - Filter text files, (optional)

- filter_archive ( bool ) - Filter archive files, (optional)

- filter_btx ( bool ) - Filter btx files, (optional)

- filter_alembic ( bool ) - Filter Alembic files, (optional)

- filter_usd ( bool ) - Filter USD files, (optional)

- filter_obj ( bool ) - Filter OBJ files, (optional)

- filter_volume ( bool ) - Filter OpenVDB volume files, (optional)

- filter_folder ( bool ) - Filter folders, (optional)

- filter_blenlib ( bool ) - Filter Blender IDs, (optional)

- filemode ( int ) - File Browser Mode, Browser configuration for loading .blend files, libraries, or specialized formats (in [1, 9], optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) - Display Type, (optional)

- DEFAULT
Default - Chooses display type based on file type.

- `LIST_VERTICAL`
Short List - Displays files in a compact list.

- `LIST_HORIZONTAL`
Long List - Displays files with comprehensive details.

- THUMBNAIL
Thumbnails - Displays files as preview icons.

- sort_method ( str ) - File sorting mode, (optional)

- filter_glob ( str ) - (optional, never None)

[Related references](INDEX.md).
