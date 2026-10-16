# Spin

## Spin

Spin

Mode: Edit Mode
Menu: Mesh ‣ Extrude ‣ Spin
Toolbar: Spin

Spin extrudes (or duplicates if the selection is manifold) selected geometry, rotating it around a specific center point and axis. This produces lathe-like objects — circular extrusions centered on the 3D cursor and revolving around an axis perpendicular to your current view.

The viewing angle determines the rotation axis. The 3D cursor position sets the rotation center.

Tool Options

Steps
Number of copies to extrude along the rotation.

Use Duplicates
Keeps the original selected elements as separate, unlinked islands.

Axis
The pivot axis for the spin operation.

Options Panel

Steps
Number of copies along the revolution.

Angle
Sweep angle in degrees (for example, 180 creates a half rotation).

Auto Merge
Automatically joins the first and last duplicates if a full 360-degree rotation produces overlapping geometry.

Flip Normals
Reverses the normal direction of resulting surfaces.

Center X, Y, Z
Spin rotation center; defaults to the cursor position.

Axis X, Y, Z
Rotation axis vector; defaults to the current view axis.

Workflow Example

Create a 2D profile of your desired object. For a hollow object, thicken the outline.

Switch to top view (Numpad7) to work from above.

Place the 3D cursor at the profile's center. Enter Edit Mode, select a center vertex, then snap the cursor to it with Mesh ‣ Snap ‣ Cursor to Selection.

Select all vertices with A and activate Spin from the toolbar. Use the gizmo to rotate.

Angle Variations

Two side-by-side examples show a full 360-degree rotation and a 120-degree partial rotation.

Duplicate Mode

When Use Duplicates is enabled, the original geometry remains separate from the spun copies.

Handling Duplicate Vertices

The spin leaves duplicate vertices along the profile seam. Box select (B) to capture seam vertices, then apply Merge by Distance.

Compare the vertex count before and after merging (shown in the Mesh data panel). The final count should match the original profile count. If not, some vertices were missed and need manual welding.

To merge two vertices: select both with Shift - LMB, press S to scale, hold Ctrl while scaling to zero, then LMB to confirm. Run Mesh ‣ Merge ‣ By Distance or press M and choose By Distance.

Final Step

Recalculate normals by selecting all vertices, pressing Alt - N, and confirming Recalculate Normals Outside.

[Related references](INDEX.md).
