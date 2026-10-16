# bpy.ops.node.select_box

bpy.ops.node. select_box ( * , tweak = False , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' ) 

Employ rectangular capture to highlight nodes

Parameters :

- tweak ( bool ) – Tweak, Only activate when mouse is not over a node (useful for tweak gesture) (optional)

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

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
