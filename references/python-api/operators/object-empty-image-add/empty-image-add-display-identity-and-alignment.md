# bpy.ops.object.empty_image_add: empty_image_add multi-view, display, identity and alignment

bpy.ops.object. empty_image_add ( * , filepath = '' , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , name = '' , session_uid = 0 , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) , background = False ) 

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

- name ( str ) – Name, Name of the data-block to use by the operator (optional, never None)

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, The alignment of the new object (optional)

- WORLD
World – Align the new object to the world.

- VIEW
View – Align the new object to the view.

- CURSOR
3D Cursor – Use the 3D cursor orientation for the new object.

[Related references](INDEX.md).
