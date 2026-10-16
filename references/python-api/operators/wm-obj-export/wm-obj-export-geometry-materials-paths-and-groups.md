# bpy.ops.wm.obj_export: obj_export geometry, materials, paths and groups

bpy.ops.wm. obj_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , export_animation = False , start_frame = -2147483648 , end_frame = 2147483647 , forward_axis = '`NEGATIVE_Z`' , up_axis = 'Y' , global_scale = 1.0 , apply_modifiers = True , apply_transform = True , export_eval_mode = '`DAG_EVAL_VIEWPORT`' , export_selected_objects = False , export_uv = True , export_normals = True , export_colors = False , export_materials = True , export_pbr_extensions = False , path_mode = 'AUTO' , export_triangulated_mesh = False , export_curves_as_nurbs = False , export_object_groups = False , export_material_groups = False , export_vertex_groups = False , export_smooth_groups = False , smooth_group_bitflags = False , filter_glob = '*.obj;*.mtl' , collection = '' ) 

- export_selected_objects ( bool ) – Export Selected Objects, Restrict export to currently-selected objects only (optional)

- export_uv ( bool ) – Export UVs, (optional)

- export_normals ( bool ) – Export Normals, Output per-face normals for flat-shaded faces, per-corner normals for smooth ones (optional)

- export_colors ( bool ) – Export Colors, Include color attributes at each vertex (optional)

- export_materials ( bool ) – Export Materials, Output MTL library. Image textures in MTL require a Principled-BSDF node (optional)

- export_pbr_extensions ( bool ) – Export Materials with PBR Extensions, Output MTL using PBR formats (roughness, metallic, sheen, coat, anisotropy, transmission) (optional)

- path_mode ( Literal [ 'AUTO' , 'ABSOLUTE' , 'RELATIVE' , 'MATCH' , 'STRIP' , 'COPY' ] ) – Path Mode, Approach for resolving file references (optional)

- AUTO
Auto – Use relative paths with subdirectories only.

- ABSOLUTE
Absolute – Always write absolute paths.

- RELATIVE
Relative – Write relative paths where possible.

- MATCH
Match – Match absolute/relative setting with input path.

- STRIP
Strip – Write filename only.

- COPY
Copy – Copy the file to the destination path.

- export_triangulated_mesh ( bool ) – Export Triangulated Mesh, Converts all ngons of 4+ vertices to triangles. Meshes in the scene are unaffected. Works like Triangulate with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4 (optional)

- export_curves_as_nurbs ( bool ) – Export Curves as NURBS, Write curves in parametric form rather than as mesh (optional)

- export_object_groups ( bool ) – Export Object Groups, Concatenate mesh name to object name with '_' separator (optional)

- export_material_groups ( bool ) – Export Material Groups, Form an OBJ group for each geometry segment with a distinct material (optional)

- export_vertex_groups ( bool ) – Export Vertex Groups, Write the vertex group name of a face. Approximated by choosing the vertex group with the most presence among the face's vertices (optional)

- export_smooth_groups ( bool ) – Export Smooth Groups, Make identifiers for each group of smooth faces as individual integer values (optional)

- smooth_group_bitflags ( bool ) – Bitflags Smooth Groups, When exporting smooth groups, use 'bitflags' values rather than unique integers. Distinct groups may share a bitflag if they have no mutual sharp edges or vertices (optional)

- filter_glob ( str ) – Extension Filter, (optional, never None)

- collection ( str ) – Collection, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
