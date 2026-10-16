# bpy.ops.object.vertex_group_lock

bpy.ops.object. vertex_group_lock ( * , action = 'TOGGLE' , mask = 'ALL' ) 

Flip the secure condition of entire or partial vertex clusters of working item

Parameters :

- action ( Literal [ 'TOGGLE' , 'LOCK' , 'UNLOCK' , 'INVERT' ] ) – Action, Secure action to perform on vertex clusters (optional)

- TOGGLE
Toggle – Unprotect each vertex cluster when minimum one is protected, otherwise safeguard each.

- LOCK
Lock – Protect each vertex cluster.

- UNLOCK
Unlock – Unprotect each vertex cluster.

- INVERT
Invert – Reverse the secure status of each vertex cluster.

- mask ( Literal [ 'ALL' , 'SELECTED' , 'UNSELECTED' , '`INVERT_UNSELECTED`' ] ) – Mask, Execute the action according to vertex cluster choice (optional)

- ALL
All – Run action on entire vertex clusters.

- SELECTED
Selected – Run on chosen vertex clusters.

- UNSELECTED
Unselected – Run on non-chosen vertex clusters.

- `INVERT_UNSELECTED`
Invert Unselected – Run the reverse of Secure/Unprotect to non-chosen vertex clusters.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
