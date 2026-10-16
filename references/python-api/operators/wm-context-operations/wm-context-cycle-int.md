# bpy.ops.wm.context_cycle_int

bpy.ops.wm. context_cycle_int ( * , data_path = '' , reverse = False , wrap = False ) 

Establishes a context variable (beneficial for cycling active material, vertex groups, collections, etc.)

Parameters :

- data_path ( str ) - Context Attributes, Context parameter-trajectory (expanded using accessible windows in the current .blend project) (optional, never None)

- reverse ( bool ) - Reverse, Cycles forward (optional)

- wrap ( bool ) - Wrap, Returns to the start/end settings (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:584

[Related references](INDEX.md).
