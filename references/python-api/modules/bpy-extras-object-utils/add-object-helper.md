# bpy_extras.object_utils.AddObjectHelper

class bpy_extras.object_utils. AddObjectHelper
align_update_callback ( _context ) 

Update callback for the align property; it clears rotation when world alignment is chosen.
classmethod poll ( context ) 

Confirm the scene isn't linked in from a library.

Parameters :

context (bpy.types.Context) – The context.

Returns :

True when the scene is local (not linked from a library).

Return type :

bool

[Related references](INDEX.md).
