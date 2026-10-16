# bpy.types.WindowManager: draw_cursor_add, draw_cursor_remove

classmethod draw_cursor_add ( callback , args , space_type , region_type )

Register a new draw-cursor handler on this space type.
It runs each time the cursor is drawn for the named region within the space type.
Note: for the time being every argument is positional only.

Parameters :

- callback ( Callable [ ... , Any ] ) – The function invoked while the cursor is being drawn.
It receives the supplied arguments, with the mouse position ( tuple[int, int] ) handed in as the final one.

- args ( tuple [ Any , ... ] ) – The arguments forwarded into the callback.

- space_type ( str ) – The space type the callback draws in; for example `VIEW_3D` . (bpy.types.Space.type)

- region_type ( str ) – The region type the callback draws in; usually WINDOW . (bpy.types.Region.type)

Returns :

A handler you can remove afterward.

Return type :

object
classmethod draw_cursor_remove ( handler )

Take off a draw-cursor handler that was registered earlier.

Parameters :

handler ( object ) – The draw cursor handler that should be removed.

[Related references](INDEX.md).
