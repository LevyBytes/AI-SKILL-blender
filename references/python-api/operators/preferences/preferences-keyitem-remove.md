# bpy.ops.preferences.keyitem_remove

bpy.ops.preferences. keyitem_remove ( * , item_id = 0 ) 

Erase a keybinding entry

Parameters :

item_id ( int ) – Item Identifier, Identifier of the item to remove (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/userpref.py:443
bpy.ops.preferences. keyitem_remove ( * , item_id = 0 )
Removes a key map item.
Parameters: item_id ( int ) – Item Identifier, Identifier of the item to remove (in [-inf, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]
File: startup/bl_operators/userpref.py:443

[Related references](INDEX.md).
