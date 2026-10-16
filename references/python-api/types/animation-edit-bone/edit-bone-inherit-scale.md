# bpy.types.EditBone: inherit_scale

inherit_scale

How the bone takes on scaling from its parent (default 'FULL' )

- FULL
Full – Take on every effect of the parent’s scaling.

- `FIX_SHEAR`
Fix Shear – Take on the scaling but strip out shear from the child in the rest orientation.

- ALIGNED
Aligned – Spin non-uniform parent scaling into line with the child, sending parent X scale onto the child X axis and so on.

- AVERAGE
Average – Take on a uniform scale standing in for the parent’s overall change in volume.

- NONE
None – Disregard the parent’s scaling entirely.

- `NONE_LEGACY`
None (Legacy) – Disregard parent scaling without compensating for parent shear. Reproduces what turning off the old Inherit Scale checkbox did..

Type :

Literal[‘FULL’, ‘`FIX_SHEAR`’, ‘ALIGNED’, ‘AVERAGE’, ‘NONE’, ‘`NONE_LEGACY`’]

[Related references](INDEX.md).
