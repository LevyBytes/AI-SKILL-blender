# Header

## Header

View Menu:
Toolbar (T) — shows or hides the Toolbar.
Sidebar (N) — shows or hides the Sidebar.
Tool Settings — shows or hides the active tool's settings.
Footer — shows or hides the Footer.
Preview During Transform — shows a preview of a strip's start or end frame while you transform its matching handle.
Refresh All — pulls external files in afresh and rebuilds the current frame's preview, handy when you changed an external file or made a scene change Blender didn't notice.
Frame Selected — pans and zooms onto the selected image.
Fit Preview in Window (Home) — pans and zooms so the whole video is visible; this turns on Zoom to Fit.
Zoom — a menu of handy zoom levels and operations, figured from image resolution against screen resolution: 12.5% (1:8) Numpad8 out to 12.5%; 25% (1:4) Numpad4 to 25%; 50% (1:2) Numpad2 to 50%; 100% (1:1) Numpad1 back to 100%; 200% (2:1) Ctrl-Numpad2 in to 200%; 400% (4:1) Ctrl-Numpad4 to 400%; 800% (8:1) Ctrl-Numpad8 to 800%.
Zoom In/Out (Wheel) — zooms in or out.
Zoom to Fit (Shift-Home) — like Frame All, but grabs as much editor space as it can.
Zoom Region (Shift-B) — zooms in on the nearest item within the dragged border.
Auto Zoom — while on, the preview auto-zooms to keep the video size matched to the editor size.
Proxy — see Proxy.
Sequence Render Image — shows the current frame preview as a Render Result you can save as an image file.
Sequence Render Animation — saves previews of the scene-range frames (or the preview range, when active) out to a video file or a run of image files; see the Output panel.
Note: by default neither Sequence Render Image nor Sequence Render Animation outputs the finished video — both skip Scene Strips and fall back on the preview's shading mode (initially Solid). To output video with Scene Strips rendered, use the top-bar Render menu, or set Sidebar ‣ View ‣ Scene Strip Display ‣ Shading to Rendered.
Export Subtitles — exports Text strips, which can serve as subtitles, to a SubRip file (.srt); the exported file holds every Text strip in the video sequence.
Toggle Sequencer/Preview (Ctrl-Tab) — flips the editor between Sequencer and Preview.
Area — area controls; see the user-interface documentation.

Select Menu — see Selecting Strips.

Strip Menu — see Editing Strips.
Mirror:
Interactive Mirror (Ctrl-M) — begins a mirror based on the mouse position.
X Global — mirrors the image in global X.
Y Global — mirrors the image in global Y.
X Local — mirrors the image in local X.
Y Local — mirrors the image in local Y.
Duplicate (Shift-D) — copies the selected strip(s) into the nearest free channel above the original; the copy stays selected so you can reposition it at once. See also Duplicate.
Copy (Ctrl-C) — adds the selected strips to the copy-paste buffer.
Paste (Ctrl-V) — pastes strips from the copy-paste buffer.
Animation:
Insert Keyframe (I) — see Insert Keyframe.
Insert Keyframe with Keying Set (K) — see Insert Keyframe with Keying Set.
Change Keying Set (Shift-K) — see Set Active Keying Set.
Delete Keyframes (Alt-I) — see Delete Keyframes.
Clear Keyframes (Shift-Alt-I) — see Clear Keyframes.
See also Editing Keyframes.
Show/Hide:
Show Hidden Strips (Alt-H) — reveals all hidden/muted strips.
Hide Selected (H) — mutes the selected strips.
Hide Unselected (Shift-H) — mutes every strip but the selected ones.
Delete — deletes the selected strips.

Image Menu:
Transform — Move Origin (Ctrl-Period): moves the image strip's origin without shifting the strip's content; handy for setting the reference point for rotation, scaling, or further positioning — moving the origin to a corner, say, lets rotations pivot around that corner rather than the default center.
Clear — resets the selected images' position, rotation, or scale.
Apply:
Scale to Fit — sizes the selected images as large as they go while still fitting wholly inside the video; no cropping, aspect ratio kept.
Scale to Fill — sizes the selected images to fill the whole video space; they may be cropped, aspect ratio kept.
Stretch to Fill — sizes the selected images to the video's dimensions; no cropping, but aspect ratio may change.

Pivot Point — see Pivot Point.
Display Mode — see Display Mode.
Display Channels:
Color & Alpha — shows the preview with transparency over a checkerboard.
Color — ignores the preview's transparency (fully transparent areas turn black).
Gizmos — see Gizmos.
Overlays — see Sequencer Preview Overlays.

[Related references](INDEX.md).
