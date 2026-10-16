# Sidebar

## Sidebar

Compositor Sidebar — View. Backdrop (Sidebar region ‣ View): the backdrop shows a Viewer node's output behind the node editor — e.g. Shift-Ctrl-LMB on an Image node previews the image, while on a Mix node it shows the mix result — and it's toggled by the Backdrop panel header checkbox or the Compositor header's Backdrop button, useful for evaluating node results while editing and comparing the graph to its output. Its options: Channels (which color channels of the backdrop show), Zoom (Alt-V, V — the backdrop's display size), Offset X, Y (screen-space offset), Move (Alt-MMB — move it interactively), and Fit (scale it to fit the view). Options (Sidebar region ‣ Options) — Performance: tweak the compositor's performance with Device (CPU or GPU for compositing) and Precision (GPU — the precision of intermediate results: Auto, full for final renders and half otherwise, or Full, full for final renders and viewport).

Tool — shows the active tool's settings.

Image:
Image — tools for working with images (see Image Settings).
Metadata — lists the image's metadata.

View:
Display — the editor's display options live here.
  Aspect Ratio — the display aspect for this image; doesn't affect rendering.
  Repeat Image — tiles the image so it fills the editor entirely.
Annotations — options for the annotation tool (see Annotations).

Scopes — shows various statistics about the image's colors. The Scopes tab is hidden while the active object is in Edit Mode or Texture Paint Mode.
Histogram — graphs the image's color distribution: for each color value (Luminance, say) on the X axis it plots the pixel count on the Y axis, so a mostly dark image peaks toward the left. Use it to balance an image's tonal range — a well-balanced image shows a smooth spread of values. Drag LMB in the histogram to adjust its vertical zoom.
  Luma — a luminosity histogram.
  RGB — the RGB channels stacked on each other.
  R/G/B/A — a single channel.
  Show Line — draws lines instead of filled shapes.
Waveform — plots the color distribution for each vertical column of pixels: the Waveform's X axis matches the image's X axis, while its Y axis spans a color component such as Luminance, and the brighter a point, the more pixels in that column share that value.
  Waveform Opacity — the points' opacity.
  Waveform Mode — Luma (one Waveform of the luminosity spread), YCbCr (the Y, Cb, and Cr Waveforms side by side), Parade (the R, G, and B Waveforms side by side), Red Green Blue (the R, G, and B Waveforms overlaid).
Vectorscope — shows color distribution radially: angle is hue, distance from center is saturation.
  Vectorscope Opacity — the points' opacity.
Sample Line — like the Histogram, but it reads its sample data from a line.
  Sample Line — used to draw the line the sample data is read from.
Samples:
  Full Sample — samples every pixel.
  Accuracy — the proportion of pixels sampled when Full Sample is off.

Image Tab:
UV Vertex — the mean position of the selected UV vertices.
Image — see Image Settings.
UDIM Tiles — see UDIM Tiles.

Tool Tab — shows the active tool's settings.

View Tab — Display: this panel holds the editor's display options.
Aspect Ratio X, Y — the display aspect for this image; doesn't affect rendering.
Repeat Image — tiles the image so it fills the editor completely.
Pixel Coordinates — uses pixel coordinates rather than relative ones (0 to 1) for the UV Vertex and 2D Cursor Location fields.
2D Cursor — Location X, Y: view and change the 2D Cursor's position.
Annotations — options for the Annotate tool.

Scopes — see Scopes in the Image Editor.

Toggle the Sidebar with View ‣ Sidebar or the shortcut N. Below you can see two Video Sequencers side by side — one in Preview mode, the other in Sequencer mode — both with their Sidebar open.

Tool — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ Tool tab. Settings for the active tool.
Drag — what dragging LMB does somewhere other than the tool's gizmo. Active Tool (the same action as dragging the gizmo), Tweak (move the image under the cursor), or Select Box (drag a rectangle and select every image partly or wholly inside it).

View — View Settings — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ View Settings.
Proxy Render Size — sets the preview resolution; lower values lose detail but run faster. No Display (preview off entirely), Scene Size (full resolution, no proxies), or 25%, 50%, 75%, 100% (a downscaled resolution, optionally using proxies — even 100% can speed things up thanks to the lower image quality and smaller file size).
Use Proxies — turns on proxies, lower-resolution and/or lower-quality copies of the footage for better preview performance; configure them in the Sidebar's Proxy tab, which only shows in the Sequencer and Sequencer & Preview modes.
Channel — set it to 0 to show every channel; a higher number shows only the channels up to and including it.
Show Overexposed — flags overexposed (blown-white) areas with a zebra pattern, the threshold set by the slider.
Show Missing Media — renders missing images/movies in solid magenta; off, missing content renders fully transparent. Tip: strips with missing content show red in the timeline.

2D Cursor — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ 2D Cursor. The 2D Cursor is the white-red crosshair circle in the preview region (when the 2D Cursor overlay is on); it can act as the Pivot Point that rotation and scaling work around.
Location X, Y — the 2D Cursor's position relative to the video's center; each edge sits 0.5 out, so (0.5, 0.5) lands at the top-right corner. You can also set it with the Cursor tool or by dragging Shift-RMB.

Frame Overlay — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ Frame Overlay. The Frame Overlay lets you display a reference frame to compare against the current one.
Set Overlay Region — drag a rectangle to bound the overlay; instead of the button you can press O while hovering the preview.
Frame Offset — the time gap, in frames, between the reference frame and the current frame.
Overlay Type — how the reference frame appears. Rectangle (part of the reference frame, set by the Overlay Region, over the current frame), Reference (only the reference frame), or Current (only the current frame). Tip: each Video Sequencer can have its own Overlay Type, so you can open two side by side for the current and reference frames.
Overlay Lock — keeps showing the same reference frame even as you move to a different time, by auto-adjusting the Frame Offset.

Safe Areas — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ Safe Areas. Shows guides marking the video area visible across all screens. See also Camera Safe Areas.

Scene Strip Display — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ Scene Strip Display. Controls how Scene Strips appear in the preview.
Shading — the shading mode to use.
Override Scene Settings — uses the current scene's Workbench render settings rather than the strips' referenced scenes; available only for the Wireframe and Solid shading modes.

Annotations — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ View tab ‣ Annotations. For managing the Sequencer's Annotations.

Metadata — Reference: Editor: Video Sequencer; View Type: Preview; Panel: Sidebar ‣ Metadata tab. Lists data baked into whichever movie or image file is currently visible (not the file the selected strip points to) — the filename, creation date, camera model, and so on. It also works for Blender-produced images; see Render Output for what metadata can be included. Other programs may store metadata too, but only text in the header's "Comments" field can be read. Some of this metadata can also appear in the preview via the Metadata overlay.
Tip: Blender can't edit the metadata; use an external program like exiftool instead. For example, to change the "Comments" field:
```text
exiftool --comments="My new comment" name-of-file.png
```
Note: metadata shows only for images/movies that have no effect applied.

[Related references](INDEX.md).
