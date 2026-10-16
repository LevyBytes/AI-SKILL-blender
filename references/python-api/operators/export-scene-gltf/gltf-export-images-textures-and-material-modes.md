# bpy.ops.export_scene.gltf: glTF images, textures, compression and material modes

**bpy.ops.export_scene.gltf**( * , filepath = '' , check_existing = True , export_import_convert_lighting_mode = 'SPEC' , gltf_export_id = '' , export_use_gltfpack = False , export_gltfpack_tc = True , export_gltfpack_tq = 8 , export_gltfpack_si = 1.0 , export_gltfpack_sa = False , export_gltfpack_slb = False , export_gltfpack_vp = 14 , export_gltfpack_vt = 12 , export_gltfpack_vn = 8 , export_gltfpack_vc = 8 , export_gltfpack_vpi = 'Integer' , export_gltfpack_noq = True , export_gltfpack_kn = False , export_format = '' , ui_tab = 'GENERAL' , export_copyright = '' , export_image_format = 'AUTO' , export_image_add_webp = False , export_image_webp_fallback = False , export_texture_dir = '' , export_jpeg_quality = 75 , export_image_quality = 75 , export_keep_originals = False , export_texcoords = True , export_normals = True , export_gn_mesh = False , export_draco_mesh_compression_enable = False , export_draco_mesh_compression_level = 6 , export_draco_position_quantization = 14 , export_draco_normal_quantization = 10 , export_draco_texcoord_quantization = 12 , export_draco_color_quantization = 10 , export_draco_generic_quantization = 12 , export_tangents = False , export_materials = 'EXPORT' , export_unused_images = False , export_unused_textures = False , export_vertex_color = 'MATERIAL' , export_vertex_color_name = 'Color' , export_all_vertex_colors = True , export_active_vertex_color_when_no_material = True , export_attributes = False , use_mesh_edges = False , use_mesh_vertices = False , export_cameras = False , use_selection = False , use_visible = False , use_renderable = False , use_active_collection_with_nested = True , use_active_collection = False , use_active_scene = False , collection = '' , at_collection_center = False , export_extras = False , export_yup = True , export_apply = False , export_shared_accessors = False , export_animations = True , export_frame_range = False , export_frame_step = 1 , export_force_sampling = True , export_sampling_interpolation_fallback = 'LINEAR' , export_pointer_animation = False , export_animation_mode = 'ACTIONS' , export_nla_strips_merged_animation_name = 'Animation' , export_def_bones = False , export_hierarchy_flatten_bones = False , export_hierarchy_flatten_objs = False , export_armature_object_remove = False , export_leaf_bone = False , export_optimize_animation_size = True , export_optimize_animation_keep_anim_armature = True , export_optimize_animation_keep_anim_object = False , export_optimize_disable_viewport = False , export_negative_frame = 'SLIDE' , export_anim_slide_to_zero = False , export_bake_animation = False , export_merge_animation = 'ACTION' , export_anim_single_armature = True , export_reset_pose_bones = True , export_current_frame = False , export_rest_position_armature = True , export_anim_scene_split_object = True , export_skins = True , export_influence_nb = 4 , export_all_influences = False , export_morph = True , export_morph_normal = True , export_morph_tangent = False , export_morph_animation = True , export_morph_reset_sk_data = True , export_lights = False , export_try_sparse_sk = True , export_try_omit_sparse_sk = False , export_gpu_instances = False , export_action_filter = False , export_convert_animation_pointer = False , export_nla_strips = True , export_original_specular = False , will_save_settings = False , export_hierarchy_full_collections = False , export_extra_animations = False , export_loglevel = -1 , filter_glob = '*.glb' )

- export_copyright ( str ) – Copyright, Legal rights and conditions for the model (optional, never None)
- export_image_format ( Literal [ 'AUTO' , 'JPEG' , 'WEBP' , 'NONE' ] ) – Images, Output format for images. PNG is lossless and generally preferred, but JPEG might be preferable for web applications due to the smaller file size. Alternatively they can be omitted if they are not needed (optional)

- AUTO
Automatic – Save PNGs as PNGs, JPEGs as JPEGs, WebPs as WebPs. For other formats, use PNG.

- JPEG
JPEG Format (.jpg) – Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.

- WEBP
WebP Format – Save images as WebPs as main image (no fallback).

- NONE
None – Don't export images.

- export_image_add_webp ( bool ) – Create WebP, Creates WebP textures for every texture. For already WebP textures, nothing happens (optional)
- export_image_webp_fallback ( bool ) – WebP Fallback, For all WebP textures, create a PNG fallback texture (optional)
- export_texture_dir ( str ) – Textures, Folder to place texture files in. Relative to the .gltf file (optional, never None)
- export_jpeg_quality ( int ) – JPEG Quality, Quality of JPEG export (in [0, 100], optional)
- export_image_quality ( int ) – Image Quality, Quality of image export (in [0, 100], optional)
- export_keep_originals ( bool ) – Keep Original, Keep original textures files if possible. WARNING: if you use more than one texture, where pbr standard requires only one, only one texture will be used. This can lead to unexpected results (optional)
- export_texcoords ( bool ) – UVs, Export UVs (texture coordinates) with meshes (optional)
- export_normals ( bool ) – Normals, Export vertex normals with meshes (optional)
- export_gn_mesh ( bool ) – Geometry Nodes Instances (Experimental), Export Geometry nodes instance meshes (optional)
- export_draco_mesh_compression_enable ( bool ) – Draco Mesh Compression, Compress mesh using Draco (optional)
- export_draco_mesh_compression_level ( int ) – Compression Level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported) (in [0, 10], optional)
- export_draco_position_quantization ( int ) – Position Quantization Bits, Quantization bits for position values (0 = no quantization) (in [0, 30], optional)
- export_draco_normal_quantization ( int ) – Normal Quantization Bits, Quantization bits for normal values (0 = no quantization) (in [0, 30], optional)
- export_draco_texcoord_quantization ( int ) – Texcoord Quantization Bits, Quantization bits for texture coordinate values (0 = no quantization) (in [0, 30], optional)
- export_draco_color_quantization ( int ) – Color Quantization Bits, Quantization bits for color values (0 = no quantization) (in [0, 30], optional)
- export_draco_generic_quantization ( int ) – Generic Quantization Bits, Quantization bits for generic values like weights or joints (0 = no quantization) (in [0, 30], optional)
- export_tangents ( bool ) – Tangents, Export vertex tangents with meshes (optional)
- export_materials ( Literal [ 'EXPORT' , 'PLACEHOLDER' , 'VIEWPORT' , 'NONE' ] ) – Materials, Export materials (optional)

- EXPORT
Export – Export all materials used by included objects.

- PLACEHOLDER
Placeholder – Do not export materials, but write multiple primitive groups per mesh, keeping material slot information.

- VIEWPORT
Viewport – Export minimal materials as defined in Viewport display properties.

[Related references](INDEX.md).
