# Merge

## Merge

### Merge 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Merge ,
Context Menu ‣ Merge

Shortcut :

M

Fuses the selected vertices together. The menu lists:

At Center
Fuse every selected vertex into one at their geometric center — the average of their positions,
not the bounding-box center.

At Cursor
Fuse every selected vertex into one sitting at the 3D Cursor.

Collapse
Fuse each island of connected vertices into one at that island's average position.

At First
Fuse every selected vertex into whichever was picked first. Vertex selection mode only.

At Last
Fuse every selected vertex into whichever was picked last. Vertex selection mode only.

By Distance
Fuse each cluster of vertices closer together than a set distance.

Note

At First and At Last hinge on selection order, which is easily lost (for example by switching
selection mode). Run them right after making the selection as a rule.

See also

The Weld Modifier merges vertices by distance non-destructively.

### Options 

After merging, the following options are available in the Adjust Last Operation panel:

Type
The type of merge to perform.

UVs
Corrects the UV coordinates to avoid texture distortion.

Merge By Distance instead has the following options:

Merge Distance
Vertices nearer to each other than this get fused.

Centroid Merge
Set each new vertex at the average position of the vertices fused together. Off, it uses the
position of whichever original vertex sat nearest that average.

Unselected
Allow merging selected vertices with unselected ones.

Sharp Edges
On a smooth-shaded mesh carrying custom split normals, this adds edge marks where needed so sharp
edges stay sharp through the merge.

[Related references](INDEX.md).
