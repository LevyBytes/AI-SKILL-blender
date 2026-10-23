# Graph editor menus and controls

Header - View Menu:
Sidebar (N): shows or hides the Sidebar Region.
Adjust Last Operation: opens a pop-up to alter the last operation's properties (see Adjust Last Operation).
Channels: shows or hides the Channels Region.
Playback Controls: shows or hides the Playback Controls.
Frame Selected (NumpadPeriod): pans and zooms onto the selected keyframes.
Frame All (Home): pans and zooms to show every keyframe.
Frame Scene/Preview Range: resets the horizontal view to the scene frame range, honoring the preview range if active.
Go to Current Frame (Numpad0): centers the area on the Playhead.
Realtime Updates: whether other views (the 3D Viewport, say) refresh while you drag keyframes; if off, they update only when you finish.
Show Sliders: adds a value slider beside each channel; nudging one inserts a keyframe automatically.
Auto-Merge Keyframes: auto-merges keyframes landing on the same frame after a transform.
Auto-Lock Key Axis: auto-locks keyframe movement to whichever axis best matches the mouse direction.
Show Markers: shows the marker region; with it off, the Marker Menu hides and marker operators are unavailable here.
Show Cursor: toggles the horizontal blue line (see Playhead & 2D Cursor).
Use Timecode (Ctrl-T): shows timing in seconds rather than frames; e.g. 01:03+02 reads "1 minute, 3 seconds, 2 frames."
Sync Visible Range: keeps the editor's horizontal pan and scale in step with other time-based editors that enable this, so they show the same slice of time.
Show Extrapolation: toggles the extrapolated portion of curves.
Show Handles (Ctrl-H): toggles display of keyframe handles.
Only Selected Keyframes Handles: shows handles only for the selected keyframes.
Set Preview Range (P): drag a box to set a preview time range; while active, playback stays inside it for replaying a segment without rewinding. Change its start/end with the matching button in the Timeline editor's Playback popover, or just run Set Preview Range again.
Clear Preview Range (Alt-P): clears the preview range.
Set Preview Range to Selected (Ctrl-Alt-P): sets a preview range covering the selected keyframes.
Toggle Dope Sheet: flips the area over to the Dope Sheet Editor.
Area: area controls; see the user-interface documentation.

Select Menu:
All (A): selects all keyframes and handles.
None (Alt-A): clears the selection.
Invert (Ctrl-I): flips the selection.
Box Select (B): drag a box to select the keyframes and handles inside it.
Box Select (Axis Range) (Alt-B): drag a box to select keyframes and handles in the matching time range, even above or below the box.
Box Select (Include Handles): selects keyframes and their handles inside the box.
Circle Select (C): shows a circle at the cursor that you drag over keyframes and handles to select them.
Lasso Select (Ctrl-RMB): draw a freehand shape to select the keyframes and handles inside it.
Columns on Selected Keys (K): selects keys on the same frame as an already-selected key.
Column on Current Frame (Ctrl-K): selects every key on the current frame.

Columns on Selected Markers (Shift-K): selects keys sharing a frame with a selected marker.
Between Selected Markers (Alt-K): selects keys between the leftmost and rightmost selected markers.
Before Current Frame ([) — selects keys at or before the current frame; you can also Shift-Ctrl-LMB anywhere left of the Playhead.
After Current Frame (]): selects keys at or after the current frame; you can also Shift-Ctrl-LMB anywhere right of the Playhead.
Select Handles: selects the handles of the currently selected keyframes.
Select Keys: selects the keyframes of the currently selected handles.
Select More (Ctrl-NumpadPlus): grows the selection to take in the time-neighbors of the selected keys.
Select Less (Ctrl-NumpadMinus): drops keys with fewer than two selected neighbors.
Select Linked: selects keys on the same curve as an already-selected key.

Marker Menu: markers flag frames carrying key points or notable events in an animation and, as in most animation editors, appear along the bottom. For the various marker tools, see Editing Markers.

Channel Menu: see Editing Channels.

Key Menu: see Editing F-Curves.

Normalize: scales each curve's display so they all seem to span the same -1-to-1 range, which eases editing when curves have wildly different value ranges. Turning it on zooms the view to match and darkens the area outside the normalized range. With a preview range defined, keys inside it are normalized while the rest scale proportionally.
Auto Normalization: recomputes curve normalization on every curve edit.

View Controls:
Show Only Selected: shows only curves of selected objects/bones/….
Show Hidden: shows keyframes from hidden objects/bones/….
Show Only Errors: shows only channels with errors (e.g., ones animating a property the object lacks).
Create Ghost Curves (framed F-Curve icon): snapshots the current curves and shows them in the background as a reference; click again to clear it.
Filter (funnel icon):
  Search: filters the channel list by a search term.
  Filtering Collection: pick a collection to show only its objects' keyframes.
  Filter by Type: filters curves by property type.
  Sort Data-Blocks: sorts data-blocks alphabetically for easier finding; if it slows playback (really only with many objects), switch it off.

Transform Controls:
Pivot Point: the pivot for rotating and scaling.
  Bounding Box Center: the center of the smallest box around the selected keyframes.
  2D Cursor: where the Playhead meets the horizontal Cursor line.
  Individual Centers: rotate/scale each handle about its own keyframe.
Snap: the icon toggles snapping; the dropdown adds:
  Snap To: the element to snap to: Frame (whole frames), Second (seconds), Nearest Marker (the closest Marker).
  Absolute Time Snap: off, keyframes move in increments of Snap To; e.g. with Second and a key on 0:06+5, dragging right snaps to 0:07+5, gaining a second while keeping its 5-frame subsecond offset. On, keyframes snap to multiples of Snap To, so the same key lands on 0:07+0, losing the offset.
Proportional Editing (O): see Proportional Editing.

Playback Controls: this region holds controls and options for playback, keying, auto keyframing, and transport. They let you control how animations preview and sync with audio, add and manage keyframes via keying sets and auto keying, navigate the timeline with playback and transport controls, and set frame ranges and preview chosen segments. See also the Playback Controls documentation for the full footer rundown.

Sidebar Region - View Tab:
Show Cursor: toggles the 2D Cursor's horizontal line.
Cursor X, Y: shows and lets you edit the 2D Cursor's X (current frame) and Y (value) coordinates.
Cursor to Selection: sets the 2D Cursor to the mean time-and-value of the picked keyframes.
Cursor Value to Selection: drops the 2D Cursor at the selected keyframes' average value, leaving its time alone.
F-Curve Tab: see F-Curve Properties.
Modifiers Tab: see F-Curve Modifiers.

[Related references](INDEX.md).
