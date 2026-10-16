# bpy.ops.export_scene.fbx: FBX animation, paths, batches, axes and return

**bpy.ops.export_scene.fbx**( * , filepath = '' , check_existing = True , filter_glob = '*.fbx' , use_selection = False , use_visible = False , use_active_collection = False , collection = '' , global_scale = 1.0 , apply_unit_scale = True , apply_scale_options = '`FBX_SCALE_NONE`' , use_space_transform = True , bake_space_transform = False , object_types = {'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'} , use_mesh_modifiers = True , use_mesh_modifiers_render = True , mesh_smooth_type = 'OFF' , colors_type = 'SRGB' , prioritize_active_color = False , use_subsurf = False , use_mesh_edges = False , use_tspace = False , use_triangles = False , use_custom_props = False , add_leaf_bones = True , primary_bone_axis = 'Y' , secondary_bone_axis = 'X' , use_armature_deform_only = False , armature_nodetype = 'NULL' , bake_anim = True , bake_anim_use_all_bones = True , bake_anim_use_nla_strips = True , bake_anim_use_all_actions = True , bake_anim_force_startend_keying = True , bake_anim_step = 1.0 , bake_anim_simplify_factor = 1.0 , path_mode = 'AUTO' , embed_textures = False , batch_mode = 'OFF' , use_batch_own_dir = True , use_metadata = True , axis_forward = '-Z' , axis_up = 'Y' )

- bake_anim ( bool ) – Baked Animation, Export baked keyframe animation (optional)
- bake_anim_use_all_bones ( bool ) – Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4) (optional)
- bake_anim_use_nla_strips ( bool ) – NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation (optional)
- bake_anim_use_all_actions ( bool ) – All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all) (optional)
- bake_anim_force_startend_keying ( bool ) – Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels (optional)
- bake_anim_step ( float ) – Sampling Rate, How often to evaluate animated values (in frames) (in [0.01, 100], optional)
- bake_anim_simplify_factor ( float ) – Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified) (in [0, 100], optional)
- path_mode ( Literal [ 'AUTO' , 'ABSOLUTE' , 'RELATIVE' , 'MATCH' , 'STRIP' , 'COPY' ] ) – Path Mode, Method used to reference paths (optional)

- AUTO
Auto – Use relative paths with subdirectories only.

- ABSOLUTE
Absolute – Always write absolute paths.

- RELATIVE
Relative – Write relative paths where possible.

- MATCH
Match – Match absolute/relative setting with input path.

- STRIP
Strip – Filename only.

- COPY
Copy – Copy the file to the destination path (or subdirectory).

- embed_textures ( bool ) – Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!) (optional)
- batch_mode ( Literal [ 'OFF' , 'SCENE' , 'COLLECTION' , '`SCENE_COLLECTION`' , '`ACTIVE_SCENE_COLLECTION`' ] ) – Batch Mode, (optional)

- OFF
Off – Active scene to file.

- SCENE
Scene – Each scene as a file.

- COLLECTION
Collection – Each collection (data-block ones) as a file, does not include content of children collections.

- `SCENE_COLLECTION`
Scene Collections – Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.

- `ACTIVE_SCENE_COLLECTION`
Active Scene Collections – Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.

- use_batch_own_dir ( bool ) – Batch Own Dir, Create a dir for each exported file (optional)
- use_metadata ( bool ) – Use Metadata, (optional)
- axis_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Forward, (optional)
- axis_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Up, (optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

File: addons_core/io_scene_fbx/__init__.py:604

[Related references](INDEX.md).
