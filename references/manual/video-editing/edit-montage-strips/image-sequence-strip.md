# Image/Sequence Strip

## Image/Sequence Strip

### Image/Sequence Strip

Image strips serve to integrate photographic content or sequenced image sets into the Video Sequencer, making them suitable for presentations, overlaid graphics, base footage, rendered frame collections, or hand-drawn animation workflows.

A single-frame strip shows one static image for a defined span, while a sequence strip plays through a collection of images sequentially, each occupying one frame slot. Both formats accommodate spatial transformation, applied effects, color space configuration, and blending operations alongside other timeline content.

Tip: Display frame previews directly on image strips in the Sequencer through the Thumbnails overlay option.

### Single Image

When you load one still image (*.jpg, *.png, etc.), Blender defaults to a 25-frame duration, displaying the image across that entire span. You can modify this length using the "Add Image Strip" operator and adjusting the property via the sidebar.

### Image Sequence

For numbered image collections (*-0001.jpg, *-0002.jpg, *-0003.jpg, etc. in any format), two primary selection modes are available:

Range
Open the directory and drag the mouse over a group of consecutive filenames to highlight them. Use page navigation and Shift-drag to extend the selection further.

Batch
Use Shift-click on individual files to gather non-consecutive images; each will play as a single frame in file order, allowing mixed formats (jpg, png, exr, etc.).

All
Press A to select or deselect every file in the current folder.

Tip

Managing Size Mismatches

Working with images of varying dimensions alongside different output resolutions requires planning. When source dimensions differ from render dimensions, the Video Sequencer attempts automatic scaling to fit the entire image within the render boundary, but this can result in parts being cut off. To avoid clipping, use Crop and/or Offset in the Input panel to reposition and select the needed region. When Crop or Offset are applied, automatic scaling disables, and manual size adjustment via the Transform effect becomes possible.

### Add Image Strip

Reference

Menu: Add ‣ Image/Sequence

Move Strips
Enable mouse positioning to place the strip immediately after insertion. When this option is on, Start Frame and Channel fields are hidden since they update interactively.

Start Frame
Designate where the strip's left edge begins on the timeline.

Channel
Which row to place the strip within.

Replace Selection
Currently highlighted strips become unselected, and only the new strip is marked as active.

Relative Path
Store file location as a path relative to the blend document.

Fit Method
Specifies how media with aspect ratios mismatched to the output resolution scale to fit the display area.

Scale to Fit:
Modifies the strip's Scale Transform so the visual material fits within the project boundary while keeping proportions unchanged. This often adds transparent borders around the content.

Scale to Fill:
Adjusts the strip's Scale Transform to fill the entire output area while preserving aspect ratio. Parts of the image may extend beyond the visible region.

Stretch to Fill:
Resizes the strip to occupy the entire output without aspect constraint. The image may become warped to fit.

Set View Transform
Automatically applies an appropriate View Transform matching the imported media's Color Space. Standard is usually correct; wrong settings risk color inaccuracy or reduced performance.

Import As
Governs how media loads into the editor.

Auto Detect:
Consecutively numbered files are loaded as a single sequence spanning their count; otherwise files appear as individual strips using the specified length.

Image Sequence:
All files become a single sequence regardless of extension or naming, and placeholders are not supported.

Individual Images:
Each file becomes a separate strip of the given length, arranged sequentially.

Use Placeholders
Image sequences can utilize placeholder files. Enable the Use Placeholders option when adding a strip. Blender recognizes the frame numbering pattern (filename + frame index + .extension) and builds a sequence spanning the detected range even if some frames are absent. This lets you render with missing frames while keeping the sequence properly timed. Missing frames appear in pink in the preview. Once the missing images are rendered or added, refreshing the Sequencer fills in the placeholder frames. This option also works with the Change Data/File operator to extend the range.

Length
Duration in frames of the inserted strip. This parameter is ignored when importing sequences, as their length matches the file count.

[Related references](INDEX.md).
