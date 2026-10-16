# Sort Elements

## Sort Elements

### Sort Elements

Reference

Mode:

Edit Mode

Menu:

Mesh → Sort Elements…

Reorders the internal storage of selected mesh elements.

Hint

Enable Developer Extras in Preferences, then turn on the Indices overlay in the 3D Viewport to view element storage indices.

View Z Axis
Sort by the current viewport's Z axis, from farthest to nearest.

View X Axis
Sort by the current viewport's X axis, left to right.

Cursor Distance
Sort by distance from the 3D Cursor, nearest to farthest.

Material
Sort faces by material slot index, lowest to highest. Relative order within each "material group" persists.

Selected
Move all selected elements to the start (maintaining their relative order).
Warning: This also changes unselected element indices!

Randomize
Shuffle selected elements randomly.

Reverse
Flip the order of selected elements.

The Adjust Last Operation panel includes:

Type
The applied sort order (as listed above).

Elements
Choose to sort vertices, edges, or faces. Initially matches the current selection mode.

Reverse
Invert the default sort direction.

Seed
When using Randomize, different seeds generate different orderings.

[Related references](INDEX.md).
