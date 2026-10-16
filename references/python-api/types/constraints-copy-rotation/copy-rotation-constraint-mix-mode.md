# bpy.types.CopyRotationConstraint: mix_mode

mix_mode

Choose the way the copied rotation blends with the one already present (default 'REPLACE' )

- REPLACE
Replace – Swap the copied rotation in for the original.

- ADD
Add – Sum the euler components of both rotations.

- BEFORE
Before Original – Put the copied rotation first, treating the target as though it were a parent.

- AFTER
After Original – Put the copied rotation last, treating the target as though it were a child.

- OFFSET
Offset (Legacy) – Mix the rotations the way the old Offset checkbox did. Tends to fall apart once more than one axis rotates..

Type :

Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER', 'OFFSET']

[Related references](INDEX.md).
