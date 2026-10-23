# Roll Hair Curves

## Roll Hair Curves

### Roll Hair Curves

Roll Hair Curves winds strand tips into coils, rolling them in or out under a handful of geometric controls — good for spiral or curled looks, rolled fur, or stylized motion.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for rolling.

Factor
Overall strength of the roll. At 0.0 nothing happens; at 1.0 the full roll lands.

Subdivision
How finely each strand subdivides ahead of the deform. Higher values smooth and detail the rolls at more compute cost.

Variation Level
Works variation into the roll path by smoothing or warping it. Raise it for more natural, uneven rolls.

Roll Length
The stretch of each strand, back from the tip, that gets rolled. Larger values lengthen the coiled section.

Roll Radius
The roll's radius, fixing how tightly each strand winds.

Roll Depth
Offsets along the roll axis to stretch or compress the spiral.

Roll Taper
Sets how the roll radius shrinks toward the tip, tapering the spiral.

Retain Overall Shape
On, the roll is offset along the strand's original path so the initial flow and shape of the hair survive better.

Roll Direction
The axis the roll turns around (for example X, Y, or Z), which fixes how the curls are oriented.

Random Orientation
Randomizes roll direction to break up uniform patterns and read naturally.

Seed
The random seed for that orientation randomization. Change it to redistribute curl directions while other settings hold.

Preserve Length
On, each strand keeps its full length. Off, curves may stretch or compress slightly from the rolling.

### Outputs

Geometry
Output geometry with the rolled hair curves applied.

[Related references](INDEX.md).
