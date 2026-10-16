# bpy.ops.export_scene.gltf: glTF declaration, lighting conversion, packing and format

**bpy.ops.export_scene.gltf**( * , filepath = '' , check_existing = True , export_import_convert_lighting_mode = 'SPEC' , gltf_export_id = '' , export_use_gltfpack = False , export_gltfpack_tc = True , export_gltfpack_tq = 8 , export_gltfpack_si = 1.0 , export_gltfpack_sa = False , export_gltfpack_slb = False , export_gltfpack_vp = 14 , export_gltfpack_vt = 12 , export_gltfpack_vn = 8 , export_gltfpack_vc = 8 , export_gltfpack_vpi = 'Integer' , export_gltfpack_noq = True , export_gltfpack_kn = False , export_format = '' , ui_tab = 'GENERAL' , export_copyright = '' , export_image_format = 'AUTO' , export_image_add_webp = False , export_image_webp_fallback = False , export_texture_dir = '' , export_jpeg_quality = 75 , export_image_quality = 75 , export_keep_originals = False , export_texcoords = True , export_normals = True , export_gn_mesh = False , export_draco_mesh_compression_enable = False , export_draco_mesh_compression_level = 6 , export_draco_position_quantization = 14 , export_draco_normal_quantization = 10 , export_draco_texcoord_quantization = 12 , export_draco_color_quantization = 10 , export_draco_generic_quantization = 12 , export_tangents = False , export_materials = 'EXPORT' , export_unused_images = False , export_unused_textures = False , export_vertex_color = 'MATERIAL' , export_vertex_color_name = 'Color' , export_all_vertex_colors = True , export_active_vertex_color_when_no_material = True , export_attributes = False , use_mesh_edges = False , use_mesh_vertices = False , export_cameras = False , use_selection = False , use_visible = False , use_renderable = False , use_active_collection_with_nested = True , use_active_collection = False , use_active_scene = False , collection = '' , at_collection_center = False , export_extras = False , export_yup = True , export_apply = False , export_shared_accessors = False , export_animations = True , export_frame_range = False , export_frame_step = 1 , export_force_sampling = True , export_sampling_interpolation_fallback = 'LINEAR' , export_pointer_animation = False , export_animation_mode = 'ACTIONS' , export_nla_strips_merged_animation_name = 'Animation' , export_def_bones = False , export_hierarchy_flatten_bones = False , export_hierarchy_flatten_objs = False , export_armature_object_remove = False , export_leaf_bone = False , export_optimize_animation_size = True , export_optimize_animation_keep_anim_armature = True , export_optimize_animation_keep_anim_object = False , export_optimize_disable_viewport = False , export_negative_frame = 'SLIDE' , export_anim_slide_to_zero = False , export_bake_animation = False , export_merge_animation = 'ACTION' , export_anim_single_armature = True , export_reset_pose_bones = True , export_current_frame = False , export_rest_position_armature = True , export_anim_scene_split_object = True , export_skins = True , export_influence_nb = 4 , export_all_influences = False , export_morph = True , export_morph_normal = True , export_morph_tangent = False , export_morph_animation = True , export_morph_reset_sk_data = True , export_lights = False , export_try_sparse_sk = True , export_try_omit_sparse_sk = False , export_gpu_instances = False , export_action_filter = False , export_convert_animation_pointer = False , export_nla_strips = True , export_original_specular = False , will_save_settings = False , export_hierarchy_full_collections = False , export_extra_animations = False , export_loglevel = -1 , filter_glob = '*.glb' )

Save scene as glTF 2.0 file.

Parameters:
- filepath ( str ) – File Path, Filepath used for exporting the file (optional, never None)

- check_existing ( bool ) – Check Existing, Check and warn on overwriting existing files (optional)
- export_import_convert_lighting_mode ( Literal [ 'SPEC' , 'COMPAT' , 'RAW' ] ) – Lighting Mode, Optional backwards compatibility for non-standard render engines. Applies to lights (optional)

- SPEC
Standard – Physically-based glTF lighting units (cd, lx, nt).

- COMPAT
Unitless – Non-physical, unitless lighting. Useful when exposure controls are not available.

- RAW
Raw (Deprecated) – Blender lighting strengths with no conversion.

- gltf_export_id ( str ) – Identifier, Identifier of caller (in case of add-on calling this exporter). Can be useful in case of Extension added by other add-ons (optional, never None)
- export_use_gltfpack ( bool ) – Use Gltfpack, Use gltfpack to simplify the mesh and/or compress its textures (optional)
- export_gltfpack_tc ( bool ) – KTX2 Compression, Convert all textures to KTX2 with BasisU supercompression (optional)
- export_gltfpack_tq ( int ) – Texture Encoding Quality, Texture encoding quality (in [1, 10], optional)
- export_gltfpack_si ( float ) – Mesh Simplification Ratio, Simplify meshes targeting triangle count ratio (in [0, 1], optional)
- export_gltfpack_sa ( bool ) – Aggressive Mesh Simplification, Aggressively simplify to the target ratio disregarding quality (optional)
- export_gltfpack_slb ( bool ) – Lock Mesh Border Vertices, Lock border vertices during simplification to avoid gaps on connected meshes (optional)
- export_gltfpack_vp ( int ) – Position Quantization, Use N-bit quantization for positions (in [1, 16], optional)
- export_gltfpack_vt ( int ) – Texture Coordinate Quantization, Use N-bit quantization for texture coordinates (in [1, 16], optional)
- export_gltfpack_vn ( int ) – Normal/Tangent Quantization, Use N-bit quantization for normals and tangents (in [1, 16], optional)
- export_gltfpack_vc ( int ) – Vertex Color Quantization, Use N-bit quantization for colors (in [1, 16], optional)
- export_gltfpack_vpi ( Literal [ 'Integer' , 'Normalized' , 'Floating-point' ] ) – Vertex Position Attributes, Type to use for vertex position attributes (optional)

- Integer
Integer – Use integer attributes for positions.

- Normalized
Normalized – Use normalized attributes for positions.

- Floating-point
Floating-point – Use floating-point attributes for positions.

- export_gltfpack_noq ( bool ) – Disable Quantization, Disable quantization; produces much larger glTF files with no extensions (optional)
- export_gltfpack_kn ( bool ) – Keep Named Nodes, Restrict some optimization to keep named nodes and meshes attached to named nodes so that named nodes can be transformed externally (optional)
- export_format ( str ) – Format, Output format. Binary is most efficient, but JSON may be easier to edit later (optional)
- ui_tab ( Literal [ 'GENERAL' , 'MESHES' , 'OBJECTS' , 'ANIMATION' ] ) – ui_tab, Export setting categories (optional)

- GENERAL
General – General settings.

- MESHES
Meshes – Mesh settings.

- OBJECTS
Objects – Object settings.

- ANIMATION
Animation – Animation settings.

[Related references](INDEX.md).
