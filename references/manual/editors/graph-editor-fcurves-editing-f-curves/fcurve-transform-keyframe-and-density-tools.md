# Fcurve transform keyframe and density tools

## Editing F-Curves

Transform — Reference: Mode: Edit Mode; Menu: Key ‣ Transform. You edit an F-Curve by transforming where its keyframes sit.
Move, Rotate, Scale — like other Blender elements, keyframes can be moved, rotated, and scaled as covered in Basic Transformations.
Extend (E) — quickly shifts whichever selected keyframes lie on one side of the Playhead, handy when, say, you need to push everything after a certain time to the right to clear room. To use it, select some or all keyframes, put the pointer left or right of the Playhead, press E, move the mouse to drag only the keyframes on that side, and confirm with LMB (or cancel with RMB).
Tip: for exact figures you can also edit the Key Frame and Value properties in Sidebar ‣ F-Curve ‣ Active Keyframe. While transforming, hold Shift to move keyframes more slowly for precision, or Ctrl to move them in coarse steps.

Snap — Reference: Menu: Key ‣ Snap; Shortcut: Shift-S. Besides this menu's snapping operators, you can also switch snapping on in the header.
Selection to Current Frame — sets the selected keyframes' time to the current frame.
Selection to Cursor Value — sets the selected keyframes' value to the 2D Cursor's.
Selection to Nearest Frame — rounds each keyframe's time to the nearest frame.
Selection to Nearest Second — rounds each keyframe's time to the nearest second; Use Timecode shows seconds rather than frames at the editor's top.
Selection to Nearest Marker — sets each keyframe's time to the nearest marker's.
Flatten Handles — flattens the Bézier handles of the selected keyframes.
Equalize Handles — gives the selected keyframes' handles equal length.
  Side — which handles to touch (left, right, or both).
  Handle Length — the length to give the selected keyframes' Bézier handles.
  Flatten — sets the handle values equal to their own keyframes.
Cursor to Selected (Ctrl-G) — sends the 2D Cursor to the mean time and value across the picked keyframes.
Cursor Value to Selection — sets the 2D Cursor's value to the picked keyframes' mean value.

Mirror — Reference: Menu: Key ‣ Mirror; Shortcut: Ctrl-M. Mirrors the selected keyframes about a reference point.
By Times over Current Frame — mirrors horizontally about the current frame.
By Values over Cursor Value — mirrors vertically about the 2D Cursor's value.
By Times over Zero Time — mirrors horizontally about frame 0.
By Values over Zero Value — mirrors vertically about value 0.
By Times over First Selected Marker — mirrors horizontally about the first selected marker.

Jump to Selected — Reference: Menu: Key ‣ Jump to Selected; Shortcut: Ctrl-G. Parks the 2D Cursor at the mean time and value of the picked keyframes.

Insert — Reference: Menu: Key ‣ Insert; Shortcut: I. Adds new keyframes and selects them, leaving any previously selected ones selected too.
All Channels — keys every visible, editable F-Curve at its current value.
Only Selected Channels — keys the selected F-Curves at their current value.
Only Active F-Curve — keys the active F-Curve at its current value.
Active Channels at Cursor — keys the active F-Curve at the 2D Cursor's value.
Selected Channels at Cursor — keys the selected F-Curves at the 2D Cursor's value.

Copy/Paste — Reference: Menu: Key ‣ Copy, Key ‣ Paste; Shortcut: Ctrl-C, Ctrl-V. Ctrl-C copies the selected keyframes, Ctrl-V pastes them; afterward the Adjust Last Operation panel adds options:
Frame Offset — shifts the pasted keyframes horizontally so that… Frame Start (the first lands on the current frame), Frame End (the last lands on the current frame), Frame Relative (they keep the same distance from the current frame as when copied), or No Offset (they stay at their original frames).
Value Offset — shifts the pasted keyframes vertically so that… Left Key (the first takes the value of the existing key left of the Playhead), Right Key (the last takes the value of the key right of the Playhead), Current Frame Value (the first takes the curve's value at the current frame), Cursor Value (the first takes the 2D Cursor's value), or No Offset (they keep their original values).
Type — Mix (blends the pasted keyframes with existing ones, overwriting only those sharing a frame), Overwrite All (clears all prior keyframes in the target F-Curves), Overwrite Range (within each F-Curve, removes existing keys lying within the range of the keys pasted into it), Overwrite Entire Range (within each F-Curve, removes existing keys within the combined range of all pasted keys).
Flipped — if you copied keys from one or more pairs of symmetrically opposite bones, this pastes the left bones' keys into the right bones' curves and vice versa, inverting the values to mirror the animation.

Duplicate — Reference: Menu: Key ‣ Duplicate; Shortcut: Shift-D. Duplicates the selected keyframes; reposition them by moving the mouse.

Delete — Reference: Menu: Key ‣ Delete; Shortcut: X, Delete. X or Delete opens a pop-up for deleting the selected keyframes.

Handle Type — Reference: Menu: Key ‣ Handle Type; Shortcut: V. Sets the handle type of the selected keyframes.

Interpolation Mode — Reference: Menu: Key ‣ Interpolation Mode; Shortcut: T. Sets the selected keyframes' interpolation mode, which governs how the curve runs from each keyframe to the next.

Easing Type — Reference: Menu: Key ‣ Easing Type; Shortcut: Ctrl-E. Sets the selected keyframes' easing mode, which decides whether easing touches the left, the right, or both ends of each segment running from one keyframe to the next.

Density:
Decimate — Reference: Menu: Key ‣ Density ‣ Decimate (Ratio), Key ‣ Density ‣ Decimate (Allowed Change). Simplifies an F-Curve by dropping the keyframes that least affect its shape.
  Mode — how to decide how many keyframes to delete.
  Ratio — deletes a set percentage of keyframes.
  Remove — the percentage to remove.
  Error Margin — deletes as many keyframes as it can while keeping the F-Curve's shape within a set tolerance.
  Max Error Margin — how far the decimated curve may stray from the original.
Bake Keyframes — Reference: Menu: Key ‣ Density ‣ Bake Keyframes; Shortcut: Shift-Alt-O. Drops a keyframe on every frame. See also Bake Channels, which adds options for which range to bake and how.
Clean Keyframes — Reference: Menu: Key ‣ Density ‣ Clean Keyframes; Shortcut: X. Hunts down redundant keyframes among the selected ones and deletes them; a keyframe counts as redundant when it matches its neighbors' value, even if the surrounding curve segments aren't flat. Tip: it tends to alter the affected curves' shape, so run it after, e.g., bulk keyframe insertion across all an armature's bones (which leaves useless keys on bones that didn't move) and before hand-tweaking the curves.
  Threshold — the value threshold; raise it to also delete keys that nearly match their neighbors.
  Channels — cleans all keyframes (even unselected ones) in the selected F-Curves; a curve left with a single keyframe is deleted outright.

[Related references](INDEX.md).
