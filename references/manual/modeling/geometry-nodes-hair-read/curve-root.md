# Curve Root

## Curve Root

### Curve Root

Curve Root reports on the root point of each curve. It turns up in hair grooming and procedural setups to anchor deforms, apply transforms relative to the curve base, or isolate operations that hit only the roots.

### Inputs

No inputs on this node.

### Outputs

Root Selection
A boolean mask flipped true at curve root points and nowhere else. Handy for running operations strictly at the curve base.

Root Position
Each curve's root point in 3D space. Use it to align objects, sample data off a surface, or build root-based effects.

Root Direction
A unit vector for the first segment's heading, away from the root toward the next control point. Useful for orienting instances or reading initial growth direction.

Root Index
The index of each curve's root point. Usually 0 on every curve, but it can flag root points across several curves processed together.

[Related references](INDEX.md).
