# bpy.types.Mesh: calc_tangents, calc_loop_triangles, calc_smooth_groups

calc_tangents ( * , uvmap = '' )

Work out the tangents and bitangent signs so that, paired with the custom normals, you have a full tangent space for normal mapping (any missing custom normals get computed too)

Parameters :

uvmap ( str ) – Name of the UV map to use for tangent space computation (optional, never None)
calc_loop_triangles ( )

Build the loop-triangle tessellation (works in editmode as well)
calc_smooth_groups ( * , use_bitflags = False , use_boundary_vertices_for_bitflags = False )

Derive smooth groups out of the sharp edges

Parameters :

- use_bitflags ( bool ) – Produce bitflags groups instead of simple numeric values (optional)

- use_boundary_vertices_for_bitflags ( bool ) – Also consider different smoothgroups sharing only vertices (but without any common edge) as neighbors, preventing them from sharing the same bitflag value. Only effective when use_bitflags is set. WARNING: Will overflow (run out of available bits) easily with some types of topology, e.g. large fans of sharp edges (optional)

Returns :

poly_groups , Smooth Groups, bpy_prop_array[int]

groups , Total number of groups, int

Return type :

tuple[bpy_prop_array[int], int]

[Related references](INDEX.md).
