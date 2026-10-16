# bpy.types.BooleanModifier: material_mode

material_mode

How materials get assigned to the newly generated faces (default 'INDEX' )

- INDEX
Index Based – Assigns the material to new faces by matching the order of the material slot lists. When the modifier object lacks a given material, the face reuses that same slot index, or the first slot if there aren't enough..

- TRANSFER
Transfer – Carries materials over from filled slots into the result mesh, creating new ones where required. Where a slot is empty, the operand mesh's own material index is used as a fallback..

Type :

Literal['INDEX', 'TRANSFER']

[Related references](INDEX.md).
