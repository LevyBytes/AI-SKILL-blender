# Introduction

The NonLinear Animation editor, or NLA editor, lets you animate at a higher level: instead of individual keyframes, it works with actions — named, reusable animation segments.

Main Region: the editor shows a stack of tracks that behave like layers in an image editor, higher tracks taking precedence over lower ones, though you can also blend them. Each track can hold any number of strips, usually Action Strips (instances of actions). The orange-highlighted top track is special: the Action Track holds no strips but instead the object's active action, where new keyframes go by default. Editors like the Dope Sheet Editor normally show only this active action's keyframes; to edit another action, select it in the NLA editor and press Tab for Tweak Mode.

Header - View Menu:
Sidebar (N): shows or hides the Sidebar Region.
Adjust Last Operation: opens a pop-up to alter the last operation's properties (see Adjust Last Operation).
Channels: shows or hides the Track Region.
Playback Controls: shows or hides the Playback Controls.
Frame Selected (NumpadPeriod): pans and zooms onto the selected strips.
Frame All (Home): pans and zooms to show every strip.
Frame Scene/Preview Range: resets the horizontal view to the scene frame range, honoring the preview range if active.
Go to Current Frame (Numpad0): centers the view on the Playhead.
Realtime Updates: whether other views (the 3D Viewport, say) refresh while you drag strips; off, they update only when you finish.
Show Control F-Curves: draws a graph atop each strip that uses Animated Influence.
Show Markers: shows the marker region (when markers exist); off, the Marker Menu hides and marker operators are unavailable here.
Show Local Markers: shows action-local markers (made in the Action Editor), useful for aligning strips to one another.
Use Timecode (Ctrl-T): shows timing in seconds rather than frames.
Sync Visible Range: keeps the editor's horizontal pan and scale in step with other time-based editors that enable this, so they show the same slice of time.
Set Preview Range (P): drag a box to set a preview time range; while active, playback stays inside it for replaying a segment without rewinding. Change its start/end with the matching button in the Timeline editor's Playback popover, or just run Set Preview Range again.
Clear Preview Range (Alt-P): clears the preview range.
Set Preview Range to Selected (Ctrl-Alt-P): sets a preview range spanning the selected strips.
Area: area controls; see the user-interface documentation.

Select Menu:
All (A): selects every strip.
None (Alt-A): deselects every strip.
Invert (Ctrl-I): flips the current selection.
Box Select (B): drag a box to select strips partly or wholly inside it.
Box Select (Axis Range) (Alt-B): drag a box to select strips overlapping the matching time range, even above or below the box.
Before Current Frame ([) — selects every strip starting at or before the current frame.
After Current Frame (]): selects every strip ending at or after the current frame.

Marker Menu: markers flag frames carrying key points or notable events and, as in most animation editors, appear along the bottom. For the marker tools, see Editing Markers.

Add Menu:
Action (Shift-A): drops a strip that references an action onto the active track.
Transition (Shift-T): inserts a transition strip linking the two selected action strips.
Sound (Shift-K): adds a strip controlling when a Speaker Objects plays its sound clip.
Selected Objects: makes the selected objects show up in the NLA Editor without adding an action or track.
See Strips for the various strip types.

Track Menu: tools for NLA tracks (see Editing Tracks).
Strip Menu: tools for NLA strips (see Editing Strips).

Filters:
Only Show Selected: shows only tracks of selected objects.
Show Hidden: shows tracks of hidden objects.
Include Missing NLA: shows the Action Track even when it holds no action.
Search: filters the track list by a search term.
Filtering Collection: pick a collection to show only its objects' tracks.
Filter by Type: filters tracks by target type.
Sort Data-Blocks: sorts data-blocks alphabetically for easier finding; if it slows playback (really only with many objects), switch it off.

Snap: the toggle enables/disables automatic strip snapping; the dropdown adds:
Snap To: the element to snap to: Frame (whole frames), Second (seconds), Nearest Marker (the closest Marker).
Absolute Time Snap: off, strips move in increments of Snap To; e.g. with Second and a strip starting on 0:06+5, dragging right snaps it to 0:07+5, gaining a second while keeping its 5-frame subsecond offset.

On, strips snap to multiples of Snap To, so in that same example the strip lands on 0:07+0, losing the subsecond offset.

Playback Controls: this region holds controls and options for playback, keying, auto keyframing, and transport. They let you control how animations preview and sync with audio, add and manage keyframes via keying sets and auto keying, navigate the timeline with playback and transport controls, and set frame ranges and preview chosen segments. See also the Playback Controls documentation for the full footer rundown.

[Related references](INDEX.md).
