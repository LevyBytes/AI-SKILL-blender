# bpy.ops.wm.stl_export: stl_export format, batch selection, scale and orientation

bpy.ops.wm. stl_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , ascii_format = False , use_batch = False , export_selected_objects = False , collection = '' , global_scale = 1.0 , use_scene_unit = False , forward_axis = 'Y' , up_axis = 'Z' , apply_modifiers = True , filter_glob = '*.stl' ) 

- ascii_format ( bool ) – ASCII Format, Output in text-based format; otherwise uses binary (optional)

- use_batch ( bool ) – Batch Export, Write each object to its own file (optional)

- export_selected_objects ( bool ) – Export Selected Objects, Restrict export to currently-selected objects only (optional)

- collection ( str ) – Source Collection, Write only objects from this collection and its children (optional, never None)

- global_scale ( float ) – Scale, (in [1e-06, 1e+06], optional)

- use_scene_unit ( bool ) – Scene Unit, Incorporates the active scene's scale factor into exported data (optional)

- forward_axis ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Forward Axis, (optional)

- X
X – Positive X axis.

- Y
Y – Positive Y axis.

- Z
Z – Positive Z axis.

- `NEGATIVE_X`
-X – Negative X axis.

- `NEGATIVE_Y`
-Y – Negative Y axis.

- `NEGATIVE_Z`
-Z – Negative Z axis.

- up_axis ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Up Axis, (optional)

- X
X – Positive X axis.

- Y
Y – Positive Y axis.

- Z
Z – Positive Z axis.

- `NEGATIVE_X`
-X – Negative X axis.

- `NEGATIVE_Y`
-Y – Negative Y axis.

- `NEGATIVE_Z`
-Z – Negative Z axis.

- apply_modifiers ( bool ) – Apply Modifiers, Execute modifiers on exported geometry (optional)

- filter_glob ( str ) – Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
