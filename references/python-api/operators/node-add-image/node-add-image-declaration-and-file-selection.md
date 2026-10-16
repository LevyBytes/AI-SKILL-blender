# bpy.ops.node.add_image: add_image declaration and file selection

bpy.ops.node. add_image ( * , filepath = '' , directory = '' , files = None , hide_props_region = True , check_existing = False , filter_blender = False , filter_backup = False , filter_image = True , filter_movie = True , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , show_multiview = False , use_multiview = False , display_type = 'DEFAULT' , sort_method = '' , name = '' , session_uid = 0 ) 

Bring a pic/reel record as node to the focal node panel

Parameters :

- filepath ( str ) – File Path, Path to record (optional, never None)

- directory ( str ) – Directory, Folder of the record (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – Files, (optional)

- hide_props_region ( bool ) – Hide Operator Properties, Fold up the panel showing the tool options (optional)

- check_existing ( bool ) – Check Existing, Check and alert on rewriting present records (optional)

- filter_blender ( bool ) – Filter .blend files, (optional)

- filter_backup ( bool ) – Filter backup .blend files, (optional)

- filter_image ( bool ) – Filter pic records, (optional)

- filter_movie ( bool ) – Filter reel records, (optional)

- filter_python ( bool ) – Filter Python records, (optional)

- filter_font ( bool ) – Filter font records, (optional)

- filter_sound ( bool ) – Filter tone records, (optional)

- filter_text ( bool ) – Filter text records, (optional)

- filter_archive ( bool ) – Filter pack records, (optional)

- filter_btx ( bool ) – Filter btx records, (optional)

- filter_alembic ( bool ) – Filter Alembic records, (optional)

- filter_usd ( bool ) – Filter USD records, (optional)

- filter_obj ( bool ) – Filter OBJ records, (optional)

- filter_volume ( bool ) – Filter OpenVDB bulk records, (optional)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_blenlib ( bool ) – Filter Blender IDs, (optional)

- filemode ( int ) – File Browser Mode, The setup for the record panel mode to open a .blend record, a book or a unique record (in [1, 9], optional)

- relative_path ( bool ) – Relative Path, Mark the record relative to the mix record (optional)

[Related references](INDEX.md).
