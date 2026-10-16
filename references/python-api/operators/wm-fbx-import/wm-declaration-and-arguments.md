# bpy.ops.wm.fbx_import: declaration-and-arguments

bpy.ops.wm. fbx_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , mtl_name_collision_mode = '`MAKE_UNIQUE`' , import_colors = 'SRGB' , use_custom_normals = True , use_custom_props = True , use_custom_props_enum_as_string = True , import_subdivision = False , ignore_leaf_bones = False , validate_meshes = True , use_anim = True , anim_offset = 1.0 , filter_glob = '*.fbx' ) 

Ingests an FBX file into the current composition

Parameters :

- filepath ( str ) - File Path, Destination file path (optional, never None)

- directory ( str ) - Directory, Folder containing the file (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) - Files, (optional)

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

[Related references](INDEX.md).
