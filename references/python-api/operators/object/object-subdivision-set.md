# bpy.ops.object.subdivision_set

bpy.ops.object. subdivision_set ( * , level = 1 , relative = False , ensure_modifier = True ) 

Assigns a Subdivision Surface iterations (1 to 5)

Parameters :

- level ( int ) – Level, (in [-100, 100], optional)

- relative ( bool ) – Relative, Treat the subdivision surface iterations as an added step on top of the current setting (optional)

- ensure_modifier ( bool ) – Ensure Modifier, Build the matching modifier when it isn't already there (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object.py:242

[Related references](INDEX.md).
