# bpy.ops.wm.usd_export: declaration-and-arguments

bpy.ops.wm. usd_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , selected_objects_only = False , collection = '' , export_animation = False , export_hair = False , export_uvmaps = True , rename_uvmaps = True , export_mesh_colors = True , export_normals = True , export_materials = True , export_subdivision = '`BEST_MATCH`' , export_armatures = True , only_deform_bones = False , export_shapekeys = True , use_instancing = False , evaluation_mode = 'RENDER' , generate_preview_surface = True , generate_materialx_network = False , convert_orientation = False , export_global_forward_selection = '`NEGATIVE_Z`' , export_global_up_selection = 'Y' , export_textures_mode = 'NEW' , overwrite_textures = False , relative_paths = True , xform_op_mode = 'TRS' , root_prim_path = '/root' , export_custom_properties = True , custom_properties_namespace = 'userProperties' , accessibility_label = '' , accessibility_description = '' , author_blender_name = True , convert_world_material = True , allow_unicode = True , export_meshes = True , export_lights = True , export_cameras = True , export_curves = True , export_points = True , export_volumes = True , triangulate_meshes = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , usdz_downscale_size = 'KEEP' , usdz_downscale_custom_size = 128 , merge_parent_xform = False , convert_scene_units = 'METERS' , meters_per_unit = 1.0 ) 

Ship the current composition as a USD storage file

Parameters :

- filepath ( str ) – File Path, Location to file (optional, never None)

- check_existing ( bool ) – Check Existing, Verify and warn when writing over files (optional)

- filter_blender ( bool ) – Filter .blend files, (optional)

- filter_backup ( bool ) – Filter backup .blend files, (optional)

- filter_image ( bool ) – Filter image files, (optional)

- filter_movie ( bool ) – Filter movie files, (optional)

- filter_python ( bool ) – Filter Python files, (optional)

- filter_font ( bool ) – Filter font files, (optional)

- filter_sound ( bool ) – Filter sound files, (optional)

- filter_text ( bool ) – Filter text files, (optional)

- filter_archive ( bool ) – Filter archive files, (optional)

- filter_btx ( bool ) – Filter btx files, (optional)

- filter_alembic ( bool ) – Filter Alembic files, (optional)

- filter_usd ( bool ) – Filter USD files, (optional)

- filter_obj ( bool ) – Filter OBJ files, (optional)

- filter_volume ( bool ) – Filter OpenVDB volume files, (optional)

- filter_folder ( bool ) – Filter folders, (optional)

- filter_blenlib ( bool ) – Filter Blender IDs, (optional)

- filemode ( int ) – File Browser Mode, Configuration for the file browser type to open a .blend file, a library or specific file (in [1, 9], optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Identify display method for files automatically.

- `LIST_VERTICAL`
Short List – Show files in a brief list view.

- `LIST_HORIZONTAL`
Long List – Show files in a comprehensive tabular format.

- THUMBNAIL
Thumbnails – Show files as icon previews.

- sort_method ( str ) – File sorting mode, (optional)

- filter_glob ( str ) – (optional, never None)

- selected_objects_only ( bool ) – Selection Only, Ship only chosen things. Hidden ancestors of picked things are written as bare translate (optional)

- collection ( str ) – Collection, (optional, never None)

- export_animation ( bool ) – Animation, Ship all frames in the render frame set, rather than just the now frame (optional)

- export_hair ( bool ) – Hair, Ship hair particle arrays as USD lines (optional)

- export_uvmaps ( bool ) – UV Maps, Put all surface shade coordinates in the shipped file (optional)

- rename_uvmaps ( bool ) – Rename UV Maps, Rename main render shade coordinate to "st" to match USD rules (optional)

- export_mesh_colors ( bool ) – Color Attributes, Put surface hue properties in the shipped data (optional)

- export_normals ( bool ) – Normals, Add regular vectors for shipped meshes to the data (optional)

- export_materials ( bool ) – Materials, Transmit viewport configuration of materials as USD review materials, and transmit material links as shape subsets (optional)

- export_subdivision ( Literal [ 'IGNORE' , 'TESSELLATE' , '`BEST_MATCH`' ] ) – Subdivision, Pick how subdivision changes get mapped to the USD subdivision type on transmit (optional)

- IGNORE
Ignore – Scheme = None. Write foundation mesh no subdivision.

- TESSELLATE
Tessellate – Scheme = None. Write subdivided mesh.

- `BEST_MATCH`
Best Match – Scheme = Catmull-Clark, as feasible. Reverts to writing the subdivided mesh for the Basic subdivision classification.

- export_armatures ( bool ) – Armatures, Write joint systems and meshes with joint changes as USD joint structures and shaped meshes (optional)

[Related references](INDEX.md).
