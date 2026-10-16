# Copy Rotation Constraint

## Copy Rotation Constraint

The Copy Rotation constraint forces an object or bone to match a target's rotation, removing shear as a side effect. Options: Target (the object or bone whose rotation to copy); Order (the Euler order used during the copy, defaulting to the owner's); Axis (which axes to copy); Invert (which axes to flip the sign of, so 10° becomes -10° and vice versa); Mix, combining the target's current rotation with the owner's original — Replace (the target's angles replace the owner's), Add (the target's angles are added), Before Original (applied before the owner's, as if the owner were a child of the target with no constraint), After Original (applied after, as if the target were a child of the owner), or Offset (Legacy) (replicates the original Offset checkbox, meant to be like Before Original but broken with multiple axes, hence deprecated); Target/Owner (the spaces for reading angles and applying them); and Influence.

[Related references](INDEX.md).
