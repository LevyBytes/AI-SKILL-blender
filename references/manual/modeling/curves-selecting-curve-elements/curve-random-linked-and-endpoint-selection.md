# Curve random linked and endpoint selection

Reference

Mode: Edit Mode
Menu: Select ‣ None
Shortcut: Alt+A

Clear the current selection while keeping the active element unchanged.

Reference

Mode: Edit Mode
Menu: Select ‣ Invert
Shortcut: Ctrl+I

Toggle selection: deselect what is chosen and choose what is deselected.

Reference

Mode: Edit Mode
Menu: Select ‣ Select Random

Pick a random subset based on seed and probability.

Seed: Pseudo-random sequence starter.
Probability: The percentage of control points to include.

Reference

Mode: Edit Mode
Menu: Select ‣ More/Less
Shortcut: Ctrl+NumpadPlus , Ctrl+NumpadMinus

Expand or contract selection based on connectivity.

More: For each selected point, add all its neighbors (typically one or two adjacent points).
Less: Keep a selected point only if all its neighbors are also selected.

Two consequences follow:
- If all points in a curve are chosen, More adds nothing. Conversely, Less leaves everything unchanged.
- These never "jump" to a neighboring curve—expansion stays within the current curve boundary.

Reference

Mode: Edit Mode
Menu: Select ‣ Select Linked
Shortcut: Ctrl+L

Extend selection to all points reachable from the active point along the curve path. This is especially valuable in dense curves, where point-by-point selection would be tedious.

Reference

Mode: Edit Mode
Hotkeys: L , Shift+L

Activate selection ( L ) or deactivate it ( Shift+L ) for points adjacent to the cursor position.

Note: When a Bézier handle is selected, the entire point and its chain are selected.

Reference

Mode: Edit Mode
Menu: Select ‣ Select Endpoints

Activate only the start and end points of curve segments. Only available in Control Point selection mode.

[Related references](INDEX.md).
