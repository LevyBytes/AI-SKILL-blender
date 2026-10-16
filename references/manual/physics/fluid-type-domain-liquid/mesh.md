# Mesh

## Mesh

### Mesh

Liquid particles' companion, the mesh, is another visualization approach. It emanates from particles, often higher-res than Resolution Divisions.

Enabling Mesh signals cache which data to read. Enabled-but-missing mesh shows the original domain. Toggle-switching between original and baked mesh is possible without cache reset.

Mesh shape depends on parameter combinations. Adjusting Particle Radius shifts concavity interpretation.

Upres Factor
Mesh resolution booster, matching Resolution Divisions (mesh is this times bigger than simulation).

Particle Radius
Single liquid particle radius in voxel units, determining surface coverage and considered-liquid distance. Larger covers more area, expanding mesh volume around particles.

Relates to liquid domain Particle Radius yet interpreted independently. Mesh resolution differs from base via Upres Factor. Useful for mesh size per particle tuning.

Speed Vectors
Generates velocity Attribute recording per-frame vertex velocity. Auto-used with motion blur.

Note

Cycles motion blur requires Deformation Motion Blur enabled.

| Description | Description |
| --- | --- |
| Motion blur on.  | Motion blur off.  |

Mesh Generator
Mesh generator method determines accuracy. Final yields higher quality and more options; Preview runs faster, less smooth.

Smoothing Positive
Positive smoothing cycles. More = increasingly smooth outline, yet risks detail loss (small drops).

Smoothing Negative
Negative smoothing cycles. More = sharper outline. Preserves details but rougher (single particle has flat sides vs. rounded).

Liquid drop impact (top view) smoothing comparisons. Left: 1, 1. Middle: 10, 1. Right: 1, 10. Right shows slightly sharper splash corners. 

Concavity Upper
Upper concavity limit. High = filled/smoothed concavities.

Concavity Lower
Lower concavity limit. High = filled/smoothed concavities.

Lower > Upper produces distorted, non-manifold meshes. Avoid unless intentional.

| Upper: 1.0, Lower: 0.0.  | Upper: 1.0, Lower: 0.5.  | Upper: 1.0, Lower: 1.0.  |
| --- | --- | --- |
| Upper: 1.5, Lower: 0.0.  | Upper: 1.5, Lower: 0.5.  | Upper: 1.5, Lower: 1.0.  |
| Upper: 2.0, Lower: 0.0.  | Upper: 2.0, Lower: 0.5.  | Upper: 2.0, Lower: 1.0.  |

Bake Mesh, Free Mesh
With Modular cache.

Status bar shows progress; Esc halts. Post-baking, Free Mesh clears cache. Pause/resume available.

[Related references](INDEX.md).
