# bpy.ops.sequencer.strip_modifier_move_to_index

bpy.ops.sequencer.strip_modifier_move_to_index(*, modifier='', index=0)

Modify the piece modifier's rank in the compilation so it computes following the configured number of others.

Parameters:

- modifier (str) – Modifier, Name of the modifier to manage (optional, never None)
- index (int) – Index, The rank to move the modifier to (in [0, inf], optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.strip_modifier_move_to_index(*, modifier='', index=0)

Modify the piece modifier's rank in the compilation so it computes following the configured number of others.

Parameters:

- modifier (str) – Modifier, Name of the modifier to manage (optional, never None)
- index (int) – Index, The rank to move the modifier to (in [0, inf], optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer. strip_modifier_move_to_index ( * , modifier = '' , index = 0 ) 

Reposition the strip modifier within the stack so it is evaluated after the chosen number of others

Parameters :

- modifier ( str ) – Modifier, The modifier to edit, by name (optional, never None)

- index ( int ) – Index, Where in the stack to move the modifier (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
