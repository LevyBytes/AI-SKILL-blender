# Sidebar Region

## Sidebar Region

Footage — Proxy/Timecode: high-resolution video can drag down Blender's performance, making scrubbing and other operations sluggish. To counter that, generate one or more proxies — copies of the footage kept at lower resolution and/or quality — and use them as lighter stand-ins while you work.
Build Original: which proxy resolution(s) to make from the original, distorted footage.
Build Undistorted: which proxy resolution(s) to make from the undistorted footage (i.e. with the Lens settings applied to remove the recording's distortion).
Quality — the amount of lossy compression applied, given as a percentage. Lossy compression shrinks file size by discarding some image data, which can cost detail. 0% means maximum compression — smallest files, most obvious quality loss; 100% means none — full quality at a larger file size.
Proxy Custom Directory: proxies normally land in a BL_proxy subfolder beside the original file; use this to point somewhere else.
Build Proxy/Timecode: generates proxies from the settings above along with timecode files. Instead of this button you can also choose Clip ‣ Proxy ‣ Rebuild Proxy and Timecode Indices.
Timecode Index: footage copied straight off a camera without preprocessing can show many artifacts, mostly from seeking to a particular frame, because such footage usually lacks correct frame-rate values in its header; this can crop up even when the clip's frame rate matches the scene's. For Blender to count frames and frame rate correctly there are two routes: preprocess the video with something like MEncoder to fix the header and insert proper keyframes, or use Blender's Timecode Index option.
  None: disregards generated timecodes and seeks in the movie stream by calculated timestamp.
  Record Run: seeks using timestamps read from the movie stream, giving the best alignment between scene and movie times.
  Record Run No Gaps: in effect turns the movie into an image sequence, ignoring incomplete or dropped frames and frame-rate changes.
  Note: Record Run is usually the best Timecode Index, but for a thoroughly damaged source file, Record Run No Gaps may be the only way to get a usable result.
Proxy Render Size: which proxy size to display; depending on the Render Undistorted setting, Blender picks either the Original proxy or the Undistorted one.

Footage Settings: see Image Settings.
Animation: manages animation data for movie-clip properties, including the active Actions and their assigned Slot; see Manually Assigning Actions and Slots.

Track: see Track.
Stabilization: see 2D Stabilization.

View - 2D Cursor: the 2D Cursor appears as the dashed crosshair sitting in the main region and can act as a transformation pivot point if you pick that option in the editor's header. It's available only in Mask mode, not Tracking mode.
  Location X, Y: the 2D Cursor's relative position, from (0, 0) at the bottom-left corner to (1, 1) at the top-right. You can also place it with Shift-RMB in or near the video.
Annotations: see Annotations.

[Related references](INDEX.md).
