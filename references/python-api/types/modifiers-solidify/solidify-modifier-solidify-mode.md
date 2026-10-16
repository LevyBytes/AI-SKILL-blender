# bpy.types.SolidifyModifier: solidify_mode

solidify_mode

Picks which algorithm is used (default 'EXTRUDE' )

- EXTRUDE
Simple – Output a solidified version of a mesh by simple extrusion.

- `NON_MANIFOLD`
Complex – Output a manifold mesh even if the base mesh is non-manifold, where edges have 3 or more connecting faces. This method is slower..

Type :

Literal[‘EXTRUDE’, ‘`NON_MANIFOLD`’]

[Related references](INDEX.md).
