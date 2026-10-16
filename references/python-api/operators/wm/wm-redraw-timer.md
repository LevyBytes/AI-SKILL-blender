# bpy.ops.wm.redraw_timer

bpy.ops.wm. redraw_timer ( * , type = 'DRAW' , iterations = 10 , time_limit = 0.0 ) 

Executes a simple redraw timer to measure interface refresh velocity

Parameters :

- type ( Literal [ 'DRAW' , '`DRAW_SWAP`' , '`DRAW_WIN`' , '`DRAW_WIN_SWAP`' , '`ANIM_STEP`' , '`ANIM_PLAY`' , 'UNDO' ] ) – Type, (optional)

- DRAW
Draw Region – Draw region.

- `DRAW_SWAP`
Draw Region & Swap – Draw region and swap.

- `DRAW_WIN`
Draw Window – Draw window.

- `DRAW_WIN_SWAP`
Draw Window & Swap – Draw window and swap.

- `ANIM_STEP`
Animation Step – Animation steps.

- `ANIM_PLAY`
Animation Play – Animation playback.

- UNDO
Undo/Redo – Undo and redo.

- iterations ( int ) – Iterations, How many times to redraw (in [1, inf], optional)

- time_limit ( float ) – Time Limit, Duration to run the test for (replaces iterations) (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
