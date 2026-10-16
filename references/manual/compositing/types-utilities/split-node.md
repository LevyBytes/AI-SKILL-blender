# Split Node

## Split Node

The Split node combines two input images into one output, showing them side by side or along a rotated split line — useful for comparing two versions of one image — say, before and after a color correction or render tweak. Inputs: Position (a 2D vector locating the split line in normalized 0-to-1 coordinates, so (0.5, 0.5) centers it); Rotation (the split line's angle in degrees); Image (the first input, on one side); and Image (the second input, on the opposite side). Output: Image (the combined image divided by the split line). Gizmos: an interactive Node-Editor gizmo (enable Active Node Gizmo and select the Split node) shows a split line with draggable handles — drag the line to move the split, and use the central circular handle to rotate it interactively. Examples: typically used to compare two images in the compositor (connect to a Viewer Node for before/after, like an ungraded versus color-corrected render), and also to align scene transitions by showing one scene's last frame beside another's first for visual consistency.

[Related references](INDEX.md).
