# bpy.ops.export_scene.gltf: glTF animation, frame and armature settings

**bpy.ops.export_scene.gltf**( * , filepath = '' , check_existing = True , export_import_convert_lighting_mode = 'SPEC' , gltf_export_id = '' , export_use_gltfpack = False , export_gltfpack_tc = True , export_gltfpack_tq = 8 , export_gltfpack_si = 1.0 , export_gltfpack_sa = False , export_gltfpack_slb = False , export_gltfpack_vp = 14 , export_gltfpack_vt = 12 , export_gltfpack_vn = 8 , export_gltfpack_vc = 8 , export_gltfpack_vpi = 'Integer' , export_gltfpack_noq = True , export_gltfpack_kn = False , export_format = '' , ui_tab = 'GENERAL' , export_copyright = '' , export_image_format = 'AUTO' , export_image_add_webp = False , export_image_webp_fallback = False , export_texture_dir = '' , export_jpeg_quality = 75 , export_image_quality = 75 , export_keep_originals = False , export_texcoords = True , export_normals = True , export_gn_mesh = False , export_draco_mesh_compression_enable = False , export_draco_mesh_compression_level = 6 , export_draco_position_quantization = 14 , export_draco_normal_quantization = 10 , export_draco_texcoord_quantization = 12 , export_draco_color_quantization = 10 , export_draco_generic_quantization = 12 , export_tangents = False , export_materials = 'EXPORT' , export_unused_images = False , export_unused_textures = False , export_vertex_color = 'MATERIAL' , export_vertex_color_name = 'Color' , export_all_vertex_colors = True , export_active_vertex_color_when_no_material = True , export_attributes = False , use_mesh_edges = False , use_mesh_vertices = False , export_cameras = False , use_selection = False , use_visible = False , use_renderable = False , use_active_collection_with_nested = True , use_active_collection = False , use_active_scene = False , collection = '' , at_collection_center = False , export_extras = False , export_yup = True , export_apply = False , export_shared_accessors = False , export_animations = True , export_frame_range = False , export_frame_step = 1 , export_force_sampling = True , export_sampling_interpolation_fallback = 'LINEAR' , export_pointer_animation = False , export_animation_mode = 'ACTIONS' , export_nla_strips_merged_animation_name = 'Animation' , export_def_bones = False , export_hierarchy_flatten_bones = False , export_hierarchy_flatten_objs = False , export_armature_object_remove = False , export_leaf_bone = False , export_optimize_animation_size = True , export_optimize_animation_keep_anim_armature = True , export_optimize_animation_keep_anim_object = False , export_optimize_disable_viewport = False , export_negative_frame = 'SLIDE' , export_anim_slide_to_zero = False , export_bake_animation = False , export_merge_animation = 'ACTION' , export_anim_single_armature = True , export_reset_pose_bones = True , export_current_frame = False , export_rest_position_armature = True , export_anim_scene_split_object = True , export_skins = True , export_influence_nb = 4 , export_all_influences = False , export_morph = True , export_morph_normal = True , export_morph_tangent = False , export_morph_animation = True , export_morph_reset_sk_data = True , export_lights = False , export_try_sparse_sk = True , export_try_omit_sparse_sk = False , export_gpu_instances = False , export_action_filter = False , export_convert_animation_pointer = False , export_nla_strips = True , export_original_specular = False , will_save_settings = False , export_hierarchy_full_collections = False , export_extra_animations = False , export_loglevel = -1 , filter_glob = '*.glb' )

- export_animations ( bool ) – Animations, Exports active actions and NLA tracks as glTF animations (optional)
- export_frame_range ( bool ) – Limit to Playback Range, Clips animations to selected playback range (optional)
- export_frame_step ( int ) – Sampling Rate, How often to evaluate animated values (in frames) (in [1, 120], optional)
- export_force_sampling ( bool ) – Always Sample Animations, Apply sampling to all animations (optional)
- export_sampling_interpolation_fallback ( Literal [ 'LINEAR' , 'STEP' ] ) – Sampling Interpolation Fallback, Interpolation fallback for sampled animations, when the property is not keyed (optional)

- LINEAR
Linear – Linear interpolation between keyframes.

- STEP
Step – No interpolation between keyframes.

- export_pointer_animation ( bool ) – Export Animation Pointer (Experimental), Export material, Light & Camera animation as Animation Pointer. Available only for baked animation mode 'NLA Tracks' and 'Scene' (optional)
- export_animation_mode ( Literal [ 'ACTIONS' , '`ACTIVE_ACTIONS`' , 'BROADCAST' , '`NLA_TRACKS`' , 'SCENE' ] ) – Animation Mode, Export Animation mode (optional)

- ACTIONS
Actions – Export actions (actives and on NLA tracks) as separate animations.

- `ACTIVE_ACTIONS`
Active actions merged – All the currently assigned actions become one glTF animation.

- BROADCAST
Broadcast actions – Broadcast all compatible actions to all objects. Animated objects will get all actions compatible with them, others will get no animation at all.

- `NLA_TRACKS`
NLA Tracks – Export individual NLA Tracks as separate animation.

- SCENE
Scene – Export baked scene as a single animation.

- export_nla_strips_merged_animation_name ( str ) – Merged Animation Name, Name of single glTF animation to be exported (optional, never None)
- export_def_bones ( bool ) – Export Deformation Bones Only, Export Deformation bones only (optional)
- export_hierarchy_flatten_bones ( bool ) – Flatten Bone Hierarchy, Flatten Bone Hierarchy. Useful in case of non decomposable transformation matrix (optional)
- export_hierarchy_flatten_objs ( bool ) – Flatten Object Hierarchy, Flatten Object Hierarchy. Useful in case of non decomposable transformation matrix (optional)
- export_armature_object_remove ( bool ) – Remove Armature Object, Remove Armature object if possible. If Armature has multiple root bones, object will not be removed (optional)
- export_leaf_bone ( bool ) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data) (optional)
- export_optimize_animation_size ( bool ) – Optimize Animation Size, Reduce exported file size by removing duplicate keyframes (optional)
- export_optimize_animation_keep_anim_armature ( bool ) – Force Keeping Channels for Bones, If all keyframes are identical in a rig, force keeping the minimal animation. When off, all possible channels for the bones will be exported, even if empty (minimal animation, 2 keyframes) (optional)
- export_optimize_animation_keep_anim_object ( bool ) – Force Keeping Channel for Objects, If all keyframes are identical for object transformations, force keeping the minimal animation (optional)
- export_optimize_disable_viewport ( bool ) – Disable Viewport for Other Objects, When exporting animations, disable viewport for other objects, for performance (optional)
- export_negative_frame ( Literal [ 'SLIDE' , 'CROP' ] ) – Negative Frames, Negative Frames are slid or cropped (optional)

- SLIDE
Slide – Slide animation to start at frame 0.

- CROP
Crop – Keep only frames above frame 0.

- export_anim_slide_to_zero ( bool ) – Set All glTF Animation Starting at 0, Set all glTF animation starting at 0.0s. Can be useful for looping animations (optional)
- export_bake_animation ( bool ) – Bake All Objects Animations, Force exporting animation on every object. Can be useful when using constraints or driver. Also useful when exporting only selection (optional)
- export_merge_animation ( Literal [ '`NLA_TRACK`' , 'ACTION' , 'NONE' ] ) – Merge Animation, Merge Animations (optional)

- `NLA_TRACK`
NLA Track Names – Merge by NLA Track Names.

- ACTION
Actions – Merge by Actions.

- NONE
No Merge – Do Not Merge Animations.

- export_anim_single_armature ( bool ) – Export all Armature Actions, Export all actions, bound to a single armature. WARNING: Option does not support exports including multiple armatures (optional)
- export_reset_pose_bones ( bool ) – Reset Pose Bones Between Actions, Reset pose bones between each action exported. This is needed when some bones are not keyed on some animations (optional)
- export_current_frame ( bool ) – Use Current Frame as Object Rest Transformations, Export the scene in the current animation frame. When off, frame 0 is used as rest transformations for objects (optional)
- export_rest_position_armature ( bool ) – Use Rest Position Armature, Export armatures using rest position as joints' rest pose. When off, current frame pose is used as rest pose (optional)
- export_anim_scene_split_object ( bool ) – Split Animation by Object, Export Scene as seen in Viewport, But split animation by Object (optional)

[Related references](INDEX.md).
