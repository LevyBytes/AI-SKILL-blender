# bpy.ops.node.group_separate

bpy.ops.node. group_separate ( * , type = 'COPY' ) 

Disconnect currently highlighted nodes from the node group

Parameters :

type ( Literal [ 'COPY' , 'MOVE' ] ) – Type, (optional)

- COPY
Copy – Duplicate to parent node tree, keep group intact.

- MOVE
Move – Shift to parent node tree, remove from group.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
