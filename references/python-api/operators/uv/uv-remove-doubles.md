# bpy.ops.uv.remove_doubles

bpy.ops.uv. remove_doubles ( * , threshold = 0.02 , use_unselected = False , use_shared_vertex = False ) 

Merges together selected UV vertices that sit within a set radius of one another

Parameters :

- threshold ( float ) – Merge Distance, Maximum distance between welded vertices (in [0, 10], optional)

- use_unselected ( bool ) – Unselected, Merge selected to other unselected vertices (optional)

- use_shared_vertex ( bool ) – Shared Vertex, Weld UVs based on shared vertices (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
