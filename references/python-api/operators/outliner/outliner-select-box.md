# bpy.ops.outliner.select_box

bpy.ops.outliner. select_box ( * , tweak = False , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' ) 

Employ rectangle choosing to opt for arrangement components

Parameters :

- tweak ( bool ) – Tweak, Tweak motion from unoccupied room for rectangle choosing (optional)

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Put a refreshed choosing.

- ADD
Extend – Broaden persisting choosing.

- SUB
Subtract – Deduct persisting choosing.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
