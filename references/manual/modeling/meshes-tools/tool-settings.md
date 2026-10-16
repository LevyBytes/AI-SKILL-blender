# Tool Settings

## Tool Settings

Edit Mode Tool Options

Transform Options

Correct Face Attributes
Adjusts geometry properties like UVs and color values during transforms.

Keep Connected
When Correct Face Attributes is active, merges attributes linked to the same vertex.

Keeping UVs connected suits organic modeling but not architectural work.

Mirror Transformations

Mirror options enable symmetric transformation of vertices, edges, or faces along a chosen axis. When one element is transformed, its mirrored counterpart (in local space) moves correspondingly, preserving symmetry.

Mirrored vertices must align precisely. Imprecise alignment prevents Mirror from recognizing the pair.

The Mirror Modifier offers an alternative for automatic symmetry handling.

Topology Mirror

This feature identifies mirrored vertices by analyzing mesh relationships rather than relying solely on position. By considering the overall topology, non-symmetrical vertices can be treated as mirrored pairs.

Requires at least one Mirror Axis enabled.

Topology Mirror works best with detailed geometry. Simple meshes (cubes, UV spheres) may yield inconsistent results.

Example Workflow

Create a new scene and delete the default cube. Add a Monkey object.

Press Tab to enter Edit Mode.

Disable Mirror axes and move one vertex slightly.

Enable X Axis Mirror without Topology Mirror. Move the same vertex again — X Axis Mirror won't affect other vertices since they're not perfectly aligned.

Enable Topology Mirror and move the same vertex once more. X Axis Mirror now mirrors the other vertex despite imperfect positioning.

Auto Merge

Mode: Edit Mode
Menu: Sidebar ‣ Tool ‣ Options ‣ Auto Merge

When vertices move closer than the Threshold distance, they automatically merge. This applies to interactive operations only (including Adjust Last Operation tweaks). If multiple vertices occupy the exact target location, the moved vertex merges with one of them.

Split Edges & Faces
Detects edge intersections from transforms, creating vertices at intersection points and splitting the edge and any containing face.

Threshold
Maximum distance between vertices before merging occurs.

UV Options

Live Unwrap
Recalculates UV unwrapping each time a seam property changes on an edge. This differs from the Live Unwrap option in the UV Editor.

[Related references](INDEX.md).
