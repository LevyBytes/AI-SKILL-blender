# Navigating

Header — View Menu: the View menu governs the editor's view settings.
Toolbar (T) — shows or hides the Toolbar.
Sidebar (N) — shows or hides the Sidebar.
Tool Settings — shows or hides the active tool's settings.
Adjust Last Operation — opens a pop-up to alter the last operation's properties (see Adjust Last Operation).
Channels — shows or hides the Channel Region.
Playback Controls — shows or hides the Playback Controls.
Refresh All (Ctrl-E) — pulls external files in afresh and rebuilds the current frame's preview, handy when you changed an external file or made a scene change Blender didn't notice.
Frame Selected (NumpadPeriod) — zooms to show only the selected strips.
Frame All (Home) — zooms to show every strip.
Frame Scene/Preview Range — resets the horizontal view to the scene frame range, honoring the preview range if active.
Go to Current Frame (Numpad0) — centers the horizontal timeline on the current frame.
Zoom to Border (Shift-B) — click and drag a rectangle, then zoom to it.
Limit View to Contents — keeps you from panning above the topmost channel in use.
Show Markers — shows the marker region; off, the Marker menu hides and marker operators are unavailable here.
Use Timecode (Ctrl-T) — shows seconds rather than frames on the time axis.
Sync Visible Range — keeps the editor's horizontal pan and scale in step with other time-based editors that enable this, so they show the same slice of time.
Navigation:
Play Animation (Spacebar) — starts or stops playback, across every editor.
Go to Current Frame (Numpad0) — scrolls so the current frame sits at the timeline's center.
Jump to Previous Strip (PageUp) — sends the playhead to the nearest strip border (start or end) before the current frame.
Jump to Next Strip (PageDown) — sends the playhead to the nearest strip border after the current frame.
Jump to Previous Strip (Center) (Alt-PageUp) — sends the playhead to the nearest strip center before the current frame.
Jump to Next Strip (Center) (Alt-PageDown) — sends the playhead to the nearest strip center after the current frame.
Range:
Set Preview Range (P) — interactively define the frame range for preview playback/rendering; while active, playback stays within it (handy for replaying a segment without rewinding), and it also bounds what Sequence Render Animation renders.
Set Preview Range to Strips — applies a preview range spanning the selected strips.
Clear Preview Range (Alt-P) — clears the preview range.
Set Start Frame (Ctrl-Home) — sets the scene's Start frame to the current frame.
Set End Frame (Ctrl-End) — sets the scene's End frame to the current frame.
Set Frame Range to Strips — sets the scene's Start and End frames to span the selected strips.
Sequence Render Image — shows the current frame preview as a Render Result you can save as an image file.
Sequence Render Animation — saves previews of the scene-range frames (or the preview range, when active) out to a video file or a run of image files; see the Output panel.
Note: by default neither Sequence Render Image nor Sequence Render Animation outputs the finished video — both skip Scene Strips and fall back on the preview's shading mode (initially Solid). To output video with Scene Strips rendered, use the top-bar Render menu, or set Sidebar ‣ View ‣ Scene Strip Display ‣ Shading to Rendered; that option is only available with the Video Sequencer in Preview or Sequencer & Preview mode.
Export Subtitles — exports Text strips, which can serve as subtitles, to a SubRip file (.srt); the exported file holds every Text strip in the video sequence.
Toggle Sequencer/Preview (Ctrl-Tab) — flips the editor between Sequencer and Preview.
Area — area controls; see the user-interface documentation.

Marker Menu — markers flag frames carrying key points or notable events and, as in most animation editors, appear along the editor's bottom. See Editing Markers.

Sequencer Scene — a data-block menu to choose a scene; the Sequencer Scene is the scene the Sequencer's edit lives in.

Playback Controls — this region holds controls and options for playback, keying, auto keyframing, and transport. They let you control how animations preview and sync with audio, add and manage keyframes via keying sets and auto keying, navigate the timeline with playback and transport controls, and set frame ranges and preview chosen segments.
Sync Scene Time — sets the active scene and time from the current scene strip; see the workspace settings.
See also the Playback Controls documentation for the full footer rundown.

Main View — Adjusting the View: use these shortcuts:
- Pan: MMB.
- Horizontal scroll: Ctrl-Wheel, or drag the horizontal scrollbar.
- Vertical scroll: Shift-Wheel, or drag the vertical scrollbar.
- Zoom: Wheel.
- Scale view: Ctrl-MMB dragged left/right (horizontal scale) or up/down (vertical scale); or drag the scrollbar circles with LMB.
Playhead — the blue vertical line carrying the current time at its top; see the Playhead documentation for how to use it. The Video Sequencer adds a special case: start dragging on a strip and that strip gets highlighted and shown solo in the preview, with all others temporarily muted.

If scrubbing (or ordinary playback) runs poorly, you can speed it up by making proxies.

Hint: the current frame is synced across every editor, so moving the Playhead in the Timeline editor, say, also moves it in the Video Sequence editor (and the reverse).

[Related references](INDEX.md).
