# bpy.ops.clip.graph_select_box

bpy.ops.clip. graph_select_box ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , deselect = False , extend = True )

Choose curve vertices via rectangular selection

Parameters :

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- deselect ( bool ) – Deselect, Deselect rather than select items (optional)

- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
