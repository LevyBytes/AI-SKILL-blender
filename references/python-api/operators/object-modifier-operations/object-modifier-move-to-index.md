# bpy.ops.object.modifier_move_to_index

bpy.ops.object. modifier_move_to_index ( * , modifier = '' , index = 0 , use_selected_objects = False ) 

Set a modifier's sequence number so it processes after a specified number of other modifiers

Parameters :

- modifier ( str ) – Modifier, Name of the modifier to edit (optional, never None)

- index ( int ) – Index, The index to move the modifier to (in [0, inf], optional)

- use_selected_objects ( bool ) – Selected Objects, Affect all selected objects instead of just the active object (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
