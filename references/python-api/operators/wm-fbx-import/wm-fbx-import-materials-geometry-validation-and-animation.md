# bpy.ops.wm.fbx_import: fbx_import materials, geometry, validation and animation

bpy.ops.wm. fbx_import ( * , filepath = '' , directory = '' , files = None , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , global_scale = 1.0 , mtl_name_collision_mode = '`MAKE_UNIQUE`' , import_colors = 'SRGB' , use_custom_normals = True , use_custom_props = True , use_custom_props_enum_as_string = True , import_subdivision = False , ignore_leaf_bones = False , validate_meshes = True , use_anim = True , anim_offset = 1.0 , filter_glob = '*.fbx' ) 

- global_scale ( float ) - Scale, (in [1e-06, 1e+06], optional)

- mtl_name_collision_mode ( Literal [ '`MAKE_UNIQUE`' , '`REFERENCE_EXISTING`' ] ) - Material Name Collision, Conduct when an imported material shares a name with an existing material (optional)

- `MAKE_UNIQUE`
Make Unique - Adds each FBX material as a separate Blender material.

- `REFERENCE_EXISTING`
Reference Existing - When a material shares the same name, links to the existing one rather than importing a copy.

- import_colors ( Literal [ 'NONE' , 'SRGB' , 'LINEAR' ] ) - Vertex Colors, Ingests vertex color information (optional)

- NONE
None - Disables color attribute import.

- SRGB
sRGB - Vertex colors present in sRGB color space.

- LINEAR
Linear - Vertex colors present in linear color space.

- use_custom_normals ( bool ) - Custom Normals, Ingests personalized normals, or Blender will generate them (optional)

- use_custom_props ( bool ) - Custom Properties, Ingests user-defined characteristics as personalized variables (optional)

- use_custom_props_enum_as_string ( bool ) - Enums As Strings, Stores customized enumeration settings as words (optional)

- import_subdivision ( bool ) - Subdivision Data, Ingests FBX subdivision information as surface refinement modifiers (optional)

- ignore_leaf_bones ( bool ) - Ignore Leaf Bones, Disregards the final bone in each sequence (used to denote the size of the preceding bone) (optional)

- validate_meshes ( bool ) - Validate Meshes, Guarantees the structure is sound (when disabled, geometry might be imported causing application crashes during display or modification) (optional)

- use_anim ( bool ) - Import Animation, Ingests FBX motion sequences (optional)

- anim_offset ( float ) - Offset, Time displacement to apply to motion sequences, in frames (in [-1e+06, 1e+06], optional)

- filter_glob ( str ) - Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
