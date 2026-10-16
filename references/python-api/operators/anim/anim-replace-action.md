# bpy.ops.anim.replace_action

bpy.ops.anim. replace_action ( * , old_session_uid = 0 , new_session_uid = 0 )

Reroute all references from one action to another. Standard action slot policies govern behavior. NLA and Action Constraints are bypassed.

Parameters :

- old_session_uid ( int ) – Old Action, Old Action's session uid to replace (in [-inf, inf], optional)

- new_session_uid ( int ) – Replacement Action, The replacement Action's session uid to remap all selected Action's users to (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
