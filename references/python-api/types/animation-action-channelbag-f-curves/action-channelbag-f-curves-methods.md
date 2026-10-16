# bpy.types.ActionChannelbagFCurves: methods

new(data_path, *, index=0, group_name='')

Introduce an F-Curve into the channelbag

Parameters:

- data_path (str) – Data Path, F-Curve data path to use (never None)

- index (int) – Index, Array index ([0, inf], optional)

- group_name (str) – Group Name, Name of the Group for this F-Curve, will be created if not present yet (optional, never None)

Returns: Newly created F-Curve

Return type: FCurve
new_from_fcurve(source, *, data_path='')

Duplicate an F-Curve into the channelbag. The original F-Curve is left unchanged

Parameters:

- source (FCurve) – Source F-Curve, The F-Curve to duplicate

- data_path (str) – Data Path, F-Curve data path to use. If not provided, uses the same path as the given F-Curve (optional, never None)

Returns: Newly created F-Curve

Return type: FCurve
ensure(data_path, *, index=0, group_name='')

Retrieve the F-Curve if it exists, or create it if it does not

Parameters:

- data_path (str) – Data Path, F-Curve data path to use (never None)

- index (int) – Index, Array index ([0, inf], optional)

- group_name (str) – Group Name, Name of the Group for this F-Curve, will be created if not present yet. This parameter is ignored if the F-Curve already exists (optional, never None)

Returns: Found or newly created F-Curve

Return type: FCurve
find(data_path, *, index=0)

Scan for an F-Curve. This function performs a linear search across all F-Curves in the channelbag.

Parameters:

- data_path (str) – Data Path, F-Curve data path (never None)

- index (int) – Index, Array index ([0, inf], optional)

Returns: The found F-Curve, or None if not present

Return type: FCurve
remove(fcurve)

Erase F-Curve

Parameters:

fcurve (FCurve) – F-Curve to remove (never None)
clear()

Erase all F-Curves from this channelbag
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
