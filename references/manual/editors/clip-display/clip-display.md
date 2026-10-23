# Clip Display

## Clip Display

This pop-over gathers display settings for both Tracking mode and Mask mode.

R, G, B: sets which color channels feed the frame preview. Because the tracker works on grayscale images, toggling channels lets you find the combination of enabled and disabled channels that yields the best contrast and the least noise. This affects the preview only; to choose the channels used for actual tracking, set a default for new markers from the Track tab in the Toolbar, or configure existing markers from the Track tab in the Sidebar.
Grayscale Preview (B/W): renders the entire frame in grayscale.
Mute Footage (M): hides the movie clip and shows a black image instead, which helps you spot markers that are tracked poorly or not at all.
Render Undistorted: uses the Lens settings on the video preview to cancel lens distortion, without altering the footage itself.
Show Stable: applies the 2D stabilization settings to the preview, without altering the footage itself.
Grid: draws a grid that starts out orthographic but gets bent by the Lens settings; useful for manual calibration, since the warped grid lines should coincide with footage lines that are supposed to read as straight.
Calibration: puts the Lens settings to work on annotation strokes; like Grid, it aids manual calibration.
Display Aspect Ratio: changes the aspect ratio for display only, leaving tracking and solving untouched.

Marker Display: governs how markers appear in the editor.
Pattern: whether to show the tracks' pattern areas; useful for cutting clutter and gauging tracking quality.
Search (Alt-S): whether to show the search areas of selected tracks; again, useful for reducing clutter and checking tracking quality.
Path: shows a track's past (red) and future (blue) positions relative to the current frame, visualizing its motion so irregularities stand out.
Length: the Path's length in frames.
Show Disabled (Alt-D): when off, hides tracks disabled on the current frame (except the active one, last selected); this declutters the view and makes tracking accuracy easier to judge.
Info: shows each selected track's name and status, where the status may read "keyframed," "tracked," "disabled," and so on.
3D Markers: shows the outcome of solving the markers' 3D positions from their 2D motion; each 3D point is projected back onto the clip and drawn as a small dot, green when it lands close to the original 2D marker (a good solve) or red when it's far off (needs tweaking).
Display Thin: by default marker areas appear as bright boxes with a black outline; this option draws them as thin dashed lines instead.

[Related references](INDEX.md).
