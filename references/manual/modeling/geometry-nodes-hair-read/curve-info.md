# Curve Info

## Curve Info

### Curve Info

Curve Info hands back per-curve attributes covering each curve's identity, geometry, and relationships in a hair or curve system. It turns up often in procedural grooming and deform setups, driving randomization, orientation, or any effect keyed to curve properties.

### Inputs

No inputs on this node.

### Outputs

Curve Index
Each curve's index within the geometry component. Use it for deterministic indexing or pattern generation.

Curve ID
A stable, unique ID per curve. Unlike Curve Index , it holds steady as curves are added or removed.

Length
Each curve's total length along its evaluated spline. Useful for scaling effects or tuning deform strength by hair length.

Direction
A unit vector from root toward tip on each curve. It captures overall heading and can orient instances or drive direction-dependent effects.

Random
A random vector per curve, seeded from the Curve ID . Randomization stays consistent across evaluations, so results read reproducible yet varied.

Surface UV
On the surface mesh, the UV coordinates of each curve's attachment point. The usual jobs: sampling textures, ferrying color across, or driving procedural effects from surface position.

[Related references](INDEX.md).
