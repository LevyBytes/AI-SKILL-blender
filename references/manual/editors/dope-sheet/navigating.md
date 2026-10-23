# Navigating

## Navigating

As in most editors, you can pan vertically (channels) and horizontally (time) by dragging MMB, and zoom by rolling Wheel or dragging Ctrl-MMB; the scrollbars work too.

View Menu:
Sidebar (N): shows or hides the Sidebar Region.
Adjust Last Operation: opens a pop-up panel to alter the properties of the just-finished operation (see Adjust Last Operation).
Channels: toggles the Channels region, the column of animated property names down the left side.
Playback Controls: shows or hides the Playback Controls.
Frame Selected (NumpadPeriod): pans and zooms to focus on the selected keyframes.
Frame All (Home): pans and zooms to show every keyframe.
Frame Scene/Preview Range: resets the horizontal view to the current scene frame range, honoring the preview range if it's active.
Go to Current Frame (Numpad0): pans so the Playhead is centered.
Multi-Word Match Search: lets you filter on several search terms at once (in the search box above the channel list and in the Filters popover); terms are space-separated, so "loc rot" finds channels with either "loc" or "rot" in the name, whereas with it off the list would show only channels containing the literal text "loc rot", of which there are probably none.
Realtime Updates: whether other views (the 3D Viewport, say) refresh while you drag keyframes; if off, they update only once you finish the move.
Show Sliders: adds a value slider beside each channel, and nudging one automatically inserts a keyframe.
Show Handles and Interpolation: draws keyframes with shapes reflecting their Bézier handle type, and marks a keyframe with a green line if the curve segment after it uses a non-default interpolation type (see Handles & Interpolation Display).
Show Curve Extremes: finds keys where the curve reverses direction and tags them with an arrow inside the shape: local maxima (hills) get up arrows, local minima (valleys) get down arrows. A keyframe can show both at once, namely in a summary row holding one channel with a maximum and another with a minimum.
Auto-Merge Keyframes: automatically merges keyframes that land on the same frame after a transform.
Show Markers: shows the marker region (when any markers exist); with it off, the Marker menu is hidden and marker operators are unavailable here.
Use Timecode (Ctrl-T): shows timing in seconds rather than frames.
Sync Visible Range: keeps the editor's horizontal pan and scale in step with other time-based editors that also enable this, so they all show the same slice of time.
Set Preview Range (P): drag a box to define a preview time range; while it's active, playback stays within it, letting you replay a segment without rewinding by hand. Change its start or end with the matching button in the Timeline editor's Playback popover, or simply run Set Preview Range again.
Clear Preview Range (Alt-P): clears the preview range.
Set Preview Range to Selected (Ctrl-Alt-P): sets a preview range spanning the selected keyframes.
Toggle Graph Editor (Ctrl-Tab): swaps the area over to the Graph Editor.
Cache: picks which simulation caches appear on the timeline: baked sims show fully opaque, cached sims slightly transparent, and invalid caches slightly transparent with dark diagonal stripes.
Area: area controls; see the user-interface documentation.

Filters: available from the funnel dropdown in the header.
Summary: toggles the "Summary" row atop the Channels region, which shows the union of all keyframes across every channel.
Only Show Selected: shows only keyframes belonging to selected objects/bones/…. Note: with this on, the Dope Sheet may omit some material keyframes of the selected objects, showing instead only those tied to the nodes selected in the Shader Editor.
Show Hidden: shows keyframes from hidden objects/bones/….
Only Show Errors: shows only channels with errors (for instance, ones that try to animate a property the object doesn't have).
Search: filters the channel list by a search term (or several, if Multi-Word Match Search is on).
Filtering Collection: pick a collection to show only keyframes from objects in it.
Filter by Type: filters curves by property type.
Sort Data-Blocks: sorts data-blocks alphabetically for easier finding; if it hurts playback speed (really only a concern with lots of objects), you can switch it off.

Playback Controls: this region carries controls and options for playback, keying, auto keyframing, and transport. They let you control how animations are previewed and synced with audio, add and handle keyframes via keying sets and auto keying, navigate the timeline with playback and transport controls, and adjust frame ranges and preview chosen segments. See also the Playback Controls documentation for a full description of the properties and controls usually found in the footer.

[Related references](INDEX.md).
