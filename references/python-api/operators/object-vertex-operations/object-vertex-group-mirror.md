# bpy.ops.object.vertex_group_mirror

bpy.ops.object. vertex_group_mirror ( * , mirror_weights = True , flip_group_names = True , all_groups = False , use_topology = False ) 

Duplicate vertex cluster, reverse strength and/or names, updating merely chosen vertices, reversing when both edges are chosen or else take from non-chosen

Parameters :

- mirror_weights ( bool ) – Mirror Weights, Duplicate strength (optional)

- flip_group_names ( bool ) – Flip Group Names, Reverse vertex cluster names (optional)

- all_groups ( bool ) – All Groups, Duplicate each vertex cluster strength (optional)

- use_topology ( bool ) – Topology Mirror, Use structural duplication (for when both edges of geometry contain matching, exclusive structure) (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
