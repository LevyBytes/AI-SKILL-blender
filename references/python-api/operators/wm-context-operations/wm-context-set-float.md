# bpy.ops.wm.context_set_float

bpy.ops.wm. context_set_float ( * , data_path = '' , value = 0.0 , relative = False ) 

Assigns a context variable

Parameters :

- data_path ( str ) - Context Attributes, Context parameter-trajectory (expanded using visible windows in the current .blend project) (optional, never None)

- value ( float ) - Value, Intended value (in [-inf, inf], optional)

- relative ( bool ) - Relative, Adds to the current variable (delta) (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:267

[Related references](INDEX.md).
