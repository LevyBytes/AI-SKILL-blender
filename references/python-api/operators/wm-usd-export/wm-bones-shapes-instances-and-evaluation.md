# bpy.ops.wm.usd_export: bones, shapes, instances and evaluation

bpy.ops.wm. usd_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , selected_objects_only = False , collection = '' , export_animation = False , export_hair = False , export_uvmaps = True , rename_uvmaps = True , export_mesh_colors = True , export_normals = True , export_materials = True , export_subdivision = '`BEST_MATCH`' , export_armatures = True , only_deform_bones = False , export_shapekeys = True , use_instancing = False , evaluation_mode = 'RENDER' , generate_preview_surface = True , generate_materialx_network = False , convert_orientation = False , export_global_forward_selection = '`NEGATIVE_Z`' , export_global_up_selection = 'Y' , export_textures_mode = 'NEW' , overwrite_textures = False , relative_paths = True , xform_op_mode = 'TRS' , root_prim_path = '/root' , export_custom_properties = True , custom_properties_namespace = 'userProperties' , accessibility_label = '' , accessibility_description = '' , author_blender_name = True , convert_world_material = True , allow_unicode = True , export_meshes = True , export_lights = True , export_cameras = True , export_curves = True , export_points = True , export_volumes = True , triangulate_meshes = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , usdz_downscale_size = 'KEEP' , usdz_downscale_custom_size = 128 , merge_parent_xform = False , convert_scene_units = 'METERS' , meters_per_unit = 1.0 ) 

- only_deform_bones ( bool ) – Only Deform Bones, Write only deformation joints and their ancestors (optional)

- export_shapekeys ( bool ) – Shape Keys, Write shape keys as USD combine structures (optional)

- use_instancing ( bool ) – Instancing, Write duplicated items as cross-references in USD rather than replicated items (optional)

- evaluation_mode ( Literal [ 'RENDER' , 'VIEWPORT' ] ) – Use Settings for, Picks whether objects are shown, parameter adjustments, and additional zones where render and view setups differ (optional)

- RENDER
Render – Apply Rendering configuration for thing appearance, parameter adjustments, and so forth.

- VIEWPORT
Viewport – Apply View configuration for thing appearance, parameter adjustments, and so forth.

- generate_preview_surface ( bool ) – USD Preview Surface Network, Make a representative USD Preview SurfaceTemplate representation of a Principled BSDF diagram organization (optional)

- generate_materialx_network ( bool ) – MaterialX Network, Make a MaterialX diagram representation of the materials (optional)

- convert_orientation ( bool ) – Convert Orientation, Shift orientation direction to a distinct convention to correlate with alternative platforms (optional)

- export_global_forward_selection ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Forward Axis, (optional)

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

- export_global_up_selection ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Up Axis, (optional)

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

[Related references](INDEX.md).
