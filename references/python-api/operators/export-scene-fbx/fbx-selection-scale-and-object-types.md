# bpy.ops.export_scene.fbx: object selection, scale and transforms

**bpy.ops.export_scene.fbx**( * , filepath = '' , check_existing = True , filter_glob = '*.fbx' , use_selection = False , use_visible = False , use_active_collection = False , collection = '' , global_scale = 1.0 , apply_unit_scale = True , apply_scale_options = '`FBX_SCALE_NONE`' , use_space_transform = True , bake_space_transform = False , object_types = {'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'} , use_mesh_modifiers = True , use_mesh_modifiers_render = True , mesh_smooth_type = 'OFF' , colors_type = 'SRGB' , prioritize_active_color = False , use_subsurf = False , use_mesh_edges = False , use_tspace = False , use_triangles = False , use_custom_props = False , add_leaf_bones = True , primary_bone_axis = 'Y' , secondary_bone_axis = 'X' , use_armature_deform_only = False , armature_nodetype = 'NULL' , bake_anim = True , bake_anim_use_all_bones = True , bake_anim_use_nla_strips = True , bake_anim_use_all_actions = True , bake_anim_force_startend_keying = True , bake_anim_step = 1.0 , bake_anim_simplify_factor = 1.0 , path_mode = 'AUTO' , embed_textures = False , batch_mode = 'OFF' , use_batch_own_dir = True , use_metadata = True , axis_forward = '-Z' , axis_up = 'Y' )

Save scene as FBX file.

Parameters:
- filepath ( str ) – File Path, Filepath used for exporting the file (optional, never None)
- check_existing ( bool ) – Check Existing, Check and warn on overwriting existing files (optional)
- filter_glob ( str ) – filter_glob, (optional, never None)
- use_selection ( bool ) – Selected Objects, Only export chosen and visible objects (optional)
- use_visible ( bool ) – Visible Objects, Only export objects you can see (optional)
- use_active_collection ( bool ) – Active Collection, Only export objects from the active collection (and its children) (optional)
- collection ( str ) – Source Collection, Only export objects from this collection (and its children) (optional, never None)
- global_scale ( float ) – Scale, Resize all geometry (Note: Some importers do not support scaled armatures!) (in [0.001, 1000], optional)
- apply_unit_scale ( bool ) – Apply Unit, Account for Blender's native units (if off, raw Blender units are preserved) (optional)
- apply_scale_options ( Literal [ '`FBX_SCALE_NONE`' , '`FBX_SCALE_UNITS`' , '`FBX_SCALE_CUSTOM`' , '`FBX_SCALE_ALL`' ] ) – Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way) (optional)

- `FBX_SCALE_NONE`
All Local – Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

- `FBX_SCALE_UNITS`
FBX Units Scale – Apply custom scaling to each object transformation, and units scaling to FBX scale.

- `FBX_SCALE_CUSTOM`
FBX Custom Scale – Apply custom scaling to FBX scale, and units scaling to each object transformation.

- `FBX_SCALE_ALL`
FBX All – Apply custom scaling and units scaling to FBX scale.

- use_space_transform ( bool ) – Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is (optional)
- bake_space_transform ( bool ) – Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations) (optional)
- object_types ( set [ Literal [ 'EMPTY' , 'CAMERA' , 'LIGHT' , 'ARMATURE' , 'MESH' , 'OTHER' ] ] ) – Object Types, Which kind of object to export (optional)

- EMPTY
Empty.

- CAMERA
Camera.

- LIGHT
Lamp.

- ARMATURE
Armature – WARNING: not supported in dupli/group instances.

- MESH
Mesh.

- OTHER
Other – Other geometry types, like curve, meta-ball, etc. (converted to meshes).

[Related references](INDEX.md).
