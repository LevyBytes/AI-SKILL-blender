# bpy.ops.view3d.select

bpy.ops.view3d. select ( * , extend = False , deselect = False , toggle = False , deselect_all = False , select_passthrough = False , center = False , enumerate = False , object = False , location = (0, 0) ) 

Highlight and make current specific item(s)

Parameters :

- extend ( bool ) - Extend, Adds to the current selection rather than clearing it beforehand (optional)

- deselect ( bool ) - Deselect, Removes from the current selection (optional)

- toggle ( bool ) - Toggle Selection, Reverses the selection state (optional)

- deselect_all ( bool ) - Deselect On Nothing, Clears all selection when the cursor points to empty space (optional)

- select_passthrough ( bool ) - Only Select Unselected, Ignores the choose action when the element is already highlighted (optional)

- center ( bool ) - Center, Uses the object's midpoint when choosing, in edit mode used to expand object selection (optional)

- enumerate ( bool ) - Enumerate, Displays items beneath the cursor (object mode only) (optional)

- object ( bool ) - Object, Uses object selection (edit mode only) (optional)

- location ( Sequence [ int ] ) - Location, Cursor position (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
