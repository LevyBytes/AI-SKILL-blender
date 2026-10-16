# Braid Hair Curves: Inputs, Shape Parameters, Hair Tie

## Braid Hair Curves

### Braid Hair Curves

Braid Hair Curves bends existing strands into braids by clustering nearby curves around guide curves. The deform lays a multi-strand braid pattern, with knobs for radius, twist rate, strand thickness, and an optional flare or tied finish.

It targets grooming where a few curves act as braid guides and the surrounding curves wrap them into a structured braid.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for braiding.

Factor
How strongly the braid effect lands. At 0.0 the hair is untouched; at 1.0 the full braid deform applies.

Subdivision
Subdivisions applied before the deform. Higher values smooth the braids at a performance cost.

Braid Start
Sets where along each strand the braid begins, measured from the root. Lower values start it nearer the root; higher values leave more unbraided length.

Radius
The braid's overall radius. Larger values fatten the braid by pushing strands farther from its center.

Shape
Tunes the radius profile down each strand. Use it to taper or vary braid width from root to tip.

Frequency
How fast the curves twist around the braid's center; higher values wrap tighter and more often. It can vary per point along a strand, so twists tighten or loosen down the length.

### Shape Parameters

Factor Min
The braid cross-section's lower radius factor, fixing how close strands may approach the center.

Factor Max
The braid cross-section's upper radius factor, fixing how far strands may travel outward.

Thickness
How thick each hair strand sits within the braid.

Thickness Shape
How strand thickness shifts down the braid's length.

Shape Asymmetry
Works asymmetry into the strand shaping, breaking perfect radial uniformity so the braid reads more organic.

Flare Length
How long the flare runs at the braid's end, where strands loosen or fan out.

Flare Opening
That flare's radius at the braid tip. Push it higher for a wider opening.

### Hair Tie

Hair Tie Input Type
How the hair tie object — a band or wrap, say — gets supplied for instancing.

Object :

Point at the tie through an object reference.

Geometry :

Take the tie straight from a geometry input.

Hair Tie
Whatever object or geometry caps or binds the braid end as the hair tie.

Scale
Scale of the hair tie instance.

[Related references](INDEX.md).
