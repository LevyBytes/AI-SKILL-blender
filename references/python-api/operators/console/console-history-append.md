# bpy.ops.console.history_append

bpy.ops.console. history_append ( * , text = '' , current_character = 0 , remove_duplicates = False )

Append history at cursor position

Parameters :

- text ( str ) – Text, Text to insert at the cursor position (optional, never None)

- current_character ( int ) – Cursor, The index of the cursor (in [0, inf], optional)

- remove_duplicates ( bool ) – Remove Duplicates, Remove duplicate items in the history (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
