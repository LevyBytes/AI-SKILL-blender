# bpy.ops.wm.usd_export: usd_export textures, paths and transform representation

bpy.ops.wm. usd_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , selected_objects_only = False , collection = '' , export_animation = False , export_hair = False , export_uvmaps = True , rename_uvmaps = True , export_mesh_colors = True , export_normals = True , export_materials = True , export_subdivision = '`BEST_MATCH`' , export_armatures = True , only_deform_bones = False , export_shapekeys = True , use_instancing = False , evaluation_mode = 'RENDER' , generate_preview_surface = True , generate_materialx_network = False , convert_orientation = False , export_global_forward_selection = '`NEGATIVE_Z`' , export_global_up_selection = 'Y' , export_textures_mode = 'NEW' , overwrite_textures = False , relative_paths = True , xform_op_mode = 'TRS' , root_prim_path = '/root' , export_custom_properties = True , custom_properties_namespace = 'userProperties' , accessibility_label = '' , accessibility_description = '' , author_blender_name = True , convert_world_material = True , allow_unicode = True , export_meshes = True , export_lights = True , export_cameras = True , export_curves = True , export_points = True , export_volumes = True , triangulate_meshes = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , usdz_downscale_size = 'KEEP' , usdz_downscale_custom_size = 128 , merge_parent_xform = False , convert_scene_units = 'METERS' , meters_per_unit = 1.0 ) 

- export_textures_mode ( Literal [ 'KEEP' , 'PRESERVE' , 'NEW' ] ) – Export Textures, Surface map delivery method (optional)

- KEEP
Keep – Maintain original location of surfaces.

- PRESERVE
Preserve – Keep file positioning of surfaces from previously brought USD information.
Ship extra surfaces to a 'images' folder near the USD data.

- NEW
New Path – Ship surfaces to a 'images' folder near the USD data.

- overwrite_textures ( bool ) – Overwrite Textures, Overwrite existing documents when writing surfaces (optional)

- relative_paths ( bool ) – Relative Paths, Utilize relative links to mention external documents (e.g. surfaces, quantity) in USD, or else utilize full links (optional)

- xform_op_mode ( Literal [ 'TRS' , 'TOS' , 'MAT' ] ) – Xform Ops, Category of transform functions to create (optional)

- TRS
Translate, Rotate, Scale – Write utilizing move, rotate, and expand Xform functions.

- TOS
Translate, Orient, Scale – Write utilizing move, point quaternion, and expand Xform functions.

- MAT
Matrix – Write math function.

- root_prim_path ( str ) – Root Prim, If given, append a translate element with the specified label to the set as the chief of all written material (optional, never None)

- export_custom_properties ( bool ) – Custom Properties, Write personalized qualities as USD qualities (optional)

- custom_properties_namespace ( str ) – Namespace, If given, add the specified namespace as a label to written individualized characteristic codes. This operates only to names that lack a previous tag (e.g., it handles 'bar' but rejects 'foo:bar') and does not apply to blender thing and file labels which are constantly written in the 'userProperties:blender' namespace (optional, never None)

- accessibility_label ( str ) – Label, Make the ease-of-use identifier for the written set's principal element (optional, never None)

- accessibility_description ( str ) – Description, Make the ease-of-use narrative for the written set's principal element (optional, never None)

- author_blender_name ( bool ) – Blender Names, Compose USD personalized characteristics bearing the actual Blender thing and file information codes (optional)

- convert_world_material ( bool ) – World Dome Light, Shift the environmental material to a USD illuminated hemisphere. Presently functions for uncomplicated materials, made of a background photo attached to a lighting filter, with a possible arithmetic operation of the photo coloration (optional)

- allow_unicode ( bool ) – Allow Unicode, Maintain UTF-8 translation signs when composing USD label and characteristic codes (wants package utilizing USD 24.03 or greater when unlocking the output documents) (optional)

- export_meshes ( bool ) – Meshes, Send all surfaces (optional)

- export_lights ( bool ) – Lights, Send all illumination (optional)

- export_cameras ( bool ) – Cameras, Send all lenses (optional)

- export_curves ( bool ) – Curves, Send all arcs (optional)

- export_points ( bool ) – Point Clouds, Send all mark gatherings (optional)

- export_volumes ( bool ) – Volumes, Send all areas (optional)

- triangulate_meshes ( bool ) – Triangulate Meshes, Convert meshes to triangles during delivery (optional)

- quad_method (Literal[Modifier Triangulate Quad Method Items]) – Quad Method, Technique for breaking the quadrangles to triangles (optional)

- ngon_method (Literal[Modifier Triangulate Ngon Method Items]) – N-gon Method, Technique for breaking the n-sided shapes to triangles (optional)

[Related references](INDEX.md).
