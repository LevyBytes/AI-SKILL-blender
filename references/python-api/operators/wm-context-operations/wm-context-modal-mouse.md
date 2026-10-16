# bpy.ops.wm.context_modal_mouse

bpy.ops.wm. context_modal_mouse ( * , data_path_iter = '' , data_path_item = '' , header_text = '' , input_scale = 0.01 , invert = False , initial_x = 0 ) 

Modifies arbitrary parameters via mouse interaction

Parameters :

- data_path_iter ( str ) - data_path_iter, Context-relative trajectory, must reference an enumerable group (optional, never None)

- data_path_item ( str ) - data_path_item, Each item's parameter from the enumerable (int or float) (optional, never None)

- header_text ( str ) - Header Text, Display text exhibited in the header during adjustment (optional, never None)

- input_scale ( float ) - input_scale, Multiplier for cursor movement before calculating the adjustment (in [-inf, inf], optional)

- invert ( bool ) - invert, Reverses the mouse motion (optional)

- initial_x ( int ) - initial_x, (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:1014

[Related references](INDEX.md).
