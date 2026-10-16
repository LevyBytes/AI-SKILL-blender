# bpy.ops.clip.select

bpy.ops.clip. select ( * , extend = False , deselect_all = False , location = (0.0, 0.0) )
Pick motion tracking markers

Parameters :

- extend ( bool ) – Extend, Extend selection rather than clearing the existing selection (optional)

- deselect_all ( bool ) – Deselect On Nothing, Deselect all when nothing under the cursor (optional)

- location (mathutils.Vector) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
