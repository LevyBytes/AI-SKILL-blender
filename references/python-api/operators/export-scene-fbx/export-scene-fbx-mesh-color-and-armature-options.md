# bpy.ops.export_scene.fbx: FBX mesh, color and armature options

**bpy.ops.export_scene.fbx**( * , filepath = '' , check_existing = True , filter_glob = '*.fbx' , use_selection = False , use_visible = False , use_active_collection = False , collection = '' , global_scale = 1.0 , apply_unit_scale = True , apply_scale_options = '`FBX_SCALE_NONE`' , use_space_transform = True , bake_space_transform = False , object_types = {'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'} , use_mesh_modifiers = True , use_mesh_modifiers_render = True , mesh_smooth_type = 'OFF' , colors_type = 'SRGB' , prioritize_active_color = False , use_subsurf = False , use_mesh_edges = False , use_tspace = False , use_triangles = False , use_custom_props = False , add_leaf_bones = True , primary_bone_axis = 'Y' , secondary_bone_axis = 'X' , use_armature_deform_only = False , armature_nodetype = 'NULL' , bake_anim = True , bake_anim_use_all_bones = True , bake_anim_use_nla_strips = True , bake_anim_use_all_actions = True , bake_anim_force_startend_keying = True , bake_anim_step = 1.0 , bake_anim_simplify_factor = 1.0 , path_mode = 'AUTO' , embed_textures = False , batch_mode = 'OFF' , use_batch_own_dir = True , use_metadata = True , axis_forward = '-Z' , axis_up = 'Y' )

- use_mesh_modifiers ( bool ) – Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys (optional)
- use_mesh_modifiers_render ( bool ) – Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8) (optional)
- mesh_smooth_type ( Literal [ 'OFF' , 'FACE' , 'EDGE' , '`SMOOTH_GROUP`' ] ) – Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understands custom normals) (optional)

- OFF
Normals Only – Export only normals instead of writing edge or face smoothing data.

- FACE
Face – Write face smoothing.

- EDGE
Edge – Write edge smoothing.

- `SMOOTH_GROUP`
Smoothing Groups – Write face smoothing groups.

- colors_type ( Literal [ 'NONE' , 'SRGB' , 'LINEAR' ] ) – Vertex Colors, Export vertex color attributes (optional)

- NONE
None – Do not export color attributes.

- SRGB
sRGB – Export colors in sRGB color space.

- LINEAR
Linear – Export colors in linear color space.

- prioritize_active_color ( bool ) – Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one (optional)
- use_subsurf ( bool ) – Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if 'Apply Modifiers' is enabled) (optional)
- use_mesh_edges ( bool ) – Loose Edges, Export loose edges (as two-vertices polygons) (optional)
- use_tspace ( bool ) – Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!) (optional)
- use_triangles ( bool ) – Triangulate Faces, Convert all faces to triangles (optional)
- use_custom_props ( bool ) – Custom Properties, Export custom properties (optional)
- add_leaf_bones ( bool ) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data) (optional)
- primary_bone_axis ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Primary Bone Axis, (optional)
- secondary_bone_axis ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Secondary Bone Axis, (optional)
- use_armature_deform_only ( bool ) – Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children) (optional)

- armature_nodetype ( Literal [ 'NULL' , 'ROOT' , 'LIMBNODE' ] ) – Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use the Null type unless you experience issues with the other app, as other choices may not import back perfectly into Blender…) (optional)

- NULL
Null – 'Null' FBX node, similar to Blender's Empty (default).

- ROOT
Root – 'Root' FBX node, supposed to be the root of chains of bones….

- LIMBNODE
LimbNode – 'LimbNode' FBX node, a regular joint between two bones….

[Related references](INDEX.md).
