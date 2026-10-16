# bpy.ops.file.unpack_item

bpy.ops.file.unpack_item(*, method='`USE_LOCAL`', id_name='', id_type=19785)

Retrieve this document to a standalone type

Parameters:

- method (Literal['`USE_LOCAL`', '`WRITE_LOCAL`', '`USE_ORIGINAL`', '`WRITE_ORIGINAL`']) – Method, How to retrieve (optional)
- id_name (str) – ID Name, Label of the information block to retrieve (optional, never None)
- id_type (int) – ID Type, Code type of the information block (in [0, inf], optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
