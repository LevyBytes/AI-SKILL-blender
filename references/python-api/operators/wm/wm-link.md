# bpy.ops.wm.link

bpy.ops.wm. link ( * , filepath = '' , directory = '' , filename = '' , files = None , check_existing = False , filter_blender = True , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = True , filemode = 1 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , link = True , do_reuse_local_id = False , clear_asset_data = False , autoselect = True , active_collection = True , instance_collections = True , instance_object_data = True )
Create a link from a Library .blend file

Parameters :

- filepath ( str ) – File Path, The location of the file (optional, never None)

- directory ( str ) – Directory, Where the file is stored (optional, never None)

- filename ( str ) – File Name, The name of the target file (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

- check_existing ( bool ) – Check Existing, Verifies and alerts when about to overwrite current files (optional)

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

- link ( bool ) – Link, Bring in objects or data-blocks via linking as opposed to duplication (optional)

- do_reuse_local_id ( bool ) – Re-Use Local Data, Make use of existing previously-matched appended data-blocks rather than adding fresh ones (optional)

- clear_asset_data ( bool ) – Clear Asset Data, Strip asset metadata and tags from the original data-block (optional)

- autoselect ( bool ) – Select, Choose new objects (optional)

- active_collection ( bool ) – Active Collection, Add new objects to the active collection (optional)

- instance_collections ( bool ) – Instance Collections, Make instances from collections as opposed to placing them into the scene directly (optional)

- instance_object_data ( bool ) – Instance Object Data, Create instances when object data are unreferenced by any objects (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
