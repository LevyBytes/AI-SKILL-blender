# Track To Constraint

## Track To Constraint

The Track To constraint points an object or bone toward a target, then rolls so a chosen local axis points up — often "Look At" or "Aim" elsewhere. When the owner sits almost directly above the target, roll about the tracking axis turns unstable, in which case use the Damped Track Constraint instead. Options: Target (the object or bone to point at); Track Axis (the owner's local axis that should point at the target, typically Y for bones, a negative axis pointing away); Up (the owner's local axis that should point up in the world) — and Track Axis and Up must differ, or the constraint stops and its icon turns red; Target Z (bring the owner's Up axis as near as it can to the target's Z axis instead of the global one); Target/Owner (the spaces for the target and owner transforms); and Influence.

[Related references](INDEX.md).
