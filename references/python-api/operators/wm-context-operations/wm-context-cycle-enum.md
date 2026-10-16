# bpy.ops.wm.context_cycle_enum

bpy.ops.wm. context_cycle_enum ( * , data_path = '' , reverse = False , wrap = False )
Toggle a context value

Parameters :

- data_path ( str ) - Context Attributes, Context parameter-trajectory (expanded using accessible windows in the current .blend project) (optional, never None)

- reverse ( bool ) - Reverse, Cycles forward (optional)

- wrap ( bool ) - Wrap, Returns to the start/end settings (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:624

[Related references](INDEX.md).
