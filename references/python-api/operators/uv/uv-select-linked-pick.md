# bpy.ops.uv.select_linked_pick

bpy.ops.uv. select_linked_pick ( * , extend = False , deselect = False , location = (0.0, 0.0) ) 

Selects all UV vertices connected beneath the pointer

Parameters :

- extend ( bool ) – Extend, Extend selection rather than clearing the existing selection (optional)

- deselect ( bool ) – Deselect, Deselect linked UV vertices rather than selecting them (optional)

- location (mathutils.Vector) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
