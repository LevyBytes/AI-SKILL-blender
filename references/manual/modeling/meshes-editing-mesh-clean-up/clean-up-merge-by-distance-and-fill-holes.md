# Clean Up: Merge by Distance, Fill Holes

### Merge by Distance 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Merge by Distance

Merges selected vertices that lie within a set distance of one another.

Merge Distance
Vertices nearer to each other than this get fused.

Unselected
Allow merging selected vertices with unselected ones.

Sharp Edges
On a smooth-shaded mesh carrying custom split normals, this adds edge marks where needed so sharp
edges stay sharp through the merge.

See also

The Weld Modifier performs this operation non-destructively.

### Fill Holes 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Fill Holes

Drops a face into every hole in the selected geometry.

Sides
The edge-count ceiling: a hole with more edges than this stays open. Use 0 to fill them all.

See also

For filling a large hole that has many edges,
Face Fill or
Grid Fill may be a better option.

[Related references](INDEX.md).
