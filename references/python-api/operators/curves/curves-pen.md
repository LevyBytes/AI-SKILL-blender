# bpy.ops.curves.pen

**bpy.ops.curves.pen**( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , extrude_point = False , extrude_handle = 'VECTOR' , delete_point = False , insert_point = False , move_segment = False , select_point = False , move_point = False , cycle_handle_type = False , size = 0.01 )

Create and modify Bézier curves using the Pen tool.

Parameters:
- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)
- deselect ( bool ) – Deselect, Remove from selection (optional)
- toggle ( bool ) – Toggle Selection, Toggle the selection (optional)
- deselect_all ( bool ) – Deselect On Nothing, Deselect all when nothing under the cursor (optional)
- select_passthrough ( bool ) – Only Select Unselected, Ignore the select action when the element is already selected (optional)
- extrude_point ( bool ) – Extrude Point, Add a point connected to the last selected point (optional)
- extrude_handle ( Literal [ 'AUTO' , 'VECTOR' ] ) – Extrude Handle Type, Type of the extruded handle (optional)
- delete_point ( bool ) – Delete Point, Delete an existing point (optional)
- insert_point ( bool ) – Insert Point, Insert Point into a curve segment (optional)
- move_segment ( bool ) – Move Segment, Move an existing curve segment (optional)
- select_point ( bool ) – Select Point, Select a point or its handles (optional)
- move_point ( bool ) – Move Point, Move a point or its handles (optional)
- cycle_handle_type ( bool ) – Cycle Handle Type, Cycle between all four handle types (optional)
- size ( float ) – Size, Diameter of new points (in [0, inf], optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
