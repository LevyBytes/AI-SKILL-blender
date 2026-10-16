# bpy.ops.curve.pen

**bpy.ops.curve.pen**( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , extrude_point = False , extrude_handle = 'VECTOR' , delete_point = False , insert_point = False , move_segment = False , select_point = False , move_point = False , close_spline = True , close_spline_method = 'OFF' , toggle_vector = False , cycle_handle_type = False )

Create and modify curves using the Pen tool.

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
- close_spline ( bool ) – Close Spline, Make a spline cyclic by clicking endpoints (optional)
- close_spline_method ( Literal [ 'OFF' , '`ON_PRESS`' , '`ON_CLICK`' ] ) – Close Spline Method, The condition for close spline to activate (optional)

- OFF
None.

- `ON_PRESS`
On Press – Move handles after closing the spline.

- `ON_CLICK`
On Click – Spline closes on release if not dragged.

- toggle_vector ( bool ) – Toggle Vector, Toggle between Vector and Auto handles (optional)
- cycle_handle_type ( bool ) – Cycle Handle Type, Cycle between all four handle types (optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
