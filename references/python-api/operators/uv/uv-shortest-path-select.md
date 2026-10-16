# bpy.ops.uv.shortest_path_select

bpy.ops.uv. shortest_path_select ( * , use_face_step = False , use_topology_distance = False , use_fill = False , skip = 0 , nth = 1 , offset = 0 ) 

Selects the shortest route linking two vertices, edges, or faces

Parameters :

- use_face_step ( bool ) – Face Stepping, Traverse connected faces (includes diagonals and edge-rings) (optional)

- use_topology_distance ( bool ) – Topology Distance, Find the minimum number of steps, ignoring spatial distance (optional)

- use_fill ( bool ) – Fill Region, Select all paths between the source/destination elements (optional)

- skip ( int ) – Deselected, Number of deselected elements in the repetitive sequence (in [0, inf], optional)

- nth ( int ) – Selected, Number of selected elements in the repetitive sequence (in [1, inf], optional)

- offset ( int ) – Offset, Offset from the starting point (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
