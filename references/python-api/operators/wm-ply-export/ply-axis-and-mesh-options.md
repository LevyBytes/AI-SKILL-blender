# bpy.ops.wm.ply_export: up axis, mesh attributes and output

bpy.ops.wm. ply_export ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = False , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 8 , display_type = 'DEFAULT' , sort_method = '' , forward_axis = 'Y' , up_axis = 'Z' , global_scale = 1.0 , apply_modifiers = True , export_selected_objects = False , collection = '' , export_uv = True , export_normals = False , export_colors = 'SRGB' , export_attributes = True , export_triangulated_mesh = False , ascii_format = False , filter_glob = '*.ply' ) 

- up_axis ( Literal [ 'X' , 'Y' , 'Z' , '`NEGATIVE_X`' , '`NEGATIVE_Y`' , '`NEGATIVE_Z`' ] ) – Up Axis, (optional)

- X
X – Positive X axis.

- Y
Y – Positive Y axis.

- Z
Z – Positive Z axis.

- `NEGATIVE_X`
-X – Negative X axis.

- `NEGATIVE_Y`
-Y – Negative Y axis.

- `NEGATIVE_Z`
-Z – Negative Z axis.

- global_scale ( float ) – Scale, Adjusts object dimensions relative to the world's origin (in [0.0001, 10000], optional)

- apply_modifiers ( bool ) – Apply Modifiers, Execute modifiers on exported geometry (optional)

- export_selected_objects ( bool ) – Export Selected Objects, Restrict export to currently-selected objects only (optional)

- collection ( str ) – Source Collection, Write only objects from this collection and its children (optional, never None)

- export_uv ( bool ) – Export UVs, (optional)

- export_normals ( bool ) – Export Vertex Normals, Include calculated or pre-computed vertex normals (optional)

- export_colors ( Literal [ 'NONE' , 'SRGB' , 'LINEAR' ] ) – Export Vertex Colors, Output per-vertex color attributes (optional)

- NONE
None – Do not import/export color attributes.

- SRGB
sRGB – Vertex colors in the file are in sRGB color space.

- LINEAR
Linear – Vertex colors in the file are in linear color space.

- export_attributes ( bool ) – Export Vertex Attributes, Write user-defined vertex attributes (optional)

- export_triangulated_mesh ( bool ) – Export Triangulated Mesh, Converts all ngons of 4+ vertices to triangles. Meshes in the scene are unaffected. Works like Triangulate with ngon-method: "Beauty", quad-method: "Shortest Diagonal", min vertices: 4 (optional)

- ascii_format ( bool ) – ASCII Format, Output in text-based format; otherwise uses binary (optional)

- filter_glob ( str ) – Extension Filter, (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
