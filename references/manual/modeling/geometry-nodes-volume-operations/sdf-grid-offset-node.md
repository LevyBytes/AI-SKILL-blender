# SDF Grid Offset Node

## SDF Grid Offset Node

Offsets the surface of a Signed Distance Field by a specified world-space distance. Positive offset inflates (expands); negative offset shrinks (contracts). Preserves correct signed distance properties throughout the field. Core volumetric technique for wall-thickness modification, shell generation, collision-volume expansion, or blend-margin tuning.

Inputs:
- Grid: Signed distance field to offset
- Distance: Offset distance in world units; positive expands (dilation), negative contracts (erosion); applied uniformly in all directions while preserving smoothness and SDF property

Outputs:
- Grid: SDF with surface offset; preserves SDF property for subsequent booleans or mesh conversion

[Related references](INDEX.md).
