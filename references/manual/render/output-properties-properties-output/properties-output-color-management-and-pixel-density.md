# Output: Color Management, Pixel Density, Encoding

### Color Management 

This panel controls how Color Management is applied when saving images.

Follow Scene :

Applies the same color settings defined in the active Scene. These options are specified in the Render Settings.

Override :

Uses bespoke color management settings defined below in this panel, disregarding scene-level color settings.

For complete information about color management options, consult the Color Management page.

### Pixel Density 

The pixel density (commonly called PPI or DPI) specifies the intended physical dimensions for an image. This proves valuable for print output or sizing in document layout programs.

The X/Y density calculation incorporates the render X/Y aspect ratio, making these parameters useful for storing the aspect ratio of non-square pixels.

Pixel-density functions as metadata without impacting image resolution.

See also

Pixel Density support for image formats

### Encoding 

Reference

Panel :

Properties ‣ Output ‣ Encoding

Encoding panel. 

Configure video container, codec, and compression parameters here. These compression choices involve trade-offs between storage size, cross-platform compatibility, and video quality. Use the presets in the header to quickly apply optimal settings for that output type.

Tip

Access the System Console to monitor encoding process output. More detailed output is visible when running Blender as blender -d .

Container
Video container or file format. Consult video formats for all available options.

Autosplit Output
For videos exceeding 2GiB, activate Autosplit Output. Output will automatically split into multiple files once the first file reaches 2GiB.

[Related references](INDEX.md).
