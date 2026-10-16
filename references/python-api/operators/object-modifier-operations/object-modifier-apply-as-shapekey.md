# bpy.ops.object.modifier_apply_as_shapekey

bpy.ops.object. modifier_apply_as_shapekey ( * , keep_modifier = False , modifier = '' , report = False , use_selected_objects = False ) 

Finalize a modifier as a fresh shape key and take it off the stack

Parameters :

- keep_modifier ( bool ) – Keep Modifier, Preserve the modifier in the stack (optional)

- modifier ( str ) – Modifier, Name of the modifier to edit (optional, never None)

- report ( bool ) – Report, Issue a message window after the procedure finishes (optional)

- use_selected_objects ( bool ) – Selected Objects, Affect all selected objects instead of just the active object (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
