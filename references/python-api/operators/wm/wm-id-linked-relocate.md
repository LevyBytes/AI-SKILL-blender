# bpy.ops.wm.id_linked_relocate

bpy.ops.wm. id_linked_relocate ( * , id_session_uid = 0 , filepath = '' , directory = '' , filename = '' , check_existing = False , filter_blender = True , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = True , filemode = 1 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , link = True , do_reuse_local_id = False , clear_asset_data = False , autoselect = True , active_collection = False , instance_collections = False , instance_object_data = False )

Reorients a connected component, i.e. designates a replacement component to link, and adjusts its local uses to point to the newly linked component). Presently designed solely as an internal operation, not exposed in the user interface

Parameters :

- id_session_uid ( int ) - Linked ID Session UID, Distinctive runtime identifier for the connected component to reposition (in [0, inf], optional)

- filepath ( str ) - File Path, Destination file path (optional, never None)

- directory ( str ) - Directory, Folder containing the file (optional, never None)

- filename ( str ) - File Name, Title of the file (optional, never None)

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

- link ( bool ) - Link, Establishes connections to items or components rather than duplicating them (optional)

- do_reuse_local_id ( bool ) - Re-Use Local Data, Attempts to recycle previously matching imported components rather than importing a copy (optional)

- clear_asset_data ( bool ) - Clear Asset Data, Removes asset categorization and labels from the original component (optional)

- autoselect ( bool ) - Select, Marks new items as picked (optional)

- active_collection ( bool ) - Active Collection, Positions new items in the active collection (optional)

- instance_collections ( bool ) - Instance Collections, Generates instances for collections, rather than incorporating them directly into the composition (optional)

- instance_object_data ( bool ) - Instance Object Data, Generates instances for component geometry that are unreferenced by any item (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
