# bpy.ops.wm.usd_export: usd_export USDZ downscaling, scene units and return

bpy.ops.wm. usd_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , selected_objects_only = False , collection = '' , export_animation = False , export_hair = False , export_uvmaps = True , rename_uvmaps = True , export_mesh_colors = True , export_normals = True , export_materials = True , export_subdivision = '`BEST_MATCH`' , export_armatures = True , only_deform_bones = False , export_shapekeys = True , use_instancing = False , evaluation_mode = 'RENDER' , generate_preview_surface = True , generate_materialx_network = False , convert_orientation = False , export_global_forward_selection = '`NEGATIVE_Z`' , export_global_up_selection = 'Y' , export_textures_mode = 'NEW' , overwrite_textures = False , relative_paths = True , xform_op_mode = 'TRS' , root_prim_path = '/root' , export_custom_properties = True , custom_properties_namespace = 'userProperties' , accessibility_label = '' , accessibility_description = '' , author_blender_name = True , convert_world_material = True , allow_unicode = True , export_meshes = True , export_lights = True , export_cameras = True , export_curves = True , export_points = True , export_volumes = True , triangulate_meshes = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , usdz_downscale_size = 'KEEP' , usdz_downscale_custom_size = 128 , merge_parent_xform = False , convert_scene_units = 'METERS' , meters_per_unit = 1.0 ) 

- usdz_downscale_size ( Literal [ 'KEEP' , '256' , '512' , '1024' , '2048' , '4096' , 'CUSTOM' ] ) – USDZ Texture Downsampling, Establish a boundary size for shipped surfaces (optional)

- KEEP
Keep – Preserve all current surface measures.

- 256
256 – Modify to a boundary of 256 dots.

- 512
512 – Modify to a boundary of 512 dots.

- 1024
1024 – Modify to a boundary of 1024 dots.

- 2048
2048 – Modify to a boundary of 2048 dots.

- 4096
4096 – Modify to a boundary of 4096 dots.

- CUSTOM
Custom – Specify a custom measure.

- usdz_downscale_custom_size ( int ) – USDZ Custom Downscale Size, User-defined measure for shrinking written surfaces (in [64, 16384], optional)

- merge_parent_xform ( bool ) – Merge parent Xform, Merge USD building blocks with their Xform ancestor if feasible. USD does not authorize interior UsdGeomGprims, middle Xform blocks will be made to sustain the USD document authentic when meeting item lineages. (optional)

- convert_scene_units ( Literal [ 'METERS' , 'KILOMETERS' , 'CENTIMETERS' , 'MILLIMETERS' , 'INCHES' , 'FEET' , 'YARDS' , 'CUSTOM' ] ) – Units, Adjust the USD Phase meters per measurement to the chosen scale, or a user value (optional)

- METERS
Meters – Phase meters per measurement to 1.0.

- KILOMETERS
Kilometers – Phase meters per measurement to 1000.0.

- CENTIMETERS
Centimeters – Phase meters per measurement to 0.01.

- MILLIMETERS
Millimeters – Phase meters per measurement to 0.001.

- INCHES
Inches – Phase meters per measurement to 0.0254.

- FEET
Feet – Phase meters per measurement to 0.3048.

- YARDS
Yards – Phase meters per measurement to 0.9144.

- CUSTOM
Custom – Specify a user-defined phase meters per measurement amount.

- meters_per_unit ( float ) – Meters Per Unit, User value for meters per measurement in the USD Phase (in [0.0001, 1000], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
