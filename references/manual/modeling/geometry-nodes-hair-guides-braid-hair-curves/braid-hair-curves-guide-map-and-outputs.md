# Braid Hair Curves: Guide Map, Outputs

### Guide Map

Guide Index
A map saying which curve serves as central "guide" for a given braid group. Hand one in and it supersedes any existing guide_curve_index attribute; the two inputs below get bypassed.

Guide Distance
Minimum spacing between picked guides when the map is generated on the fly. Bigger numbers thin out the guides and widen each braid group.

Guide Mask
A mask gating which curves are even eligible to count as guides.

Existing Guide Map
On, lean on a guide map attribute already in place (guide_curve_index, for instance). Off, with no Guide Index handed in, the node generates one from the spacing and mask above. Prebuilding it elsewhere — a separate node or modifier — wins you finer say over which curves end up as braid guides.

### Outputs

Geometry
Output geometry with the braid deform applied.

Flare Parameter
Runs 0 to 1 to mark position within the braid's flare region. Drive shading from it, or layer on effects — tying, binding, loosening toward the tip.

Strand Index
Tags which braid strand a curve belongs to inside its braid group.

### Guide Map

Guide Index
The map of guide indices that actually drove this braid. Built fresh by the node? It exits here so later nodes can reuse it.

[Related references](INDEX.md).
