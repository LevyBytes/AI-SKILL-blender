# bpy.types.Bone: inherit_scale

inherit_scale

Controls the manner in which scaling carries down from the parent bone (default 'FULL')

- FULL
Full – Inherit all effects of parent scaling.

- `FIX_SHEAR`
Fix Shear – Inherit scaling, but remove shearing of the child in the rest orientation.

- ALIGNED
Aligned – Rotate non-uniform parent scaling to align with the child, applying parent X scale to child X axis, and so forth.

- AVERAGE
Average – Inherit uniform scaling representing the overall change in the volume of the parent.

- NONE
None – Completely ignore parent scaling.

- `NONE_LEGACY`
None (Legacy) – Ignore parent scaling without compensating for parent shear. Replicates the effect of disabling the original Inherit Scale checkbox..

Type:
Literal['FULL', '`FIX_SHEAR`', 'ALIGNED', 'AVERAGE', 'NONE', '`NONE_LEGACY`']

[Related references](INDEX.md).
