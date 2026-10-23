# Array Node: Array Node, Inputs

## Array Node

Array Node

Duplicates input geometry in linear, circular, or custom patterns with configurable count, spacing, and randomization.

Inputs:
Geometry: The shape to replicate.

Shape - Arrangement method:
Line: Straight-line arrangement.
Circle: Radial distribution.
Curve: Distribution along a curve input.
Transform: Position using transform offset or object transform.

Offset Method Line - Spacing strategy:
Relative: Offset by bounding box fraction.
Offset: Fixed world distance.
Endpoint: Even distribution between start and end.

Offset Line Relative: Bounding-box multiplier.

Count Method Circle Curve - Replica specification:
Count: Fixed count.
Distance: Space-based count.

Count Circle Curve Count: Replica quantity.

Angular Distance Circle Distance: Radial spacing angle.

Central Axis Circle: Upward reference direction for circular arrangement.

Circle Segment Circle - Arc or full 360°:
Full: Complete circle, even spacing.
Arc: Partial arc.

Radius Circle: Circle radius.

Sweep Angle Circle Arc: Total arc span (radians or degrees).

Per Curve Curve: Per-curve replica count.

Curve Object Curve: Input curve reference.

Transform Reference Transform - Application method:
Input: Direct node inputs.
Object: Object transform.

Translation Inputs Line Offset Endpoint: Per-copy displacement.

Rotation Inputs Line: Per-copy rotation.

Scale Inputs Line: Per-copy scaling.

Transform Object Transform Object: Reference object for Transform mode.

Relative Space Transform Object: Object or world space application.

Realize Instances: Converts instances to real geometry (required for merging, booleans).

Align Rotation Circle Curve:
Forward Axis: Instance facing direction.
Up Axis: Vertical reference.

Randomize:
Offset: Maximum translation variance per axis.
Rotation: Maximum rotation variance per axis.
Scale Axes - Uniform or per-axis scaling:
Uniform: Single random factor.
Axes: Independent factors per axis.
Scale: Maximum scaling factor.
Flipping: Random mirroring per axis.
Exclude First / Last: Skip randomization for original or final copy.
Seed: Random number initialization. Different seeds yield different patterns with identical other settings.

Merge (requires Realize Instances):
Distance: Merge threshold for overlapping vertices.

Outputs:
Geometry: Combined duplicated and transformed instances.

[Related references](INDEX.md).
