# bpy.ops.uv.select

bpy.ops.uv. select ( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , location = (0.0, 0.0) ) 

Selects UV vertices

Parameters :

- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)

- deselect ( bool ) – Deselect, Remove from selection (optional)

- toggle ( bool ) – Toggle Selection, Toggle the selection (optional)

- deselect_all ( bool ) – Deselect On Nothing, Deselect all when nothing under the cursor (optional)

- select_passthrough ( bool ) – Only Select Unselected, Ignore the select action when the element is already selected (optional)

- location (mathutils.Vector) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
