# bpy.ops.grease_pencil.pen

bpy.ops.grease_pencil.pen ( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , extrude_point = False , extrude_handle = 'VECTOR' , delete_point = False , insert_point = False , move_segment = False , select_point = False , move_point = False , cycle_handle_type = False , size = 0.01 )
Draw and modify bezier curves

Parameters:
- extend ( bool ) – Extend, Accumulate selection rather than replacing existing selection (optional)
- deselect ( bool ) – Deselect, Withdraw from selection (optional)
- toggle ( bool ) – Toggle Selection, Reverse the selection status (optional)
- deselect_all ( bool ) – Deselect On Nothing, Clear all selection when the cursor is empty (optional)
- select_passthrough ( bool ) – Only Select Unselected, Skip selection action when element is already highlighted (optional)
- extrude_point ( bool ) – Extrude Point, Create a new point extending from the last selected one (optional)
- extrude_handle ( Literal [ 'AUTO' , 'VECTOR' ] ) – Extrude Handle Type, Behavior for the new handle (optional)
- delete_point ( bool ) – Delete Point, Discard an existing control point (optional)
- insert_point ( bool ) – Insert Point, Embed a point within a curve segment (optional)
- move_segment ( bool ) – Move Segment, Relocate an existing curve segment (optional)
- select_point ( bool ) – Select Point, Highlight a point or its handles (optional)
- move_point ( bool ) – Move Point, Reposition a point or its handles (optional)
- cycle_handle_type ( bool ) – Cycle Handle Type, Rotate through all four handle modes (optional)
- size ( float ) – Size, Diameter of new points (in [0, inf], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
