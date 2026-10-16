# bpy.ops.wm.stl_import: stl_import scale, units, normals and orientation

bpy.ops.wm. stl_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , use_scene_unit = False , use_facet_normal = False , forward_axis = 'Y' , up_axis = 'Z' , use_mesh_validate = True , filter_glob = '*.stl' )

- global_scale ( float ) – Scale, (in [1e-06, 1e+06], optional)

- use_scene_unit ( bool ) – Scene Unit, Use current scene's unit scale (as specified by unit measurement) on brought-in content (optional)

- use_facet_normal ( bool ) – Facet Normals, Utilize (importing) facet normals (note that this will still yield flat shading) (optional)

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

- use_mesh_validate ( bool ) – Validate Mesh, Ensure the data is valid (when disabled, imported content may be problematic causing slowdowns or crashes when interacting with or presenting) (optional)

- filter_glob ( str ) – Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
