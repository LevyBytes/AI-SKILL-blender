# bpy.ops.clip.frame_jump

bpy.ops.clip. frame_jump ( * , position = 'PATHSTART' )

Go to a special frame location

Parameters :

position ( Literal [ 'PATHSTART' , 'PATHEND' , 'FAILEDPREV' , 'FAILNEXT' ] ) – Position, Position to jump to (optional)

- PATHSTART
Path Start – Jump to start of current path.

- PATHEND
Path End – Jump to end of current path.

- FAILEDPREV
Previous Failed – Jump to previous failed frame.

- FAILNEXT
Next Failed – Jump to next failed frame.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
