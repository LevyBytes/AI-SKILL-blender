# bpy.ops.mask.select_box

bpy.ops.mask. select_box ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' )

Select curve points using box selection

Parameters :

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

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
