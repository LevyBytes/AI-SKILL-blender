# bpy.ops.object.vertex_group_smooth

bpy.ops.object. vertex_group_smooth ( * , group_select_mode = '' , factor = 0.5 , repeat = 1 , expand = 0.0 ) 

Smooth strength for picked vertices

Parameters :

- group_select_mode ( str ) – Subset, Identify which portion of clusters to employ (optional)

- factor ( float ) – Factor, (in [0, 1], optional)

- repeat ( int ) – Iterations, (in [1, 10000], optional)

- expand ( float ) – Expand/Contract, Broaden/reduce strength (in [-1, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
