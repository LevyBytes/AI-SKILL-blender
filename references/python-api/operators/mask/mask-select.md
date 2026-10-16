# bpy.ops.mask.select

bpy.ops.mask. select ( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , location = (0.0, 0.0) )

Select spline points

Parameters :

- extend ( bool ) – Extend, Add to the selection rather than clearing it first (optional)

- deselect ( bool ) – Deselect, Take out of the selection (optional)

- toggle ( bool ) – Toggle Selection, Flip the selection state (optional)

- deselect_all ( bool ) – Deselect On Nothing, Clear the selection when nothing sits under the cursor (optional)

- select_passthrough ( bool ) – Only Select Unselected, Skip the select action when the element is already selected (optional)

- location (mathutils.Vector) – Location, Vertex position in normalized space (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
