# bpy.ops.uv.select_box

bpy.ops.uv. select_box ( * , pinned = False , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' ) 

Selects UV vertices by dragging a box

Parameters :

- pinned ( bool ) – Pinned, Border select pinned UVs only (optional)

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Begin a brand-new selection.

- ADD
Extend – Grow the current selection.

- SUB
Subtract – Shrink the current selection.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
