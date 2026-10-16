# bpy.ops.wm.stl_import: stl_import declaration and file selection

bpy.ops.wm. stl_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , use_scene_unit = False , use_facet_normal = False , forward_axis = 'Y' , up_axis = 'Z' , use_mesh_validate = True , filter_glob = '*.stl' )

Bring in an STL file as an object

Parameters :

- filepath ( str ) – File Path, Location to the file (optional, never None)

- directory ( str ) – Directory, Folder of the file (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

- check_existing ( bool ) – Check Existing, Verify and caution when writing over files (optional)

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

- filemode ( int ) – File Browser Mode, Settings for the file browser type to open a .blend file, a library or particular file (in [1, 9], optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Determine display format for files automatically.

- `LIST_VERTICAL`
Short List – Show files in a concise list arrangement.

- `LIST_HORIZONTAL`
Long List – Show files with more information in a detailed layout.

- THUMBNAIL
Thumbnails – Show files as image previews.

- sort_method ( str ) – File sorting mode, (optional)

[Related references](INDEX.md).
