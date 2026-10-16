# bpy.ops.image.open

bpy.ops.image. open ( * , allow_path_tokens = True , filepath = '' , directory = '' , files = None , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , use_sequence_detection = True , use_udim_detecting = True )

Open image

Parameters :

- allow_path_tokens ( bool ) – Permit substitution tokens inside the path (optional)

- filepath ( str ) – File Path, Path to file (optional, never None)

- directory ( str ) – Directory, Directory of the file (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

- hide_props_region ( bool ) – Hide Operator Properties, Fold away the area that shows the operator settings (optional)

- check_existing ( bool ) – Check Existing, Warn before overwriting files that already exist (optional)

- filter_blender ( bool ) – Show .blend files in the dialog, (optional)

- filter_backup ( bool ) – Show backup .blend files in the dialog, (optional)

- filter_image ( bool ) – Show image files in the dialog, (optional)

- filter_movie ( bool ) – Show movie files in the dialog, (optional)
- filter_python ( bool ) – Show Python files in the dialog, (optional)

- filter_font ( bool ) – Show font files in the dialog, (optional)

- filter_sound ( bool ) – Show sound files in the dialog, (optional)

- filter_text ( bool ) – Show text files in the dialog, (optional)

- filter_archive ( bool ) – Show archive files in the dialog, (optional)

- filter_btx ( bool ) – Show btx files in the dialog, (optional)

- filter_alembic ( bool ) – Show Alembic files in the dialog, (optional)

- filter_usd ( bool ) – Show USD files in the dialog, (optional)

- filter_obj ( bool ) – Show OBJ files in the dialog, (optional)

- filter_volume ( bool ) – Show OpenVDB volume files in the dialog, (optional)

- filter_folder ( bool ) – Show folders in the dialog, (optional)

- filter_blenlib ( bool ) – Show Blender IDs in the dialog, (optional)

- filemode ( int ) – File Browser Mode, Which file-browser mode to use when loading a .blend file, a library, or a special file (in [1, 9], optional)

- relative_path ( bool ) – Relative Path, Pick the file relative to the current blend file (optional)

- show_multiview ( bool ) – Enable Multi-View, (optional)

- use_multiview ( bool ) – Use Multi-View, (optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Let Blender pick the display type for files automatically.

- `LIST_VERTICAL`
Short List – Show files in a compact list.

- `LIST_HORIZONTAL`
Long List – Show files in a detailed list.

- THUMBNAIL
Thumbnails – Show files as thumbnail previews.

- sort_method ( str ) – File sorting mode, (optional)

- use_sequence_detection ( bool ) – Detect Sequences, Spot animated sequences among the selected images using their file names (optional)

- use_udim_detecting ( bool ) – Detect UDIMs, Find selected UDIM files and pull in every matching tile (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
