# Editing Dopesheet Data

## Editing Dopesheet Data

Select Menu — see also Selecting.
All (A) — selects every keyframe.
None (Alt-A) — deselects every keyframe.
Invert (Ctrl-I) — flips the selection.
Box Select (B) — drag a box to select the keyframes within it.
Box Select (Axis Range) (Alt-B) — drag a box to select keyframes in the matching time range, even those above or below the box.
Circle Select (C) — shows a circle at the cursor that you drag across keyframes to select them.
Lasso Select (Ctrl-RMB) — draw a freehand shape to select the keyframes inside it.
More (Ctrl-NumpadPlus) — grows the selection to take in the time-neighbors of the currently selected keys.
Less (Ctrl-NumpadMinus) — drops keyframes that have fewer than two selected neighbors.
Select Linked (L) — selects keys sharing a channel with an already-selected key.
Columns on Selected Keys (K) — selects keys on the same frame as an already-selected key.
Column on Current Frame (Ctrl-K) — selects every key on the current frame.
Columns on Selected Markers (Shift-K) — selects keys sharing a frame with a selected marker.
Between Selected Markers (Alt-K) — selects keys falling between the leftmost and rightmost selected markers.
Before Current Frame ([) — selects keys at or before the current frame; you can also Shift-Ctrl-LMB anywhere left of the Playhead.
After Current Frame (]) — selects keys at or after the current frame; you can also Shift-Ctrl-LMB anywhere right of the Playhead.

Marker Menu — markers flag frames that carry key points or notable events in an animation and, as in most animation editors, appear along the bottom. A few options are exclusive to the Dope Sheet editor:
Sync Markers — whether moving the selected keyframes also moves the selected markers.
Show Pose Markers (Action Editor) — shows the local pose markers (which exist only inside the action) rather than the global scene markers; while it's active, the Add Marker item likewise produces pose markers in place of scene ones.
Make Markers Local (Action Editor) — turns the selected scene markers into pose markers, so they appear only inside the currently selected action.
For the rest of the marker tools, see Editing Markers.

Channel Menu — see Graph Editor Channels.

Key Menu — most of this menu is documented on the Graph Editor's Editing F-Curves page. One key difference: scaling keyframes in the Dope Sheet Editor shifts them only along the time axis (with the Playhead as pivot) and leaves their values untouched. The Dope Sheet adds these items:
Slide (Shift-T) — stretches one set of keyframes across time while squeezing an adjacent set to compensate, keeping the total duration the same. To use it, first select three or more keyframes, drop the cursor somewhere in the middle, and press Shift-T; the range temporarily splits in two at the cursor, marked by a dashed vertical line, and moving the mouse lengthens or shortens the two halves while their keyframes follow along. Confirm with LMB or back out with RMB.
Keyframe Type (R) — assigns a type to the selected keyframes.

Snap — the toggle button enables or disables automatic keyframe snapping, and the dropdown shows a popover:
Snap To — the kind of element to snap to. Frame snaps to whole frames; Second snaps to seconds; Nearest Marker snaps to the closest Marker.
Absolute Time Snap — when off, keyframes move in increments of Snap To; e.g. with Second chosen and a key currently at 0:06+5, dragging right snaps it to 0:07+5 — its time grows by a second while its 5-frame subsecond offset stays put. When on, keyframes snap to multiples of Snap To, so in that same example the key lands on 0:07+0, dropping the subsecond offset.

Proportional Editing — see Proportional Editing.

[Related references](INDEX.md).
