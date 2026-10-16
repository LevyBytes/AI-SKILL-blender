# bpy.ops.wm.usd_import: usd_import materials, lights and textures

bpy.ops.wm. usd_import ( * , filepath = '' , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , scale = 1.0 , set_frame_range = True , import_cameras = True , import_curves = True , import_lights = True , import_materials = True , import_meshes = True , import_volumes = True , import_shapes = True , import_skeletons = True , import_blendshapes = True , import_points = True , import_subdivision = False , support_scene_instancing = True , import_visible_only = True , create_collection = False , read_mesh_uvs = True , read_mesh_colors = True , read_mesh_attributes = True , prim_path_mask = '' , import_guide = False , import_proxy = False , import_render = True , import_all_materials = False , import_usd_preview = True , set_material_blend = True , light_intensity_scale = 1.0 , mtl_purpose = '`MTL_FULL`' , mtl_name_collision_mode = '`MAKE_UNIQUE`' , import_textures_mode = '`IMPORT_PACK`' , import_textures_dir = '//textures/' , tex_name_collision_mode = '`USE_EXISTING`' , property_import_mode = 'ALL' , validate_meshes = False , create_world_material = True , import_defined_only = True , merge_parent_xform = True , apply_unit_conversion_scale = True ) 

- import_all_materials ( bool ) – Import All Materials, Also bring materials that lack usage by any material. Remember that when this choice is false, materials utilized by material will remain brought (optional)

- import_usd_preview ( bool ) – Import USD Preview, Transmute UsdPreviewSurface color programs to Principled BSDF color schemes (optional)

- set_material_blend ( bool ) – Set Material Blend, If the Bring USD Preview choice is turned on, the material mix method will be configured automatically grounded on the color program's opacity and opacityThreshold characteristics (optional)

- light_intensity_scale ( float ) – Light Intensity Scale, Growth for the power of brought-in illumination (in [0.0001, 10000], optional)

- mtl_purpose ( Literal [ '`MTL_ALL_PURPOSE`' , '`MTL_PREVIEW`' , '`MTL_FULL`' ] ) – Material Purpose, Endeavor to bring materials with the designated objective. If no material bearing this objective is fastened to the item, revert on bringing any substitute fastened material (optional)

- `MTL_ALL_PURPOSE`
All Purpose – Strive to bring 'allPurpose' materials.

- `MTL_PREVIEW`
Preview – Strive to bring 'preview' materials. Bring 'allPurpose' materials as a fallback.

- `MTL_FULL`
Full – Strive to bring 'full' materials. Bring 'allPurpose' or 'preview' materials, in that ranking, as a fallback.

- mtl_name_collision_mode ( Literal [ '`MAKE_UNIQUE`' , '`REFERENCE_EXISTING`' ] ) – Material Name Collision, Procedure when the identifier of a brought-in material overlaps with a present material (optional)

- `MAKE_UNIQUE`
Make Unique – Bring each USD material as a discrete Blender material.

- `REFERENCE_EXISTING`
Reference Existing – If a material carrying the same identifier currently remains, utilize that rather than bringing.

- import_textures_mode ( Literal [ '`IMPORT_NONE`' , '`IMPORT_PACK`' , '`IMPORT_COPY`' ] ) – Import Textures, Procedure when getting surfaces from a USDZ storage file (optional)

- `IMPORT_NONE`
None – Don't bring surfaces.

- `IMPORT_PACK`
Packed – Bring surfaces as compressed information.

- `IMPORT_COPY`
Copy – Duplicate documents to surfaces folder.

- import_textures_dir ( str ) – Textures Directory, Direction to the folder where brought surfaces will be duplicated (optional, never None)

- tex_name_collision_mode ( Literal [ '`USE_EXISTING`' , 'OVERWRITE' ] ) – File Name Collision, Procedure when the identifier of a brought document disputes with a present document (optional)

- `USE_EXISTING`
Use Existing – If a document with the matching identifier currently exists, utilize that rather than duplicating.

- OVERWRITE
Overwrite – Overwrite present documents.

- property_import_mode ( Literal [ 'NONE' , 'USER' , 'ALL' ] ) – Custom Properties, Procedure when getting USD qualities as Blender customized characteristics (optional)

- NONE
None – Do not get USD customized characteristics.

- USER
User – Get USD qualities in the 'userProperties' namespace as Blender customized characteristics. The namespace will be stripped from the property identifiers.

- ALL
All Custom – Get every USD customized qualities as Blender customized characteristics. Namespaces will be maintained in the property identifiers.

- validate_meshes ( bool ) – Validate Meshes, Verify that the content is sound (when deactivated, brought content may create slowdowns or crashes when viewing or altering) (optional)

- create_world_material ( bool ) – World Dome Light, Shift the initially encountered USD dome illumination to a planetary lighting filter (optional)

- import_defined_only ( bool ) – Defined Primitives Only, Bring merely interpreted USD structures. When deactivated this permits bringing USD structures which stay unfulfilled, for instance those bearing an alternative signifier (optional)

- merge_parent_xform ( bool ) – Merge parent Xform, Let USD structures unite with their Xform ancestor if they are the sole heir in the ranking (optional)

- apply_unit_conversion_scale ( bool ) – Apply Unit Conversion Scale, Modify the setup things by the USD set's meters per measurement amount. This alteration is employed in appendix to the amount specified in the Growth choice (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
