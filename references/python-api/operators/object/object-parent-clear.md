# bpy.ops.object.parent_clear

bpy.ops.object. parent_clear ( * , type = 'CLEAR' ) 

Sever the object's parent connection

Parameters :

type ( Literal [ 'CLEAR' , '`CLEAR_KEEP_TRANSFORM`' , '`CLEAR_INVERSE`' ] ) – Type, (optional)

- CLEAR
Clear Parent – Fully remove the parent link and any tied constraints.

- `CLEAR_KEEP_TRANSFORM`
Clear and Keep Transformation – Sever the parent link while holding the current visual position.

- `CLEAR_INVERSE`
Clear Parent Inverse – Erase the transform offset built into the parent link without breaking the connection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
