# Array (Legacy) Modifier

## Array (Legacy) Modifier

The Array modifier creates an array of copies of the base object, each offset from the previous in any of several possible ways. Vertices in adjacent copies can be merged if nearby, allowing smooth Subdivision Surface frameworks to be generated. It's useful with tileable meshes for quickly developing large scenes, and for creating complex repetitive shapes. Multiple Array modifiers can be active on one object at the same time (e.g. to create complex three-dimensional constructs).

Options:
Fit Type — controls how the array's length is determined; the three choices each activate the display of the Curve, Length, or Count settings below.
- Fit Curve: generate enough copies to fit within the length of the curve object specified in Curve.
- Fit Length: generate enough copies to fit within the fixed length given by Length.
- Fixed Count: generate the number of copies specified in Count.
Note: both Fit Curve and Fit Length use the base object's local coordinate-system size, so scaling the base object in Object Mode won't change the number of copies generated; Fit Curve uses the curve's local coordinate-system length, so scaling the curve in Object Mode won't change it either — applying the scale can be useful for both.

Relative Offset:
Factor X/Y/Z — add a translation equal to the object's bounding-box size along each axis, multiplied by a scaling factor; X, Y, and Z scaling factors can be specified.

Constant Offset:
Distance X/Y/Z — add a constant translation component to the duplicate's offset; X, Y, and Z constant components can be specified.

Object Offset — add a transformation taken from an object (relative to the current object) to the offset. It's good practice to use an empty centered on or near the initial object — for example, rotating that empty creates a circle or helix of objects.

Merge — when enabled, vertices in each copy are merged with vertices in the next copy within the given Distance.
First and Last Copies — when enabled along with Merge, vertices in the first copy are merged with those in the last copy (again within Distance range), useful for circular objects.
Distance — controls the merge distance for Merge and First and Last Copies.

UVs:
Offset U/V — shift the UVs of each new duplicate by a settable amount.

Caps:
Cap Start, End — give either endpoint of the array a different mesh: the start as if at position -1 (one "array step" before the first regular copy), the end as if at position n + 1 (one "array step" after the last regular copy). When Merge is on, cap vertices within the Distance threshold are merged.
Note: the start/end cap objects currently do not support the First and Last Copies option.

Hints — Offset Calculation: the transformation from one copy to the next is the sum of three components (Relative, Constant, and Object), each independently enabled/disabled. This allows, for example, a relative offset of (1.0, 0.0, 0.0) and a constant offset of (0.1, 0.0, 0.0), giving an array neatly spaced along the X axis with a constant 0.1 unit between objects whatever the original object's size.

Examples: a chain created from a single link; a tentacle made with an Array Modifier followed by a Curve Modifier, where the foreground segment is the base mesh and the tentacle is capped by two specially-modeled objects deformed by the same Curve object as the main part. Fractal: a multi-level array animated with motion blur, and a fractal created with multiple arrays.

[Related references](INDEX.md).
