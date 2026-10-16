# bpy.ops.mesh.shortest_path_pick

bpy.ops.mesh. shortest_path_pick ( * , edge_mode = 'SELECT' , use_face_step = False , use_topology_distance = False , use_fill = False , skip = 0 , nth = 1 , offset = 0 , index = -1 ) 

Highlight the quickest chain connecting two marked spots

Parameters :

- edge_mode ( Literal [ 'SELECT' , 'SEAM' , 'SHARP' , 'CREASE' , 'BEVEL' , 'FREESTYLE' ] ) – Edge Tag, The mark to apply when highlighting the quickest chain (optional)

- use_face_step ( bool ) – Face Stepping, Go through attached surfaces (takes diagonals and sequences into account) (optional)

- use_topology_distance ( bool ) – Topology Distance, Get the least steps ignoring how far apart in room they are (optional)

- use_fill ( bool ) – Fill Region, Highlight every chain from start to finish (optional)

- skip ( int ) – Deselected, How many unmarked parts per cycle (in [0, inf], optional)

- nth ( int ) – Selected, How many marked parts per cycle (in [1, inf], optional)

- offset ( int ) – Offset, Starting point shift (in [-inf, inf], optional)

- index ( int ) – (in [-1, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
