# Floor Constraint

## Floor Constraint

The Floor constraint sets up a flat, infinite floor (or wall or ceiling) the owner can't pass through. Like other constraints it only considers an object's origin, not its geometry, so a cube whose origin is at its center can still sink halfway into a targeted floor plane — the Offset helps mitigate that (see also Limit Location). Options: Target (the object or bone defining the floor's location and optionally rotation); Offset (move the virtual floor up or down by a distance, e.g. to keep foot bones above the floor geometry); Min/Max (the axis perpendicular to the floor pointing toward its walkable side — Z makes a floor, X or Y a wall, -Z a ceiling, by default along the global axes); Use Rotation (use the Target's local axes for Min/Max instead of global); Target/Owner (the spaces for evaluating and limiting the coordinates); and Influence.

[Related references](INDEX.md).
