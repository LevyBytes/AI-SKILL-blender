# bpy.ops.wm.context_cycle_array

bpy.ops.wm. context_cycle_array ( * , data_path = '' , reverse = False ) 

Establishes a context array variable (beneficial for alternating active mesh editing mode)

Parameters :

- data_path ( str ) - Context Attributes, Context parameter-trajectory (expanded using accessible windows in the current .blend project) (optional, never None)

- reverse ( bool ) - Reverse, Cycles forward (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:673

[Related references](INDEX.md).
