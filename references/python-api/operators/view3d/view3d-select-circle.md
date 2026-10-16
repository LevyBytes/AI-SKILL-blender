# bpy.ops.view3d.select_circle

bpy.ops.view3d. select_circle ( * , x = 0 , y = 0 , radius = 25 , wait_for_input = True , mode = 'SET' ) 

Highlight elements via circular selection

Parameters :

- x ( int ) - X, (in [-inf, inf], optional)

- y ( int ) - Y, (in [-inf, inf], optional)

- radius ( int ) - Radius, (in [1, inf], optional)

- wait_for_input ( bool ) - Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) - Mode, (optional)

- SET
Set - Establishes a new selection.

- ADD
Extend - Expands the current selection.

- SUB
Subtract - Removes from the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
