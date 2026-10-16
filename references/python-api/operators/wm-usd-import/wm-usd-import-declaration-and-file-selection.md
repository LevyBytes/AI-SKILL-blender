# bpy.ops.wm.usd_import: usd_import declaration and file selection

bpy.ops.wm. usd_import ( * , filepath = '' , check_existing = False , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = True , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.usd' , scale = 1.0 , set_frame_range = True , import_cameras = True , import_curves = True , import_lights = True , import_materials = True , import_meshes = True , import_volumes = True , import_shapes = True , import_skeletons = True , import_blendshapes = True , import_points = True , import_subdivision = False , support_scene_instancing = True , import_visible_only = True , create_collection = False , read_mesh_uvs = True , read_mesh_colors = True , read_mesh_attributes = True , prim_path_mask = '' , import_guide = False , import_proxy = False , import_render = True , import_all_materials = False , import_usd_preview = True , set_material_blend = True , light_intensity_scale = 1.0 , mtl_purpose = '`MTL_FULL`' , mtl_name_collision_mode = '`MAKE_UNIQUE`' , import_textures_mode = '`IMPORT_PACK`' , import_textures_dir = '//textures/' , tex_name_collision_mode = '`USE_EXISTING`' , property_import_mode = 'ALL' , validate_meshes = False , create_world_material = True , import_defined_only = True , merge_parent_xform = True , apply_unit_conversion_scale = True ) 

Bring USD arrangement into the present setting

Parameters :

- filepath ( str ) – File Path, Location to file (optional, never None)

- check_existing ( bool ) – Check Existing, Verify and warn when writing over documents (optional)

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

- filemode ( int ) – File Browser Mode, Configuration for the file browser type to bring a .blend file, a library or specific document (in [1, 9], optional)

- relative_path ( bool ) – Relative Path, Choose the document relative to the blend file (optional)

- display_type ( Literal [ 'DEFAULT' , '`LIST_VERTICAL`' , '`LIST_HORIZONTAL`' , 'THUMBNAIL' ] ) – Display Type, (optional)

- DEFAULT
Default – Pick display method for documents automatically.

- `LIST_VERTICAL`
Short List – Show documents as short list.

- `LIST_HORIZONTAL`
Long List – Show documents as detailed list.

- THUMBNAIL
Thumbnails – Show documents as thumbnails.

- sort_method ( str ) – File sorting mode, (optional)

- filter_glob ( str ) – (optional, never None)

[Related references](INDEX.md).
