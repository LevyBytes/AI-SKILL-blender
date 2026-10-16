# bpy.ops.wm.obj_import: obj_import scale and orientation

bpy.ops.wm. obj_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , clamp_size = 0.0 , forward_axis = '`NEGATIVE_Z`' , up_axis = 'Y' , use_split_objects = True , use_split_groups = False , import_vertex_groups = False , validate_meshes = True , close_spline_loops = True , collection_separator = '' , mtl_name_collision_mode = '`MAKE_UNIQUE`' , filter_glob = '*.obj;*.mtl' ) 

- global_scale ( float ) – Scale, Adjusts object dimensions relative to the world's origin (in [0.0001, 10000], optional)

- clamp_size ( float ) – Clamp Bounding Box, Resize objects to keep bounding box within this threshold. Value 0 disables constraint (in [0, 1000], optional)

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

- use_split_objects ( bool ) – Split By Object, Treats each OBJ 'o' as its own distinct object (optional)

- use_split_groups ( bool ) – Split By Group, Treats each OBJ 'g' as its own distinct object (optional)

- import_vertex_groups ( bool ) – Vertex Groups, Converts OBJ groups into vertex groups (optional)

- validate_meshes ( bool ) – Validate Meshes, Ensures imported data passes validity checks (if disabled, problematic data may cause crashes) (optional)

- close_spline_loops ( bool ) – Detect Cyclic Curves, Links curve endpoints when overlapping control points are discovered (if disabled, curves will remain unclosed) (optional)

- collection_separator ( str ) – Path Separator, Symbol dividing object names into hierarchical structures (optional, never None)

- mtl_name_collision_mode ( Literal [ '`MAKE_UNIQUE`' , '`REFERENCE_EXISTING`' ] ) – Material Name Collision, Handling strategy when material names clash during import (optional)

- `MAKE_UNIQUE`
Make Unique – Create new materials with unique names for each OBJ file.

- `REFERENCE_EXISTING`
Reference Existing – Use existing materials with same name instead of creating new ones.

- filter_glob ( str ) – Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
