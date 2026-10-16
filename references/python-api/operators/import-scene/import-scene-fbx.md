# bpy.ops.import_scene.fbx

bpy.ops.import_scene. fbx ( * , filepath = '' , directory = '' , filter_glob = '*.fbx' , files = None , ui_tab = 'MAIN' , use_manual_orientation = False , global_scale = 1.0 , bake_space_transform = False , use_custom_normals = True , colors_type = 'SRGB' , use_image_search = True , use_alpha_decals = False , decal_offset = 0.0 , use_anim = True , anim_offset = 1.0 , use_subsurf = False , use_custom_props = True , use_custom_props_enum_as_string = True , ignore_leaf_bones = False , force_connect_children = False , automatic_bone_orientation = False , primary_bone_axis = 'Y' , secondary_bone_axis = 'X' , use_prepost_rot = True , mtl_name_collision_mode = '`MAKE_UNIQUE`' , axis_forward = '-Z' , axis_up = 'Y' )

Load a FBX file

Parameters :

- filepath ( str ) – File Path, Filepath used for importing the file (optional, never None)

- directory ( str ) – directory, (optional, never None)

- filter_glob ( str ) – filter_glob, (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – File Path, (optional)

- ui_tab ( Literal [ 'MAIN' , 'ARMATURE' ] ) – ui_tab, Categories of import options (optional)

- MAIN
Main – Main basic settings.

- ARMATURE
Armatures – Armature-related settings.

- use_manual_orientation ( bool ) – Manual Orientation, Set orientation and scale yourself rather than relying on the data embedded in the FBX file (optional)

- global_scale ( float ) – Scale, (in [0.001, 1000], optional)

- bake_space_transform ( bool ) – Apply Transform, Bake the space transform into the object data, which avoids unwanted rotations when the target space is not aligned with Blender's space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations) (optional)

- use_custom_normals ( bool ) – Custom Normals, Bring in custom normals when present (otherwise Blender recomputes them) (optional)

- colors_type ( Literal [ 'NONE' , 'SRGB' , 'LINEAR' ] ) – Vertex Colors, Bring in vertex color attributes (optional)

- NONE
None – Skip importing color attributes.

- SRGB
sRGB – Treat the file's colors as sRGB.

- LINEAR
Linear – Treat the file's colors as linear.

- use_image_search ( bool ) – Image Search, Look through subdirectories for related images (WARNING: may be slow) (optional)

- use_alpha_decals ( bool ) – Alpha Decals, Handle materials with alpha as decals that cast no shadows (optional)

- decal_offset ( float ) – Decal Offset, Push the geometry of alpha meshes outward (in [0, 1], optional)

- use_anim ( bool ) – Import Animation, Bring in the FBX animation (optional)

- anim_offset ( float ) – Animation Offset, Frame offset applied to the animation as it imports (in [-inf, inf], optional)

- use_subsurf ( bool ) – Subdivision Data, Turn FBX subdivision information into subdivision surface modifiers (optional)

- use_custom_props ( bool ) – Custom Properties, Bring in user properties as custom properties (optional)

- use_custom_props_enum_as_string ( bool ) – Import Enums As Strings, Keep enumeration values as strings (optional)

- ignore_leaf_bones ( bool ) – Ignore Leaf Bones, Skip the final bone of each chain (used only to mark the previous bone's length) (optional)

- force_connect_children ( bool ) – Force Connect Children, Connect child bones to their parent even when the computed head/tail positions disagree (handy for pure-joint armatures) (optional)

- automatic_bone_orientation ( bool ) – Automatic Bone Orientation, Try to point each bone's major axis toward its children (optional)

- primary_bone_axis ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Primary Bone Axis, (optional)

- secondary_bone_axis ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Secondary Bone Axis, (optional)

- use_prepost_rot ( bool ) – Use Pre/Post Rotation, Apply pre/post rotation from the FBX transform (you may need to turn this off in some cases) (optional)

- mtl_name_collision_mode ( Literal [ '`MAKE_UNIQUE`' , '`REFERENCE_EXISTING`' ] ) – Material Name Collision, What to do when an imported material's name clashes with an existing one (optional)

- `MAKE_UNIQUE`
Make Unique – Bring in each FBX material as its own Blender material.

- `REFERENCE_EXISTING`
Reference Existing – When a material of the same name already exists, point at it instead of importing a copy.

- axis_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Forward, (optional)

- axis_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Up, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
