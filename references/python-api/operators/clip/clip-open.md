# bpy.ops.clip.open

bpy.ops.clip. open ( * , directory = '' , files = None , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' )

Import a sequence or video file

Parameters :

- directory ( str ) – Directory, Directory of the file (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

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
- show_multiview ( bool ) – Enable Multi-View, (optional)

- use_multiview ( bool ) – Use Multi-View, (optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Automatically determine display type for files.

- `LIST_VERTICAL`
Short List – Display files as short list.

- `LIST_HORIZONTAL`
Long List – Display files as a detailed list.

- THUMBNAIL
Thumbnails – Display files as thumbnails.

- sort_method ( Literal [ 'DEFAULT' , '`FILE_SORT_ALPHA`' , '`FILE_SORT_EXTENSION`' , '`FILE_SORT_TIME`' , '`FILE_SORT_SIZE`' , '`ASSET_CATALOG`' ] ) – File sorting mode, (optional)

- DEFAULT
Default – Automatically determine sort method for files.

- `FILE_SORT_ALPHA`
Name – Sort the file list alphabetically.

- `FILE_SORT_EXTENSION`
Extension – Sort the file list by extension/type.

- `FILE_SORT_TIME`
Modified Date – Sort files by modification time.

- `FILE_SORT_SIZE`
Size – Sort files by size.

- `ASSET_CATALOG`
Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
