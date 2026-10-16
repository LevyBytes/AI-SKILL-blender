# bpy_extras.anim_utils.AutoKeying: classmethod active_keyingset ( context )

classmethod active_keyingset ( context ) 

Give back the active keying set when it ought to be used.

The active keying set is only returned when the auto-key settings call for it,
and when it avoids absolute paths (since
the Copy Global Transform add-on doesn't support those).

Parameters :

context (bpy.types.Context) – The context.

Returns :

The active keying set, or None when it should not be used.

Return type :

bpy.types.KeyingSet | None

[Related references](INDEX.md).
