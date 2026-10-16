# Restore Curve Segment Length

## Restore Curve Segment Length

### Restore Curve Segment Length

Restore Curve Segment Length brings each curve segment back to its original length from a reference position, usually a pre-deformation state. It fixes unwanted stretch or squeeze that creeps in after curve deforms, simulations, or procedural edits.

### Inputs

Curves
Curves — the input geometry whose segment lengths get restored.

Selection
A boolean field choosing which points or segments are affected; unselected ones stay put.

Factor
How much the length restoration weighs in. At 0.0 the curves are left as-is; at 1.0 the original segment lengths are fully restored.

Reference Position
The pre-deformation position of curve points, used to work out the original segment lengths the node tries to restore.

Pin at Parameter
Names a parameter along each curve as a fixed anchor during restoration; other points shift relative to that pinned spot, heading off unwanted drift.

### Outputs

Curves
Output geometry with per-segment lengths restored against the supplied reference positions.

[Related references](INDEX.md).
