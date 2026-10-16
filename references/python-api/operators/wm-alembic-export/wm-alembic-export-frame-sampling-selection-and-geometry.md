# bpy.ops.wm.alembic_export: alembic_export frame sampling, selection and geometry

bpy.ops.wm. alembic_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = True , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , filter_glob = '*.abc' , start = -2147483648 , end = -2147483648 , xsamples = 1 , gsamples = 1 , sh_open = 0.0 , sh_close = 1.0 , selected = False , flatten = False , collection = '' , uvs = True , packuv = True , normals = True , vcolors = False , orcos = True , face_sets = False , subdiv_schema = False , apply_subdiv = False , curves_as_mesh = False , use_instancing = True , global_scale = 1.0 , triangulate = False , quad_method = '`SHORTEST_DIAGONAL`' , ngon_method = 'BEAUTY' , export_hair = True , export_particles = True , export_custom_properties = True , as_background_job = False , evaluation_mode = 'RENDER' , init_scene_frame_range = True ) 

- start ( int ) - Start Frame, Initial frame for the export, or current scene's start if using default (in [-inf, inf], optional)

- end ( int ) - End Frame, Final frame for the export, or current scene's end if using default (in [-inf, inf], optional)

- xsamples ( int ) - Transform Samples, Sampling count per frame for motion transformations (in [1, 128], optional)

- gsamples ( int ) - Geometry Samples, Sampling count per frame for shape data (in [1, 128], optional)

- sh_open ( float ) - Shutter Open, Frame position when the shutter begins recording (in [-1, 1], optional)

- sh_close ( float ) - Shutter Close, Frame position when the shutter stops recording (in [-1, 1], optional)

- selected ( bool ) - Selected Objects Only, Exports only the highlighted geometry (optional)

- flatten ( bool ) - Flatten Hierarchy, Discards parent-child connections (optional)

- collection ( str ) - Collection, (optional, never None)

- uvs ( bool ) - UV Coordinates, Outputs texture coordinates (optional)

- packuv ( bool ) - Merge UVs, (optional)

- normals ( bool ) - Normals, Outputs surface orientation data (optional)

- vcolors ( bool ) - Color Attributes, Outputs color information (optional)

- orcos ( bool ) - Generated Coordinates, Outputs unmodified vertex positions (optional)

- face_sets ( bool ) - Face Sets, Outputs per-face shading assignments (optional)

- subdiv_schema ( bool ) - Use Subdivision Schema, Outputs meshes using Alembic's subdivision method (optional)

- apply_subdiv ( bool ) - Apply Subdivision Surface, Outputs subdivision surfaces as polygon meshes (optional)

- curves_as_mesh ( bool ) - Curves as Mesh, Outputs curves and NURBS as polygon meshes (optional)

- use_instancing ( bool ) - Use Instancing, Outputs duplicated geometry as Alembic instances; reduces file size yet may limit compatibility with other applications (optional)

- global_scale ( float ) - Scale, Factor to enlarge or reduce geometry relative to world space (in [0.0001, 1000], optional)

- triangulate ( bool ) - Triangulate, Outputs polygonal faces as triangle subdivisions (optional)

- quad_method (Literal[Modifier Triangulate Quad Method Items]) - Quad Method, Technique for splitting quadrilaterals (optional)

- ngon_method (Literal[Modifier Triangulate Ngon Method Items]) - N-gon Method, Technique for splitting polygons (optional)

- export_hair ( bool ) - Export Hair, Outputs hair particle geometry as keyframed splines (optional)

- export_particles ( bool ) - Export Particles, Outputs non-hair particle systems (optional)

- export_custom_properties ( bool ) - Export Custom Properties, Outputs user-defined parameters to Alembic .userProperties (optional)

- as_background_job ( bool ) - Run as Background Job, Allows the import to execute in the background without blocking Blender. This functionality is superseded; EXECUTE to run in the foreground, and INVOKE to run as a background operation (optional)

- evaluation_mode ( Literal [ 'RENDER' , 'VIEWPORT' ] ) - Settings, Indicates visibility behavior, modifier configuration, and contexts with distinct viewport and rendering parameters (optional)

- RENDER
Render - Applies rendering configuration to visibility and modifiers.

- VIEWPORT
Viewport - Applies viewport configuration to visibility and modifiers.

- init_scene_frame_range ( bool ) - (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
