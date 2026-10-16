# bpy.ops.node.add_image: add_image multi-view, browser display and image identity

bpy.ops.node. add_image ( * , filepath = '' , directory = '' , files = None , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , name = '' , session_uid = 0 ) 

- show_multiview ( bool ) – Enable Multi-View, (optional)

- use_multiview ( bool ) – Use Multi-View, (optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Mechanically pick display for records.

- `LIST_VERTICAL`
Short List – Show records as brief roll.

- `LIST_HORIZONTAL`
Long List – Show records as a thorough roll.

- THUMBNAIL
Thumbnails – Show records as miniatures.

- sort_method ( Literal [ 'DEFAULT' , '`FILE_SORT_ALPHA`' , '`FILE_SORT_EXTENSION`' , '`FILE_SORT_TIME`' , '`FILE_SORT_SIZE`' , '`ASSET_CATALOG`' ] ) – File sorting mode, (optional)

- DEFAULT
Default – Mechanically pick sort technique for records.

- `FILE_SORT_ALPHA`
Name – Sort the record list by letter.

- `FILE_SORT_EXTENSION`
Extension – Sort the record list by type/suffix.

- `FILE_SORT_TIME`
Modified Date – Sort records by when they changed.

- `FILE_SORT_SIZE`
Size – Sort records by size.

- `ASSET_CATALOG`
Asset Catalog – Sort the tool roll so that tools in the same category stay together. Within one category, tools are sorted by label. The categories are in rank of the leveled group makeup.

- name ( str ) – Name, Label of the information to employ (optional, never None)

- session_uid ( int ) – Session UID, Session marker of the information to employ (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
