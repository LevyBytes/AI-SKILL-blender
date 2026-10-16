# Proxy

## Proxy

As projects take on ever higher-resolution footage, the video preview can slow down badly. To fight that, Blender can build proxies — copies of the footage stored at lower quality and/or resolution — keeping editing smooth without hurting the final result's fidelity.

The fastest way to set up video proxies is simply to pick a Proxy Render Size in the View tab (shown when the editor is in Preview or Sequencer & Preview mode); this turns on the chosen proxy resolution for every strip and starts building the downscaled video files. Use the Proxy tab when you want to configure proxies in more detail (or make proxies for image sequences).

Proxy Settings — Reference: Panel: Sidebar region ‣ Proxy ‣ Proxy Settings. Holds scene-wide proxy settings.
Storage — how the project's proxies are stored. Per Strip (each strip says where its proxies go, below) or Project (all proxies in one directory).
Proxy Directory — where the project's proxies are stored.
Set Selected Strip Proxies — opens a pop-over to pick the resolution(s) to build and whether to overwrite existing proxy files; confirm with Set and your choices apply to the selected strips. View and tweak individual strips in the Strip Proxy & Timecode panel (below). In Preview mode, where the Proxy tab is missing, this runs through View ‣ Proxy ‣ Setup instead.
Rebuild Proxy and Timecode Indices — builds proxies and time indices for the selected strips. In Preview mode, where the Proxy tab is missing, this runs through View ‣ Proxy ‣ Rebuild instead.

Strip Proxy & Timecode — Reference: Panel: Sidebar region ‣ Proxy & Timecode ‣ Strip Proxy & Timecode. Holds strip-specific proxy settings; the header checkbox enables/disables proxy generation.
Custom Proxy:
Directory — by default generated proxy videos go to /BL_proxy/&lt;clip name&gt;, but this option points them at a custom directory.
File — lets you use preexisting proxies.
Resolutions — which proxy-video resolution(s) to build; you can pick several.
Overwrite — whether to overwrite existing proxy files or keep them.
Quality — the amount of lossy compression applied, as a percentage; lossy compression shrinks file size by dropping some image data, which can cost detail. 0% means maximum compression — smallest files, most obvious quality loss; 100% means none — full quality at a larger file size.
Timecode Index — footage copied straight off a camera without preprocessing can show many artifacts, mostly from seeking to a given frame, because such footage usually lacks correct frame-rate values in its header; this can crop up even when the clip's frame rate matches the scene's. For Blender to count frames and frame rate correctly there are two routes: preprocess the video with something like MEncoder to fix the header and insert proper keyframes, or use Blender's Timecode Index option.
None — disregards generated timecodes and seeks in the movie stream by calculated timestamp.
Record Run — seeks using timestamps read from the movie stream, giving the best alignment between scene and movie times.
Record Run No Gaps — in effect turns the movie into an image sequence, ignoring incomplete or dropped frames and frame-rate changes.
Note: Record Run is usually the best Timecode Index, but for a thoroughly damaged source file, Record Run No Gaps may be the only way to get a usable result.

[Related references](INDEX.md).
