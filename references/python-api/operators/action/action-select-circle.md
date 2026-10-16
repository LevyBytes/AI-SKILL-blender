# bpy.ops.action.select_circle

bpy.ops.action. select_circle ( * , x = 0 , y = 0 , radius = 25 , wait_for_input = True , mode = 'SET' )

Pick keyframe points via circular lasso.

Parameters :

- x ( int ) – X, (in [-inf, inf], optional)

- y ( int ) – Y, (in [-inf, inf], optional)

- radius ( int ) – Radius, (in [1, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Establish a new selection.

- ADD
Extend – Enlarge the current selection.

- SUB
Subtract – Shrink the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
