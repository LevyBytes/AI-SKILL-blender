# Curve Tip

## Curve Tip

### Curve Tip

Curve Tip reports on the tip — the end point — of each curve. It comes up in hair grooming, deform, and simulation setups to steer operations at curve ends: shaping, alignment, or tip-based effects.

### Inputs

No inputs on this node.

### Outputs

Tip Selection
A boolean mask reading true at curve tip points alone. Use it to single out operations that touch just the curve ends.

Tip Position
Each curve's tip point in 3D space. Useful for pinning where curves end, placing instances, or measuring length.

Tip Direction
A unit vector for the heading of each curve's final segment, toward the tip. Use it to orient instances or drive effects keyed to curve direction.

Tip Index
The index of each curve's tip point — the last point in the curve's point list.

[Related references](INDEX.md).
