# bpy.types.AnimData: methods

nla_tweak_strip_time_to_scene(frame, *, invert=False)

Translate a time from the tweaked strip's local time to scene time, exactly like built-in key editing tools. Leaves time unchanged if not in tweak mode.

Parameters:

- frame (float) – Input time ([-1.04857e+06, 1.04857e+06])

- invert (bool) – Invert, Translate scene time to action time (optional)

Returns: Translated time ([-1.04857e+06, 1.04857e+06])

Return type: float
fix_paths_rename_all(*, prefix='', old_name='', new_name='')

Update the property paths in the animation system, since properties are animated through string paths, updates are necessary to keep them valid after properties are renamed

Parameters:

- prefix (str) – Prefix, Name prefix (optional, never None)

- old_name (str) – Old Name, Old name (optional, never None)

- new_name (str) – New Name, New name (optional, never None)
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:

- id (str) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns: The RNA type or default when not found.

Return type: bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:

- id (str) – The RNA type identifier.

- default (type | None) – The value to return when not found.

Returns: The class or default when not found.

Return type: type

[Related references](INDEX.md).
