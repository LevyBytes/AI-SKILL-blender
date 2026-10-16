# Locked Track Constraint

## Locked Track Constraint

The Locked Track constraint points an object or bone toward a target — often "Look At" or "Aim" elsewhere — where "locked" means it rotates around only one axis, that axis keeping its orientation while the other two stay in their original plane. Use cases include distant tree billboards that turn to face the camera while staying upright, or a compass needle that spins horizontally toward a magnet but never points up or down. (It can combine with other Track constraints — e.g. first a Damped Track to orient the X/Y plane toward one target, then a Locked Track to rotate within that plane toward another.) Options: Target (the object or bone to point at); Track Axis (the owner's local axis that should point at the target, typically Y for bones, a negative axis pointing away); Locked Axis (the owner's local axis that keeps its orientation — the only axis it can rotate around) — and Track Axis and Locked Axis must differ, or the constraint stops and its icon turns red; and Influence.

[Related references](INDEX.md).
