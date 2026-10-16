# bpy.ops.preferences.keyitem_restore

bpy.ops.preferences. keyitem_restore ( * , item_id = 0 ) 

Bring back a keybinding entry

Parameters :

item_id ( int ) – Item Identifier, Identifier of the item to restore (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:395
bpy.ops.preferences. keyitem_restore ( * , item_id = 0 )
Restores a key map item.
Parameters: item_id ( int ) – Item Identifier, Identifier of the item to restore (in [-inf, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:395

[Related references](INDEX.md).
