# bpy.types.WindowManager: modal_handler_add

classmethod modal_handler_add ( operator )

Add a modal handler to the window manager, for the given modal operator (called by invoke() with self, just before returning {'`RUNNING_MODAL`'})

Parameters :

operator (Operator) – Operator to call

Returns :

Whether adding the handler was successful

Return type :

bool

[Related references](INDEX.md).
