# Timeline

## Timeline

The Timeline editor lets you jump between frames, work with keyframes, and drive animation playback.

Main View — the X axis is time, the figures 0/50/100/… are frame numbers; the blue line is the Playhead flagging the current frame, and the diamonds are Keyframes — points where you fixed a property's value at a given time.
Adjusting the View: pan by dragging MMB; zoom by dragging Ctrl-MMB, rolling the Wheel, or pressing NumpadMinus / NumpadPlus; the scrollbars at the bottom and right work too.
Frame Range: the Frame Range sets the scene animation's length, defaulting to frames 1 through 250; change it via the header's Start/End inputs or through the Output Properties.
Keyframes: by default the timeline shows only the selected items' keyframes; uncheck View ‣ Only Show Selected to show them all. Click a keyframe to select it alone, or Shift-click to add it to (or remove it from) the selection, and drag a box to grab several at once. Move the selected keyframes by dragging one, or press G, move the mouse, and click LMB to confirm (RMB to cancel); press S to scale them about the Playhead.
Markers: see the Markers page.

Header: Playback and Keying popovers, plus transport and frame controls.
View Menu:
  Adjust Last Operation: opens a pop-up to alter the last operation's properties (see Adjust Last Operation).
  Channels: shows or hides the Channels region, the left-hand tree of objects and their animatable properties.
  Frame All (Home): pans and zooms so every keyframe is visible.
  Frame Scene/Preview Range: resets the horizontal view to the scene frame range, honoring the preview range if active.
  Go to Current Frame (Numpad0): centers the Timeline on the Playhead.
  Show Markers: shows the Markers region (when markers exist); off, the Marker Menu hides and marker operators are unavailable here.
  Use Timecode (Ctrl-T): shows the X-axis time and the Playhead as timestamps rather than frame numbers; e.g. 01:03+02 reads "1 minute, 3 seconds, 2 frames."
  Sync Visible Range: keeps the editor's horizontal pan and scale in step with other time-based editors that enable this, so they show the same slice of time.
  Only Show Selected: shows only keyframes tied to the selected items (objects, bones, nodes, and so on). Note: with this on, the Timeline may omit some material keyframes of the selected objects, showing instead only those for the nodes selected in the Shader Editor.
  Only Show Errors: shows only curves and drivers that are disabled or in error, handy for debugging.
  Cache: picks which simulation caches appear on the timeline; see Cache.
  Area: area controls; see the user-interface documentation.
Marker Menu: markers flag frames carrying key points or notable events and, as in most animation editors, appear along the Timeline's bottom. For the marker tools, see Editing Markers.
Playback Popover: properties for how animations play; see Playback.
Keying Popover: properties for how keyframes are added; see Keying.
Auto Keying: options for adding keyframes automatically; see Auto Keying.
Transport Controls: buttons that drive playback; see Transport Controls.
Frame Controls: set the current frame and the start/end frames; see Frame Controls.

[Related references](INDEX.md).
