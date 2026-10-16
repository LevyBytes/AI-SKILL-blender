# bpy.ops.wm.usd_import: usd_import scale, object families, visibility and mesh attributes

bpy.ops.wm. usd_import ( * , filepath = '' , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , scale = 1.0 , set_frame_range = True , import_cameras = True , import_curves = True , import_lights = True , import_materials = True , import_meshes = True , import_volumes = True , import_shapes = True , import_skeletons = True , import_blendshapes = True , import_points = True , import_subdivision = False , support_scene_instancing = True , import_visible_only = True , create_collection = False , read_mesh_uvs = True , read_mesh_colors = True , read_mesh_attributes = True , prim_path_mask = '' , import_guide = False , import_proxy = False , import_render = True , import_all_materials = False , import_usd_preview = True , set_material_blend = True , light_intensity_scale = 1.0 , mtl_purpose = '`MTL_FULL`' , mtl_name_collision_mode = '`MAKE_UNIQUE`' , import_textures_mode = '`IMPORT_PACK`' , import_textures_dir = '//textures/' , tex_name_collision_mode = '`USE_EXISTING`' , property_import_mode = 'ALL' , validate_meshes = False , create_world_material = True , import_defined_only = True , merge_parent_xform = True , apply_unit_conversion_scale = True ) 

- scale ( float ) – Scale, Amount to magnify or minimize the things matching the place of beginning (in [0.0001, 1000], optional)

- set_frame_range ( bool ) – Set Frame Range, Refresh the setup's starting and closing frame to coincide with those of the USD information (optional)

- import_cameras ( bool ) – Cameras, (optional)

- import_curves ( bool ) – Curves, (optional)

- import_lights ( bool ) – Lights, (optional)

- import_materials ( bool ) – Materials, (optional)

- import_meshes ( bool ) – Meshes, (optional)

- import_volumes ( bool ) – Volumes, (optional)

- import_shapes ( bool ) – USD Shapes, (optional)

- import_skeletons ( bool ) – Armatures, (optional)

- import_blendshapes ( bool ) – Shape Keys, (optional)

- import_points ( bool ) – Point Clouds, (optional)

- import_subdivision ( bool ) – Import Subdivision Scheme, Build subdivision outer layer adjusters grounded in the USD SubdivisionScheme characteristic (optional)

- support_scene_instancing ( bool ) – Scene Instancing, Bring USD hierarchy examples as group examples (optional)

- import_visible_only ( bool ) – Visible Primitives Only, Skip importing hidden USD structures. Applies merely to structures lacking an shifting appearance characteristic. Structures with active appearance will forever be brought (optional)

- create_collection ( bool ) – Create Collection, Position every brought item into a newly made batch (optional)

- read_mesh_uvs ( bool ) – UV Coordinates, Read mesh shade coordinates (optional)

- read_mesh_colors ( bool ) – Color Attributes, Read mesh hue characteristics (optional)

- read_mesh_attributes ( bool ) – Mesh Attributes, Read USD Primvars as mesh characteristics (optional)

- prim_path_mask ( str ) – Path Mask, Bring merely the structural element at the given trail and its offspring. Many trails may be specified in a sequence split by commas or semicolons (optional, never None)

- import_guide ( bool ) – Guide, Bring guiding material (optional)

- import_proxy ( bool ) – Proxy, Bring surrogate material (optional)

- import_render ( bool ) – Render, Bring ultimate display material (optional)

[Related references](INDEX.md).
