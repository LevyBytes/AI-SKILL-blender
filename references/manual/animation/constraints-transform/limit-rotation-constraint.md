# Limit Rotation Constraint

## Limit Rotation Constraint

The Limit Rotation constraint limits each axis's Euler rotation angle to a range, clamping out-of-range angles to whichever boundary is nearer on the circle (so with a 0°-90° range and an original 340°, the result is 0°, not 90°). It doesn't work for bones affected by Inverse Kinematics — use the Limit settings in the bone's IK panel instead. Options: Limit X, Y, Z (number fields set each axis's angle range and checkboxes set whether each applies — and even with all limits off, the constraint still removes shear as a side effect); Order (the Euler order used when applying limits, defaulting to the owner's, or XYZ for a non-Euler owner); Affect Transform (when the owner is rotated by hand, restrict its Rotation in the Transform panel too); Legacy Behavior (for backwards compatibility — the semi-broken pre-4.2 behavior that mishandles the looping nature of rotations and causes erratic snapping, occasionally useful with Owner set to Local Space as some old rigs rely on, though drivers on the rotation properties do this better, so new rigs should prefer those); Owner (the space for determining and limiting rotation); and Influence.

[Related references](INDEX.md).
