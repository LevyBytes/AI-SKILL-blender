# Editing UVs: Set User Region, Custom Region

Set User Region

Mode: Edit Mode
Menu: UV ‣ Set User Region
Shortcut: Ctrl - B

Defines a rectangular region in the UV Editor for use as a Custom Region. Once defined, this region becomes available as a Pack To target in Pack Islands by choosing Custom Region and enabling Custom Region.

Custom Region

Mode: Edit Mode
Menu: UV ‣ Custom Region
Shortcut: Ctrl - Alt - B

Enables or disables the use of a Custom Region for UV operations like Pack Islands. When enabled, the previously defined user region (created with Set User Region) becomes active and visible. This region defines boundaries for UV island packing or manipulation. Disabling restores default behavior where UV operations apply to the standard unit square or active UDIM tile.

Minimize Stretch

Mode: Edit Mode
Menu: UV ‣ Minimize Stretch

Minimize Stretch reduces UV stretch by minimizing angle differences between 3D and UV space. This operation resembles the Relax tool with the Geometry Method but uses a different algorithm.

Fill Holes — During minimize stretch, internal holes are filled with temporary polygons to prevent surrounding UV stretching and overlap.

Blend — Fraction (0-1) of the original UVs to blend after minimizing. Zero represents fully minimized stretch; 0.5 is halfway between original and minimized UVs.

Iterations — More iterations produce smoother UVs but take longer.

Stitch

Mode: Edit Mode
Menu: UV ‣ Stitch
Shortcut: Alt - V

Stitch joins selected UVs that share vertices. Use Limit and Limit Distance in the Adjust Last Operation panel to restrict stitching by distance.

Align

Mode: Edit Mode
Menu: UV ‣ Align
Shortcut: Shift - W

Positions selected UV vertices along a line specified by Axis.

Axis

Straighten — Positions UV vertices along the line defined by the endpoints.

Straighten X — Positions UV vertices horizontally along the line defined by endpoints.

Straighten Y — Positions UV vertices vertically along the line defined by endpoints.

Align Auto — Positions UV vertices automatically, choosing direction based on existing alignment.

Align Vertically — Positions UV vertices vertically along the line defined by the selection midpoint.

Align Horizontally — Positions UV vertices horizontally along the line defined by the selection midpoint.

Position Mode (Align Vertically / Align Horizontally)

How the final alignment line position is calculated:

Mean — Aligns UVs along the average position.

Minimum — Aligns UVs along the smallest coordinate value.

Maximum — Aligns UVs along the largest coordinate value.

Align Rotation

Mode: Edit Mode
Menu: UV ‣ Align Rotation

Aligns entire islands to the U or V axis. Three operation methods specify the alignment source and whether to align both axes or just V.

Auto method aligns islands so UV edges align with U or V axis; best for quads and organic meshes.

Edge method aligns only selected edges to the V axis; works best for aligning a particular edge or loop.

Geometry method considers 3D geometry. Choose X, Y, or Z axis. Edges with positive extent in the chosen axis rotate to extend upward in V axis. Works best for multiple islands sharing a geometric property.

In Auto method, edges end up aligned up/down/left/right depending on pre-existing island orientation. In Edge method, selected edges align up or down in V axis depending on current UV island orientation. In Geometry method, alignment always points upward in V axis, ignoring previous orientation.

[Related references](INDEX.md).
