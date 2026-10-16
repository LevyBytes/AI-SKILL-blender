# bpy.ops.uv.rip

bpy.ops.uv. rip ( * , mirror = False , release_confirm = False , use_accurate = False , location = (0.0, 0.0) ) 

Tears apart selected vertices or a selected region

Parameters :

- mirror ( bool ) – Mirror Editing, (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

- location (mathutils.Vector) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
