# bpy.ops.action.select_box

bpy.ops.action. select_box ( * , axis_range = False , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , mode = 'SET' , tweak = False )

Mark every keyframe within a rectangular region.

Parameters :

- axis_range ( bool ) – Axis Range, (optional)

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- mode ( Literal [ 'SET' , 'ADD' , 'SUB' ] ) – Mode, (optional)

- SET
Set – Establish a new selection.

- ADD
Extend – Enlarge the current selection.

- SUB
Subtract – Shrink the current selection.

- tweak ( bool ) – Tweak, Operator has been activated using a click-drag event (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
