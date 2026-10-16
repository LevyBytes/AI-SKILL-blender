# bpy.ops.clip.select_circle

bpy.ops.clip. select_circle ( * , x = 0 , y = 0 , radius = 25 , wait_for_input = True , mode = 'SET' )

Pick markers via circular selection

Parameters :

- x ( int ) – X, (in [-inf, inf], optional)

- y ( int ) – Y, (in [-inf, inf], optional)

- radius ( int ) – Radius, (in [1, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Set a new selection.

- ADD
Extend – Extend existing selection.

- SUB
Subtract – Subtract existing selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
