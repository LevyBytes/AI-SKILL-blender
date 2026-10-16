# bpy.ops.object.volume_import

bpy.ops.object. volume_import ( * , filepath = '' , directory = '' , files = None , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = True , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , use_sequence_detection = True , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Fetch an OpenVDB volume record

Parameters :

- filepath ( str ) – File Path, Route to record (optional, never None)

- directory ( str ) – Directory, Route listing of the record (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

- hide_props_region ( bool ) – Hide Operator Properties, Break down the area showing the action adjustments (optional)

- check_existing ( bool ) – Check Existing, Inspect and notify on replacing current records (optional)

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

- filemode ( int ) – File Browser Mode, The configuration for the record browser method to pull a .blend record, a stash or a particular record (in [1, 9], optional)

- relative_path ( bool ) – Relative Path, Opt for the record comparative to the blend record (optional)
- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Programmatically determine appearance approach for records.

- `LIST_VERTICAL`
Short List – Show records as abbreviated list.

- `LIST_HORIZONTAL`
Long List – Show records as an comprehensive listing.

- THUMBNAIL
Thumbnails – Show records as picture previews.

- sort_method ( str ) – File sorting mode, (optional)

- use_sequence_detection ( bool ) – Detect Sequences, Mechanically find moving sets in chosen volume records (depending on record designations) (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, Where the fresh item sits (optional)

- WORLD
World – Position the fresh item with respect to the world axes.

- VIEW
View – Position the fresh item with respect to the viewport.

- CURSOR
3D Cursor – Employ the 3D cursor's orientation for the fresh item.

- location (mathutils.Vector) – Location, Where the inserted item goes (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, How the inserted item is oriented (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, How the inserted item is sized (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
