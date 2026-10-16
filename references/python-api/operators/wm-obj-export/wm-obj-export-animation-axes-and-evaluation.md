# bpy.ops.wm.obj_export: obj_export animation, axes and evaluation

bpy.ops.wm. obj_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , export_animation = False , start_frame = -2147483648 , end_frame = 2147483647 , forward_axis = '`NEGATIVE_Z`' , up_axis = 'Y' , global_scale = 1.0 , apply_modifiers = True , apply_transform = True , export_eval_mode = '`DAG_EVAL_VIEWPORT`' , export_selected_objects = False , export_uv = True , export_normals = True , export_colors = False , export_materials = True , export_pbr_extensions = False , path_mode = 'AUTO' , export_triangulated_mesh = False , export_curves_as_nurbs = False , export_object_groups = False , export_material_groups = False , export_vertex_groups = False , export_smooth_groups = False , smooth_group_bitflags = False , filter_glob = '*.obj;*.mtl' , collection = '' ) 

- export_animation ( bool ) – Export Animation, Include animation frames instead of just the current one (optional)

- start_frame ( int ) – Start Frame, First frame for export (in [-inf, inf], optional)

- end_frame ( int ) – End Frame, Last frame for export (in [-inf, inf], optional)

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

- global_scale ( float ) – Scale, Multiplies the dimensions of objects relative to world origin (in [0.0001, 10000], optional)

- apply_modifiers ( bool ) – Apply Modifiers, Execute modifiers on exported geometry (optional)

- apply_transform ( bool ) – Apply Transform, Bake object transformations into exported geometry (optional)

- export_eval_mode ( Literal [ '`DAG_EVAL_RENDER`' , '`DAG_EVAL_VIEWPORT`' ] ) – Object Properties, Sets object characteristics like visibility and modifiers for either render or viewport display (optional)

- `DAG_EVAL_RENDER`
Render – Export objects as they appear in render.

- `DAG_EVAL_VIEWPORT`
Viewport – Export objects as they appear in the viewport.

[Related references](INDEX.md).
