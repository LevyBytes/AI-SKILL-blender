# Array Node: Influence: See Influence Filters., Options

## Array Modifier

The Array Modifier generates copies of the base object, with each copy offset differently in multiple possible ways. It generates complex repetitive patterns useful for intricate drawings. Multiple Array modifiers may operate simultaneously on a single object to construct elaborate structures.

Note: This documentation covers Array Modifier specific to Grease Pencil. For other object types, consult the general Array Modifier guide.

Count: Total number of copied instances. Material Override: Material index for duplicated strokes (0 applies original materials).

Relative Offset: Factor X, Y, Z translates each copy by the object's bounding box extent times the specified scaling factors for each axis.

Constant Offset: Factor X, Y, Z applies fixed translation components per copy; specify separate values for each axis.

Object Offset: Distance X, Y, Z derives transformation from another object relative to the current one; using an empty object centered near or at the source object is recommended.

Randomize: Offset X, Y, Z introduces random translation to copies. Rotation X, Y, Z adds random rotation. Scale X, Y, Z applies random scaling. Uniform Scale: Uses identical random Seed across scale axes for uniform scaling. Seed: Pseudo-random generator value.

Note: Depth Order in Grease Pencil objects influences stroke visibility when using Array; see Depth Order for details.

Influence: See Influence Filters.

The Array modifier creates multiple copies of an input geometry and arranges them in a linear, circular, or custom pattern, with flexible options for count, spacing, and randomization for both precise and organic duplication of geometry.

Options:
Shape: the method used to arrange the duplicates.
- Line: arrange copies along a straight line.
- Circle: arrange copies around a circle.
- Curve: arrange copies along a curve input.
- Transform: position each copy by a transform offset or object transform.
Offset Method (Line): how copies are spaced along a line.
- Relative: offset each copy relative to the geometry's bounding-box size.
- Offset: offset copies by a fixed world-space distance.
- Endpoint: distribute copies evenly between start and end points.
Offset (Line, Relative): how far to move each copy relative to its bounding-box size in Relative mode.
Count Method (Circle, Curve): how the number of duplicates is defined.
- Count: a fixed number of copies.
- Distance: copies based on the distance between them.
Count (Circle, Curve, Count): the number of copies to generate.
Angular Distance (Circle, Distance): the angular distance between copies in Circle shape.
Central Axis (Circle): the axis used as the up direction for circular arrangements.
Circle Segment (Circle): whether the copies form a full circle or just a partial arc.
- Full: copies evenly spaced around a full 360° circle.
- Arc: copies fan out along a circular arc.
Radius (Circle): the radius of the circle the copies are distributed along.
Sweep Angle (Circle, Arc): the total angle (in radians or degrees) the arc spans when Circle Segment is set to Arc.
Per Curve (Curve): set the number of copies for each curve separately.
Curve Object (Curve): the reference curve object for the array.
Transform Reference (Transform): how the transform is applied in Transform shape.
- Input: use the transform given directly in the node inputs.
- Object: use a specified object's transform as the reference.
Translation Inputs (Line, Offset, Endpoint): the positional offset applied to each copy.
Rotation Inputs (Line): the rotation offset applied per copy.
Scale Inputs (Line): the scale factor applied per copy.
Transform Object (Transform, Object): the object whose transform is used when Transform Reference is set to Object.
Relative Space (Transform, Object): whether the transform is applied in object or world space.
Realize Instances: convert the generated instances into real geometry; required for certain operations such as merging or boolean operations.

Align Rotation (Circle, Curve):
Forward Axis: the axis defining each instance's facing direction along the circle.
Up Axis: the axis used as the vertical reference for instance orientation.

Randomize:
Offset: maximum random translation offset for each axis, setting the variation in instance position.
Rotation: maximum random rotation for each axis.
Scale Axes: how scaling randomization is applied: Uniform (a single random scale factor on all axes) or Axes (independent random scale factors per axis).
Scale: maximum random scaling factor applied to each instance.
Flipping: randomly mirror instances along one or more axes.
Exclude First / Last: exclude the first (original) or last copy from randomization effects.
Seed: initialize the random number generator; changing it produces a different random arrangement while preserving other settings.

Merge: merge overlapping points or vertices by distance; requires Realize Instances to be enabled.
Distance: the distance threshold within which points are merged.

[Related references](INDEX.md).
