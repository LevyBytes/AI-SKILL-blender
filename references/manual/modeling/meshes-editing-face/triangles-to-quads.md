# Triangles to Quads

## Triangles to Quads

### Triangles to Quads 

Reference

Mode :

Edit Mode

Menu :

Face ‣ Triangles to Quads

Shortcut :

Alt - J

Fuses neighboring triangles in the selection into quads — essentially the inverse of Triangulate
Faces, and runnable across a whole mesh in one pass.

To avoid producing malformed quads, the operator applies angle thresholds, which means a few
triangles can be left over.

| Description | Description |
| --- | --- |
| Before converting triangles to quads.  | After converting.  |

### Options 

Max Face Angle
The largest angle allowed between two triangle normals — coplanar triangles count as 0°, not 180°.
Triangle pairs exceeding this stay unmerged.

Max Shape Angle
How far from rectangular a quad may be. At 0° only triangles forming a perfect 90°-cornered quad
merge; at 40°, corners from 50° to 130° are allowed, and so on.

Topology Influence
How strongly to favor new quads that follow the topology of existing quads.

Tip

For best results, set Topology Influence between 100-130% and Max Angle to 180°.
Lower values may leave behind parallelograms and triangles, while higher values may cause errors.

Compare UVs
Don't merge triangles that are disjoint in any UV map.

Compare Color Attributes
Don't merge triangles that, for any Color Attribute, have different colors at their shared edge.

Compare Seam
Don't dissolve edges that are marked as UV Seams.

Compare Sharp
Don't dissolve edges that are marked as Sharp.

Compare Materials
Don't merge triangles that have different materials.

Deselect Joined
Drops the merged triangles from the selection, which makes it easy to find the triangles still
awaiting conversion.

[Related references](INDEX.md).
