# bpy.ops.wm.alembic_import

bpy.ops.wm. alembic_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = True , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.abc' , scale = 1.0 , set_frame_range = True , validate_meshes = False , always_add_cache_reader = False , is_sequence = False , as_background_job = False ) 

Reads an Alembic archive

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

- relative_path ( bool ) - Relative Path, Chooses the file location relative to the .blend project (optional)

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

- scale ( float ) - Scale, Factor to enlarge or reduce geometry relative to world space (in [0.0001, 1000], optional)

- set_frame_range ( bool ) - Set Frame Range, If turned on, modifies composition start/end frames to align with the archive (optional)

- validate_meshes ( bool ) - Validate Meshes, Guarantees the structure is sound (when disabled, geometry might be imported causing application crashes during display or modification) (optional)

- always_add_cache_reader ( bool ) - Always Add Cache Reader, Assigns cache modifiers and constraints to imported geometry regardless of animation so modifications apply when reloading the archive (optional)

- is_sequence ( bool ) - Is Sequence, Specifies whether the cache is separated into discrete files (optional)

- as_background_job ( bool ) - Run as Background Job, Allows the export to execute in the background without blocking Blender. This functionality is superseded; EXECUTE to run in the foreground, and INVOKE to run as a background operation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
