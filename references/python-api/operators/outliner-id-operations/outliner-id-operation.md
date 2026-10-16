# bpy.ops.outliner.id_operation

bpy.ops.outliner. id_operation ( * , type = 'UNLINK' ) 

Standard information-block handling operations

Parameters :

type ( Literal [ 'UNLINK' , 'LOCAL' , 'SINGLE' , 'DELETE' , 'REMAP' , 'COPY' , 'PASTE' , '`ADD_FAKE`' , '`CLEAR_FAKE`' , 'RENAME' , '`SELECT_LINKED`' ] ) – ID Data Operation, (optional)

- UNLINK
Unlink.

- LOCAL
Make Local.

- SINGLE
Make Single User.

- DELETE
Delete.

- REMAP
Remap Users – Redirect every holders of chosen information-blocks to employ the alternative (tapped) unit.

- COPY
Copy.

- PASTE
Paste.

- `ADD_FAKE`
Add Fake User – Safeguard information-block acquires kept regardless if it's inactive (e.g. for movement and fabric reserves).

- `CLEAR_FAKE`
Clear Fake User.

- RENAME
Rename.

- `SELECT_LINKED`
Select Linked.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
