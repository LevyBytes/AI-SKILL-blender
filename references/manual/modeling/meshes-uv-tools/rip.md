# Rip

## Rip

Rip

Toolbar: Rip

The Rip tool interactively separates selected UV elements (vertices, edges, faces) from connected parts, creating a rip. After separation, elements can move in the mouse direction for interactive repositioning.

This isolates UV islands or unwraps overlapping elements without affecting surrounding geometry.

Two images show before and after states.

Note: The Rip tool is incompatible with Sync Selection. Disable Sync Selection in the UV Editor to use this tool.

See also: UV Rip Move Operator (operator version) and Mesh editing Rip (3D Viewport equivalent).

Merge

Mode: Edit Mode
Menu: UV ‣ Merge
Shortcut: M

At Center — Moves selected UVs to their average position.

At Cursor — Moves selected UVs to the 2D cursor location.

By Distance

Mode: Edit Mode
Menu: UV ‣ Merge ‣ By Distance

Merges selected UVs within the specified distance.

Merge Distance — Maximum distance between merged vertices.

Unselected — Merge selected UVs to unselected ones.

Shared Vertex — Merge UVs corresponding to the same mesh vertex (even with different UV coordinates).

Split

Mode: Edit Mode
Menu: UV ‣ Split
Shortcut: Alt - M

Selection — Disconnects the selection from the rest of the UV map, duplicating the border edge to unselected elements.

UV Rip Move

Mode: Edit Mode
Menu: UV ‣ UV Rip Move
Shortcut: V

UV Rip Move separates selected UV elements from connected components, creating a rip in the map. After separation, the selection enters move mode for precise repositioning.

This isolates UV islands or unwraps overlapping elements without affecting surrounding geometry.

Two images show the before and after states of a rip operation.

Note: UV Rip Move is incompatible with Sync Selection. Disable Sync Selection in the UV Editor to use this tool.

See also: UV Rip Tool (modal version) and Mesh editing Rip (similar 3D Viewport functionality).

[Related references](INDEX.md).
