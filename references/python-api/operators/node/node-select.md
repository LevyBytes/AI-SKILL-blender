# bpy.ops.node.select

bpy.ops.node. select ( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , location = (0, 0) , socket_select = False , clear_viewer = False ) 

Pick the node underneath the cursor position

Parameters :

- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)

- deselect ( bool ) – Deselect, Remove from selection (optional)

- toggle ( bool ) – Toggle Selection, Toggle the selection (optional)

- deselect_all ( bool ) – Deselect On Nothing, Deselect all when nothing under the cursor (optional)

- select_passthrough ( bool ) – Only Select Unselected, Ignore the select action when the element is already selected (optional)

- location ( Sequence [ int ] ) – Location, Mouse location (array of 2 items, in [-inf, inf], optional)

- socket_select ( bool ) – Socket Select, (optional)

- clear_viewer ( bool ) – Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
