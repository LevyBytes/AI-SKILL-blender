# bpy.ops.mesh.loop_select

bpy.ops.mesh. loop_select ( * , delimit_edge_loop = {'NGONS', '`OUTER_CORNERS`'} , delimit_face_loop = set() , extend = False , deselect = False , toggle = False , object_index = -1 , edge_index = -1 , vert_index = -1 , face_index = -1 )

Activate a strand of linked edges

Parameters :

- delimit_edge_loop (set[Literal[Mesh Walk Delimit Edge Loop Items]]) – Delimit, Delimit edge loop selection (optional)

- delimit_face_loop (set[Literal[Mesh Walk Delimit Face Loop Items]]) – Face Loop Delimit, Delimit face loop selection (optional)

- extend ( bool ) – Extend Select, Extend the selection (optional)

- deselect ( bool ) – Deselect, Remove from the selection (optional)

- toggle ( bool ) – Toggle Select, Toggle the selection (optional)

- object_index ( int ) – (in [-1, inf], optional)

- edge_index ( int ) – (in [-1, inf], optional)

- vert_index ( int ) – (in [-1, inf], optional)

- face_index ( int ) – (in [-1, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
