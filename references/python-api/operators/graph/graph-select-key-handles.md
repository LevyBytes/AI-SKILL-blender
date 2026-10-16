# bpy.ops.graph.select_key_handles

bpy.ops.graph.select_key_handles(*, left_handle_action='SELECT', right_handle_action='SELECT', key_action='KEEP')

For the chose frames, mark/unmark every mix of the component itself and its grips

Parameters:

- left_handle_action (Literal['SELECT', 'DESELECT', 'KEEP']) – Left Handle, Consequence on the left grip (optional)

- SELECT
Select.

- DESELECT
Deselect.

- KEEP
Keep – Leave as is.

- right_handle_action (Literal['SELECT', 'DESELECT', 'KEEP']) – Right Handle, Consequence on the right grip (optional)

- SELECT
Select.

- DESELECT
Deselect.

- KEEP
Keep – Leave as is.

- key_action (Literal['SELECT', 'DESELECT', 'KEEP']) – Key, Consequence on the component itself (optional)

- SELECT
Select.

- DESELECT
Deselect.

- KEEP
Keep – Leave as is.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
