# Clump Hair Curves

## Clump Hair Curves

### Clump Hair Curves

Clump Hair Curves draws nearby strands together around chosen guide curves, forming the clumps seen in real hair, fur, and grass. A cornerstone of grooming for realism and structure, it stands in for how strands bunch from moisture, product, or contact.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for clumping.

Factor
Overall strength of the clump. At 0.0 nothing clumps; at 1.0 curves pull fully toward their guides.

Shape
How the clump reads along each strand. At 0.0 the strength is even; at 0.5 it falls off linearly from root to tip.

Tip Spread
Works random variation into curve-tip positions, blocking perfect convergence so clumps read natural.

Clump Offset
Lays a random directional offset over whole clumps, adding subtle variation between groups.

Distance Falloff
How a guide's pull fades with distance. At 0.0 there is no falloff, so every nearby curve is affected equally.

Distance Threshold
The farthest a curve can sit from a guide and still feel the clump. Past this threshold, that guide has no influence.

Seed
Drives the randomization behind offsets and variation. Move it to redistribute clumping randomly under the same settings.

Preserve Length
On, each strand holds its starting length. Off, curves may stretch or shrink a bit as they are drawn toward guides.

### Guide Map

Guide Index
A map of which guide curve sits at the heart of each clump. Provide one and it outranks any guide_curve_index attribute already present; the spacing and mask inputs below drop out.

Guide Distance
Smallest gap allowed between picked guide curves when one of these maps is generated. Bigger values give fewer, chunkier clumps.

Guide Mask
Gates which curves qualify as guides while a map is auto-generated.

Existing Guide Map
On, fall back on whatever guide map attribute is already around. Off, lacking a Guide Index, the node makes one from the distance and mask above. Authoring it on its own lets you fine-tune where guides land and how they group.

### Outputs

Geometry
Output geometry with the clumped hair curves.

### Guide Map

Guide Index
The index map this run relied on. Generated fresh here? It is stored and emitted through this output for reuse down the line.

[Related references](INDEX.md).
