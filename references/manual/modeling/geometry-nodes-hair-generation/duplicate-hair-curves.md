# Duplicate Hair Curves

## Duplicate Hair Curves

### Duplicate Hair Curves

Duplicate Hair Curves spins up extra copies of existing strands, scattering them around the original guides inside a set radius. Handy for boosting density, surrounding guides with secondary strands, or filling out a groom without hand-placing more guides.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in, holding the originals to duplicate.

Amount
How many duplicates each original strand spawns. Higher values raise density.

Viewport Amount
The share of Amount used for viewport display. Drop it for better viewport performance while the render result stays the same.

Radius
The farthest a duplicate can sit from its guide curve. Larger values spread the copies wider apart.

Distribution Shape
How duplicates spread inside the radius, center to outer edge. Shapes yield uniform, clustered, or edge-weighted spreads.

Tip Roundness
How rounded duplicate curves run near their tips. Higher values make the spread more circular and natural at the ends.

Even Thickness
On, density holds even across the duplicate radius. Off, it can swing with the distribution pattern.

Seed
Random seed for placing duplicates. Move it to rearrange the copies under the same settings.

### Outputs

Geometry
Output geometry with the duplicated hair curves.

Guide Index
An integer attribute holding each duplicate's original guide-curve index. Use it downstream to match colors or follow guide motion.

[Related references](INDEX.md).
