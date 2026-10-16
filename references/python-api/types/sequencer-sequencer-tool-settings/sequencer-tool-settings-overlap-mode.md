# bpy.types.SequencerToolSettings: overlap_mode

overlap_mode

The way overlaps are settled once a transform is applied (default 'EXPAND' )

- EXPAND
Expand – Push strips aside so the transformed ones fit.

- OVERWRITE
Overwrite – Cut or split strips so the overlap goes away.

- SHUFFLE
Shuffle – Relocate transformed strips into the closest open gap to clear the overlap.

Type :

Literal[‘EXPAND’, ‘OVERWRITE’, ‘SHUFFLE’]

[Related references](INDEX.md).
