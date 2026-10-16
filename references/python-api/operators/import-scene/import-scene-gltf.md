# bpy.ops.import_scene.gltf

bpy.ops.import_scene. gltf ( * , filepath = '' , export_import_convert_lighting_mode = 'SPEC' , filter_glob = '*.glb;*.gltf' , directory = '' , files = None , loglevel = 0 , import_pack_images = True , merge_vertices = False , import_shading = 'NORMALS' , bone_heuristic = 'BLENDER' , disable_bone_shape = False , bone_shape_scale_factor = 1.0 , guess_original_bind_pose = True , import_webp_texture = False , import_unused_materials = False , import_select_created_objects = True , import_scene_extras = True , import_scene_as_collection = True , import_merge_material_slots = True )

Load a glTF 2.0 file

Parameters :

- filepath ( str ) – File Path, Filepath used for importing the file (optional, never None)

- export_import_convert_lighting_mode ( Literal [ 'SPEC' , 'COMPAT' , 'RAW' ] ) – Lighting Mode, Optional backwards compatibility for render engines that aren't standard. Affects lights (optional)

- SPEC
Standard – Physically-based glTF lighting units (cd, lx, nt).

- COMPAT
Unitless – Non-physical, unitless lighting. Handy when exposure controls are missing.

- RAW
Raw (Deprecated) – Blender lighting strengths with no conversion.

- filter_glob ( str ) – filter_glob, (optional, never None)

- directory ( str ) – directory, (optional, never None)

- files ( bpy_prop_collection [ OperatorFileListElement ]) – File Path, (optional)

- loglevel ( int ) – Log Level, Log Level (in [-inf, inf], optional)

- import_pack_images ( bool ) – Pack Images, Embed every image inside the .blend file (optional)

- merge_vertices ( bool ) – Merge Vertices, The glTF format stores discontinuous normals, UVs, and other vertex attributes as separate vertices, which is what typical graphics hardware needs for rendering. This option tries to fold co-located vertices back together where it can. It currently cannot merge vertices whose normals differ (optional)

- import_shading ( Literal [ 'NORMALS' , 'FLAT' , 'SMOOTH' ] ) – Shading, How normals are worked out during import (optional)

- bone_heuristic ( Literal [ 'BLENDER' , 'TEMPERANCE' , 'FORTUNE' ] ) – Bone Dir, Strategy for laying out bones. Aims to keep them tidy (optional)

- BLENDER
Blender (best for import/export round trip) – Best when re-importing glTFs that Blender exported, and when re-exporting them to glTF after editing in Blender. Bone tips sit on their local +Y axis (in glTF space).

- TEMPERANCE
Temperance (average) – A solid general-purpose choice. A bone with a single child gets its tip placed on the local axis nearest that child.

- FORTUNE
Fortune (may look better, less accurate) – May look nicer than Temperance but can also be wrong. A bone with a single child gets its tip placed at that child's root. Watch out: non-uniform scaling can break with this option.

- disable_bone_shape ( bool ) – Disable Bone Shape, Skip creating bone shapes (optional)

- bone_shape_scale_factor ( float ) – Bone Shape Scale, Scale applied to bone shapes (in [-inf, inf], optional)

- guess_original_bind_pose ( bool ) – Guess Original Bind Pose, Attempt to recover the original bind pose of skinned meshes from their inverse bind matrices. When off, use the default/rest pose as the bind pose (optional)

- import_webp_texture ( bool ) – Import WebP Textures, When a WebP version of a texture exists, load it instead of the PNG/JPEG fallback (optional)

- import_unused_materials ( bool ) – Import Unused Materials & Images, Bring in materials and images even if no mesh uses them (optional)

- import_select_created_objects ( bool ) – Select Imported Objects, Select the created objects once the import finishes (optional)

- import_scene_extras ( bool ) – Import Scene Extras, Bring in scene extras as custom properties. Any existing custom properties get overwritten (optional)

- import_scene_as_collection ( bool ) – Import Scene as Collection, Bring the scene in as a collection (optional)

- import_merge_material_slots ( bool ) – Merge Material Slot when possible, Combine material slots wherever it can be done (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
