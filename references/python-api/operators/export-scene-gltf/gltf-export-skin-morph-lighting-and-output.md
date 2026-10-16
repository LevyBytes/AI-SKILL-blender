# bpy.ops.export_scene.gltf: glTF skin, morph, lighting and remaining output settings

**bpy.ops.export_scene.gltf**( * , filepath = '' , check_existing = True , export_import_convert_lighting_mode = 'SPEC' , gltf_export_id = '' , export_use_gltfpack = False , export_gltfpack_tc = True , export_gltfpack_tq = 8 , export_gltfpack_si = 1.0 , export_gltfpack_sa = False , export_gltfpack_slb = False , export_gltfpack_vp = 14 , export_gltfpack_vt = 12 , export_gltfpack_vn = 8 , export_gltfpack_vc = 8 , export_gltfpack_vpi = 'Integer' , export_gltfpack_noq = True , export_gltfpack_kn = False , export_format = '' , ui_tab = 'GENERAL' , export_copyright = '' , export_image_format = 'AUTO' , export_image_add_webp = False , export_image_webp_fallback = False , export_texture_dir = '' , export_jpeg_quality = 75 , export_image_quality = 75 , export_keep_originals = False , export_texcoords = True , export_normals = True , export_gn_mesh = False , export_draco_mesh_compression_enable = False , export_draco_mesh_compression_level = 6 , export_draco_position_quantization = 14 , export_draco_normal_quantization = 10 , export_draco_texcoord_quantization = 12 , export_draco_color_quantization = 10 , export_draco_generic_quantization = 12 , export_tangents = False , export_materials = 'EXPORT' , export_unused_images = False , export_unused_textures = False , export_vertex_color = 'MATERIAL' , export_vertex_color_name = 'Color' , export_all_vertex_colors = True , export_active_vertex_color_when_no_material = True , export_attributes = False , use_mesh_edges = False , use_mesh_vertices = False , export_cameras = False , use_selection = False , use_visible = False , use_renderable = False , use_active_collection_with_nested = True , use_active_collection = False , use_active_scene = False , collection = '' , at_collection_center = False , export_extras = False , export_yup = True , export_apply = False , export_shared_accessors = False , export_animations = True , export_frame_range = False , export_frame_step = 1 , export_force_sampling = True , export_sampling_interpolation_fallback = 'LINEAR' , export_pointer_animation = False , export_animation_mode = 'ACTIONS' , export_nla_strips_merged_animation_name = 'Animation' , export_def_bones = False , export_hierarchy_flatten_bones = False , export_hierarchy_flatten_objs = False , export_armature_object_remove = False , export_leaf_bone = False , export_optimize_animation_size = True , export_optimize_animation_keep_anim_armature = True , export_optimize_animation_keep_anim_object = False , export_optimize_disable_viewport = False , export_negative_frame = 'SLIDE' , export_anim_slide_to_zero = False , export_bake_animation = False , export_merge_animation = 'ACTION' , export_anim_single_armature = True , export_reset_pose_bones = True , export_current_frame = False , export_rest_position_armature = True , export_anim_scene_split_object = True , export_skins = True , export_influence_nb = 4 , export_all_influences = False , export_morph = True , export_morph_normal = True , export_morph_tangent = False , export_morph_animation = True , export_morph_reset_sk_data = True , export_lights = False , export_try_sparse_sk = True , export_try_omit_sparse_sk = False , export_gpu_instances = False , export_action_filter = False , export_convert_animation_pointer = False , export_nla_strips = True , export_original_specular = False , will_save_settings = False , export_hierarchy_full_collections = False , export_extra_animations = False , export_loglevel = -1 , filter_glob = '*.glb' )

- export_skins ( bool ) – Skinning, Export skinning (armature) data (optional)
- export_influence_nb ( int ) – Bone Influences, Choose how many Bone influences to export (in [1, inf], optional)
- export_all_influences ( bool ) – Include All Bone Influences, Allow export of all joint vertex influences. Models may appear incorrectly in many viewers (optional)
- export_morph ( bool ) – Shape Keys, Export shape keys (morph targets) (optional)
- export_morph_normal ( bool ) – Shape Key Normals, Export vertex normals with shape keys (morph targets) (optional)
- export_morph_tangent ( bool ) – Shape Key Tangents, Export vertex tangents with shape keys (morph targets) (optional)
- export_morph_animation ( bool ) – Shape Key Animations, Export shape keys animations (morph targets) (optional)
- export_morph_reset_sk_data ( bool ) – Reset Shape Keys Between Actions, Reset shape keys between each action exported. This is needed when some SK channels are not keyed on some animations (optional)
- export_lights ( bool ) – Punctual Lights, Export directional, point, and spot lights. Uses "KHR_lights_punctual" glTF extension (optional)
- export_try_sparse_sk ( bool ) – Use Sparse Accessor if Better, Try using Sparse Accessor if it saves space (optional)
- export_try_omit_sparse_sk ( bool ) – Omitting Sparse Accessor if Data is Empty, Omitting Sparse Accessor if data is empty (optional)
- export_gpu_instances ( bool ) – GPU Instances, Export using EXT_mesh_gpu_instancing. Limited to children of a given Empty. Multiple materials might be omitted (optional)
- export_action_filter ( bool ) – Filter Actions, Filter Actions to be exported (optional)
- export_convert_animation_pointer ( bool ) – Convert TRS/Weights to Animation Pointer, Export TRS and weights as Animation Pointer. Using KHR_animation_pointer extension (optional)
- export_nla_strips ( bool ) – Group by NLA Track, When on, multiple actions become part of the same glTF animation if they're pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation (optional)
- export_original_specular ( bool ) – Export Original PBR Specular, Export original glTF PBR Specular, instead of Blender Principled Shader Specular (optional)
- will_save_settings ( bool ) – Remember Export Settings, Store glTF export settings in the Blender project (optional)
- export_hierarchy_full_collections ( bool ) – Full Collection Hierarchy, Export full hierarchy, including intermediate collections (optional)
- export_extra_animations ( bool ) – Prepare Extra Animations, Export additional animations.This feature is not standard and needs an external extension to be included in the glTF file(optional)
- export_loglevel ( int ) – Log Level, Log Level (in [-inf, inf], optional)
- filter_glob ( str ) – filter_glob, (optional, never None)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

File: addons_core/io_scene_gltf2/__init__.py:1085

## See also

- [Scene Operators](../scene/INDEX.md)

[Related references](INDEX.md).
