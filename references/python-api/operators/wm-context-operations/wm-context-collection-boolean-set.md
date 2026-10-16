# bpy.ops.wm.context_collection_boolean_set

bpy.ops.wm. context_collection_boolean_set ( * , data_path_iter = '' , data_path_item = '' , type = 'TOGGLE' ) 

Sets boolean parameters across multiple components

Parameters :

- data_path_iter ( str ) - data_path_iter, Context-relative trajectory, must reference an enumerable group (optional, never None)

- data_path_item ( str ) - data_path_item, Each item's parameter from the enumerable (int or float) (optional, never None)

- type ( Literal [ 'TOGGLE' , 'ENABLE' , 'DISABLE' ] ) - Type, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:875

[Related references](INDEX.md).
