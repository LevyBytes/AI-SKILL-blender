# bpy.ops.wm.ply_import: ply_import scale, units and orientation

bpy.ops.wm. ply_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , use_scene_unit = False , forward_axis = 'Y' , up_axis = 'Z' , merge_verts = False , import_colors = 'SRGB' , import_attributes = True , filter_glob = '*.ply' ) 

- global_scale ( float ) – Scale, (in [1e-06, 1e+06], optional)

- use_scene_unit ( bool ) – Scene Unit, Incorporates the active scene's scale factor into imported data (optional)

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

- merge_verts ( bool ) – Merge Vertices, Consolidates vertices that are close together (optional)

- import_colors ( Literal [ 'NONE' , 'SRGB' , 'LINEAR' ] ) – Vertex Colors, Read in color attributes at each vertex (optional)

- NONE
None – Do not import/export color attributes.

- SRGB
sRGB – Vertex colors in the file are in sRGB color space.

- LINEAR
Linear – Vertex colors in the file are in linear color space.

- import_attributes ( bool ) – Vertex Attributes, Read in custom vertex attributes (optional)

- filter_glob ( str ) – Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
