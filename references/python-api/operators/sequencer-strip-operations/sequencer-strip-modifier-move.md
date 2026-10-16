# bpy.ops.sequencer.strip_modifier_move

bpy.ops.sequencer.strip_modifier_move(*, name='Name', direction='UP')

Reposition modifier within the compilation.

Parameters:

- name (str) – Name, Name of modifier to discard (optional, never None)
- direction (Literal['UP', 'DOWN']) – Type, (optional)
  - UP
    Up – Reposition modifier upward in the compilation.
  - DOWN
    Down – Reposition modifier downward in the compilation.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.strip_modifier_move(*, name='Name', direction='UP')

Reposition modifier within the compilation.

Parameters:

- name (str) – Name, Name of modifier to discard (optional, never None)
- direction (Literal['UP', 'DOWN']) – Type, (optional)
  - UP
    Up – Reposition modifier upward in the compilation.
  - DOWN
    Down – Reposition modifier downward in the compilation.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer. strip_modifier_move ( * , name = 'Name' , direction = 'UP' ) 

Shift a modifier up or down within the stack

Parameters :

- name ( str ) – Name, The modifier to act on, by name (optional, never None)

- direction ( Literal [ 'UP' , 'DOWN' ] ) – Type, (optional)

- UP
Up – Move the modifier one place up the stack.

- DOWN
Down – Move the modifier one place down the stack.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
