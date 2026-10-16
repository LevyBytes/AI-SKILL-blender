# bpy.types.Window: cursor_warp, cursor_set, cursor_modal_set, cursor_modal_restore

cursor_warp ( x , y )

Move the cursor to the given position

Parameters :

- x ( int ) – (in [-inf, inf])

- y ( int ) – (in [-inf, inf])
cursor_set ( cursor )

Set the cursor

Parameters :

cursor (Literal[Window Cursor Items]) – cursor
cursor_modal_set ( cursor )

Change the cursor while keeping the old one available to restore

Parameters :

cursor (Literal[Window Cursor Items]) – cursor
cursor_modal_restore ( )

Bring back the cursor that was in use before cursor_modal_set

[Related references](INDEX.md).
