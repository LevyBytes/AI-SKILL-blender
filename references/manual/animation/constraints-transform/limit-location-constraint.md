# Limit Location Constraint

## Limit Location Constraint

Limit Location keeps an object or bone above, below, or between coordinates along one or more axes. Like other constraints it only considers an object's origin, not its geometry, so a cube whose origin is at its center can still sink halfway into a targeted floor plane. Note it has no effect on connected bones, whose position is set by their parent (see also Floor Constraint). Options: Minimum/Maximum X, Y, Z (number fields set each axis's boundaries and checkboxes set whether each applies — and if a Minimum exceeds its Maximum, the constraint uses the Maximum for both); Affect Transform (when the owner is moved by hand, restrict its Location in the Transform panel too); Owner (the space for determining and limiting the position); and Influence.

[Related references](INDEX.md).
