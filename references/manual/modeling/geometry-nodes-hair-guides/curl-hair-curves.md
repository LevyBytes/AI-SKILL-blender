# Curl Hair Curves

## Curl Hair Curves

### Curl Hair Curves

Curl Hair Curves bends existing strands into curls by winding them around nearby guide curves — the tool for coiled, spiral, or wavy looks and for layering stylized flair or realism onto a groom. Each curl's radius, turn rate, and start point can shift, and optional random offsets break up the regularity.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for curling.

Factor
Overall strength of the curl. At 0.0 the effect is off; at 1.0 the full curl deform applies.

Subdivision
Subdivisions applied before the deform. Higher values smooth the curls but add processing time.

Curl Start
The percentage along each strand (root to tip) where the curl begins, letting you keep part of the strand straight ahead of it.

Radius
The curls' overall radius. Larger values loosen the curls; smaller values tighten them into spirals.

Factor Start
Multiplies curl radius near the start of the curl region, so tightness tapers in or builds gradually.

Factor End
Multiplies curl radius near the strand's end, steering how curls taper off or unwind toward the tip.

Frequency
How many full turns run down the strand's length; higher values pack in more curls. It can vary per point along the strand, enabling complex wave patterns.

Random Offset
Works random variation into each strand's curl phase or starting angle, for a more natural, less uniform look.

Seed
The random seed behind the random offsets. Move it for different curl variations under the same settings.

### Guide Map

Guide Index
A map flagging which curve is the guide, or central reference, for each cluster of curled curves. Pass one in and it trumps any guide_curve_index attribute on hand; the two settings below sit idle.

Guide Distance
How far apart picked guides must be when the node spins up its own map. Raise it for fewer guide curves and wider curl groups.

Guide Mask
A mask choosing which curves can stand in as guides.

Existing Guide Map
On, reuse a guide map attribute that already exists. Off, absent a Guide Index, the node derives one from the spacing and mask above. Authoring it separately buys you steadier control and consistency across grooming steps.

### Outputs

Geometry
Output geometry with the curled hair curves.

### Guide Map

Guide Index
The index map this operation leaned on. Should the node have generated a fresh one, it lands here for downstream nodes to pick up.

[Related references](INDEX.md).
