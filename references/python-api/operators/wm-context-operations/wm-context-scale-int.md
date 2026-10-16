# bpy.ops.wm.context_scale_int

bpy.ops.wm. context_scale_int ( * , data_path = '' , value = 1.0 , always_step = True ) 

Multiplies an int context variable

Parameters :

- data_path ( str ) - Context Attributes, Context parameter-trajectory (expanded using visible windows in the current .blend project) (optional, never None)

- value ( float ) - Value, Specifies the multiplier (in [-inf, inf], optional)

- always_step ( bool ) - Always Step, Guarantees modification by a minimum of 1 when 'value' is not 1.0 (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:376

[Related references](INDEX.md).
