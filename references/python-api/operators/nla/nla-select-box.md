# bpy.ops.nla.select_box

bpy.ops.nla. select_box ( * , axis_range = False , tweak = False , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' ) 

Grab NLA-Sections by dragging a frame

Parameters :

- axis_range ( bool ) – Axis Range, (optional)

- tweak ( bool ) – Tweak, The tool began via a point-drag occurrence (optional)

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Create a fresh choice.

- ADD
Extend – Grow the active marking.

- SUB
Subtract – Reduce the active marking.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
