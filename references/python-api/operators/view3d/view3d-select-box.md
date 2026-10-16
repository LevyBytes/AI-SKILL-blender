# bpy.ops.view3d.select_box

bpy.ops.view3d. select_box ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' ) 

Highlight elements via rectangular selection

Parameters :

- xmin ( int ) - X Min, (in [-inf, inf], optional)

- xmax ( int ) - X Max, (in [-inf, inf], optional)

- ymin ( int ) - Y Min, (in [-inf, inf], optional)

- ymax ( int ) - Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) - Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' , 'XOR' , 'AND' ] ) - Mode, (optional)

- SET
Set - Establishes a new selection.

- ADD
Extend - Expands the current selection.

- SUB
Subtract - Removes from the current selection.

- XOR
Difference - Reverses the selection state.

- AND
Intersect - Keeps only overlapping selections.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
