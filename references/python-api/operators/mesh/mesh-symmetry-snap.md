# bpy.ops.mesh.symmetry_snap

bpy.ops.mesh. symmetry_snap ( * , direction = '`NEGATIVE_X`' , threshold = 0.05 , factor = 0.5 , use_center = True ) 

Align point groups to their reflected spots

Parameters :

- direction (Literal[Symmetrize Direction Items]) – Direction, What to replicate from and to (optional)

- threshold ( float ) – Threshold, Range for finding matching points (in [0, 10], optional)

- factor ( float ) – Factor, Balance between the placements of the points (in [0, 1], optional)

- use_center ( bool ) – Center, Align middle points to the center line (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
