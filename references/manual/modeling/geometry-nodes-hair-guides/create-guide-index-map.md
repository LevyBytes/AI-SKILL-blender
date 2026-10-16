# Create Guide Index Map

## Create Guide Index Map

### Create Guide Index Map

Create Guide Index Map writes an integer attribute called guide_curve_index tying every hair curve to its nearest guide curve. Each non-guide curve gets the index of the guide it should follow.

Downstream hair-grooming nodes (for example, Braid Hair Curves, Clump Hair Curves) lean on this map to bundle curves into logical groups around shared guides and apply effects uniformly.

Other nodes in the Hair Guides Nodes category can build a map internally for convenience, but the attribute they produce matches what this node writes.

### Inputs

Geometry
Geometry — the hair-curve geometry fed in for grouping, optionally carrying existing guide curves too.

Guides
The curves or points eligible to act as guides — the candidates other curves get assigned to.

Guide Distance
The minimum spacing between chosen guides. It stops guides from being picked too close together and shapes how broad each guide's influence region runs.

Guide Mask
A mask limiting which curves may turn into guides; those with a mask value of 0 cannot be chosen.

Group ID
An ID splitting the curves into independent groups for guide assignment; a curve only picks a guide carrying the same Group ID value. Handy for keeping separate regions — say the left versus right side of a groom — from mixing.

### Outputs

Geometry
The geometry you fed in, now with two extras:

- A guide_curve_index attribute that records each curve's assigned-guide index.

- A anonymous attribute standing for the guide selection. Normal curves and the picked guide curves both remain in the result.

Guide Curves
A geometry output carrying only the curves picked as guides.

Guide Index
An integer attribute giving, per curve, the index of the closest guide curve with the matching Group ID .

Guide Selection
A boolean selection attribute, true only on curves that were chosen as guides. Use it to isolate, visualize, or further process the guide curves.

[Related references](INDEX.md).
