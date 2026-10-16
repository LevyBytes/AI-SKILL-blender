# bpy.ops.mask.select_circle

bpy.ops.mask. select_circle ( * , x = 0 , y = 0 , radius = 25 , wait_for_input = True , mode = 'SET' )

Select curve points using circle selection

Parameters :

- x ( int ) – X, (in [-inf, inf], optional)

- y ( int ) – Y, (in [-inf, inf], optional)

- radius ( int ) – Radius, (in [1, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Start a fresh selection.

- ADD
Extend – Add to the current selection.

- SUB
Subtract – Remove from the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
