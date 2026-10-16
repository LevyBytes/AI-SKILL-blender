# Copy Location Constraint

## Copy Location Constraint

The Copy Location constraint forces an object or bone to match a target's location. Note it has no effect on connected bones, whose position is set by their parent. Options: Target (the object or bone whose location to copy); Axis (which axes to copy); Invert (which axes to flip the sign of, so 10 becomes -10 and vice versa); Offset (when on, the target's current position is added to the owner's original position from preceding constraints rather than copied over); Target/Owner (the spaces for reading from the target and applying to the owner); and Influence. Examples: a video shows the Head/Tail effect when targeting a bone and the Vertex Group effect when targeting a mesh; and a solar-system animation has a camera follow the moon orbiting Earth, then Earth orbiting the Sun, then a fixed view of the Sun — done with two Copy Location constraints (one per body) whose Influence values are animated to smoothly hand off from one to the other.

[Related references](INDEX.md).
