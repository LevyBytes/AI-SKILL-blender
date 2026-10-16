# bpy.types.Object: to_mesh, to_mesh_clear, to_curve, to_curve_clear

to_mesh ( * , preserve_all_data_layers = False , depsgraph = None ) 

Build a Mesh data-block from the object's present state. The data-block stays owned by the object; call to_mesh_clear() to free it manually. What you get is temporary and may not be attached to objects in the main database.

Parameters :

- preserve_all_data_layers ( bool ) – Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)

- depsgraph (Depsgraph) – Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)

Returns :

Mesh created from object

Return type :

Mesh
to_mesh_clear ( ) 

Discard the mesh data-block that to_mesh() produced
to_curve ( depsgraph , * , apply_modifiers = False ) 

Build a Curve data-block from the object's present state. Only curve and text objects qualify. The data-block stays owned by the object; call to_curve_clear() to free it manually. What you get is temporary and may not be attached to objects in the main database.

Parameters :

- depsgraph (Depsgraph) – Dependency Graph, Evaluated dependency graph

- apply_modifiers ( bool ) – Apply the deform modifiers on the control points of the curve. This is only supported for curve objects. (optional)

Returns :

Curve created from object

Return type :

Curve
to_curve_clear ( ) 

Discard the curve data-block that to_curve() produced

[Related references](INDEX.md).
