# bpy.ops.uilist.entry_move

bpy.ops.uilist. entry_move ( * , list_path = '' , active_index_path = '' , direction = 'UP' ) 

Shifts a list entry upward or downward

Parameters :

- list_path ( str ) – list_path, (optional, never None)

- active_index_path ( str ) – active_index_path, (optional, never None)

- direction ( Literal [ 'UP' , 'DOWN' ] ) – Direction, (optional)

- UP
Up – Shift the active entry one slot higher.

- DOWN
Down – Shift the active entry one slot lower.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_ui/generic_ui_list.py:236

[Related references](INDEX.md).
