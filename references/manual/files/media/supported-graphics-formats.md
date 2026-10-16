# Supported Graphics Formats

## Supported Graphics Formats

Image Formats — these image file formats are supported internally by Blender:
- JPEG — 8bit; Alpha ✗; Metadata ✓; DPI ✓; .jpg .jpeg
- OpenEXR — float 16, 32bit; Alpha ✓; Metadata ✓; DPI ✓; .exr
- PNG — 8, 16bit; Alpha ✓; Metadata ✓; DPI ✓; .png
- WebP — 8bit; Alpha ✓; Metadata ✓; DPI ✗; .webp
- AVIF — 8, 10, 12bit; Alpha ✓; Metadata ✗; DPI ✗; .avif
- BMP — 8bit; Alpha ✓; Metadata ✗; DPI ✓; .bmp
- Cineon — 8, 10, 12, 16bit; Alpha ✓; Metadata ✗; DPI ✗; .cin
- DPX — 8, 10, 12, 16bit; Alpha ✓; Metadata ✗; DPI ✗; .dpx
- Iris — 8, 16bit; Alpha ✓; Metadata ✗; DPI ✗; .sgi .rgb .bw
- JPEG 2000 — 8, 12, 16bit; Alpha ✓; Metadata ✗; DPI ✗; .jp2 .jp2 .j2c
- Radiance HDR — float; Alpha ✓; Metadata ✗; DPI ✗; .hdr
- Targa — 8bit; Alpha ✓; Metadata ✗; DPI ✗; .tga
- Targa Raw — 8bit; Alpha ✓; Metadata ✗; DPI ✗; .tga
- TIFF — 8, 16bit; Alpha ✓; Metadata ✗; DPI ✓; .tif .tiff
Hint: if the technical detail doesn't interest you, a good rule for picking an output format is — OpenEXR if you'll composite or color-grade the images, PNG for on-screen output or encoding into multiple video formats, JPEG for on-screen output where file size matters and some quality loss is fine. All of these support compression, which can matter when rendering animations.
Hint: image bit depths give these many tonal levels per channel — 8: 256 levels; 10: 1024 levels; 12: 4096 levels; 16: 65536 levels.

Opening Images:
Relative Path — sets the file path relative to the open blend-file (see Relative Paths).
Detect Sequences — auto-hunts for image sequences in the chosen images (by file name); switch it off when you really do want single images that belong to a sequence (see Opening an Image Sequence).
Detect UDIMs — auto-hunts for UDIM tiles in the chosen image's directory and loads any matches as UDIMs; it works by spotting a .xxxx (a four-digit number) ahead of the file extension.
Opening an Image Sequence — to load a sequence in any supported format, the filenames must hold a digit marking the frame order (e.g. *-0001.jpg, *-0002.jpg, *-0003.jpg, of any format), which sets the frame. Open it by selecting the images one of these ways and confirming with the Open Image button or Return:
Range — browse into the directory and LMB-drag over a span of names to highlight several; you can page down and keep Shift-LMB-dragging to add more.
Batch — Shift-LMB unrelated stills for batch processing; each image becomes one frame, in sort order, and they can mix file types (jpg, png, exr, etc.).
All — press A to select/deselect every file in the directory.

Saving Images:
File Format — pick the image format to save to; the chosen format determines which other options (channels, bit depth, compression level) appear.
Color — the color format to save the image or video in; some formats use it to trim how much data is written. RGBA isn't available for every format — check the list above. BW (grayscale), RGB (red, green, blue channels), or RGBA (red, green, blue, alpha channels).
Color Depth — the bit depth per color channel, setting how many color values can be represented; higher depths cut color banding and improve precision but grow file size and memory, and not every format supports every depth. 8 (the common choice for on-screen graphics, web, and standard video), 10/12/16 (used by photography and digital-cinema formats like DPX and JPEG 2000, with more tonal range than 8-bit), 32 (32-bit float per channel — the highest precision and dynamic range, mainly for OpenEXR VFX and compositing), Float (Half) (16-bit float per channel — high dynamic range at lower memory/storage cost, OpenEXR only), or Float (Full) (32-bit float per channel — highest precision and dynamic range, OpenEXR only). Note: internally Blender works only in 8-bit or 32-bit, so images above 8-bit precision (10-, 12-, 16-bit) convert to 32-bit float on load.
Compression — shrinks the image file's size, by a method that varies with the format and settings.
Quality — the amount of lossy compression applied, as a percentage; lossy compression shrinks file size by dropping some image data, which can cost detail. 0% means maximum compression — smallest files, most obvious quality loss; 100% means none — full quality at a larger file size.
Save As Render — saves the image with render color management: for display formats like PNG it applies the view and display transform, and for intermediate formats like OpenEXR it uses the default render output color space.

Copy — sets whether the data-block will reference the newly created file, or leave the reference unchanged and keep it on the original.
Color Space — names the color space of the source file. The list depends on the active OCIO config; the defaults are detailed under Default OpenColorIO Configuration. Note: the Cineon, DPX, OpenEXR, and Radiance HDR types are saved in a linear color space by default.

Format Details:
Cineon & DPX — Cineon is Kodak's film-scanning standard, 10 bits per channel and logarithmic. DPX, derived from Cineon, became the ANSI/SMPTE industry standard; it supports 16-bit colors/channels, linear or logarithmic, and is a widely adopted standard in the film hardware/software industry. Both DPX and Cineon only store and convert the "visible" color range of values between 0.0 and 1.0 (the result of rendering or compositing).
OpenEXR — ILM's OpenEXR is now a software-industry standard for HDR image files, largely thanks to its flexible, expandable structure. An OpenEXR file can hold multiple layers and passes, so OpenEXR images load into a Compositor with their render layers and passes intact. Note: when opening OpenEXR images, Blender sets the Color Space automatically if it detects Linear CIE-XYZ E or ACES2065-1.
Output Options — available for OpenEXR render output:
Color Depth — the base-two exponent for how many colors fit in one channel; a higher bit depth allows more colors, cutting banding and raising precision, but grows memory use exponentially. Float (Half) (a custom 16 bits per channel in floating point, which trims the effective bit depth to 10-bit — a 5-bit power value plus a 1-bit sign) or Float (Full) (32 bits per channel in floating point).
Codec — the compression used to encode the EXR-file. None (no compression — fastest encoding, biggest files), ZIP (lossless Zlib on 16-row blocks), PIZ (lossless wavelet, good for noisy/grainy images), DWAA (lossy) (JPEG-like lossy on 32-row blocks), DWAB (lossy) (JPEG-like lossy on 256-row blocks), HTJ2K (lossless, based on high-throughput JPEG 2000 — smaller files but new and not widely supported yet), ZIPS (lossless Zlib, each row compressed on its own), RLE (lossless run-length, good when rows share values), Pxr24 (lossy) (converts 32-bit floats to 24 bits then deflates — lossless for half and 32-bit integer data, slightly lossy for 32-bit float), B44 (lossy) (lossy for 16-bit float images at a fixed 2.3:1 ratio, compressing uniformly regardless of content), or B44A (lossy) (like B44 but with extra compression on flat-color areas such as alpha).
Quality (DWAA (lossy), DWAB (lossy)) — the amount of lossy compression applied, as a percentage; lossy compression shrinks file size by dropping some image data, which can cost detail. 0% means maximum compression — smallest files, most obvious quality loss; 100% means none — full quality at a larger file size.
Interleave — uses the legacy interleaved storage of views, layers, and passes for compatibility with apps that can't read the more efficient multi-part OpenEXR files.
Preview — when rendering an animation (or single frames from the command line), it saves a JPEG copy of the image as a quick preview.
Radiance HDR — Radiance is a toolkit for lighting simulation; since it had the first (and long the only) HDR image format, many other packages support it. Radiance .hdr files store colors in 8 bits per component plus a shared 8-bit exponent, making 32 bits per pixel.

Metadata — metadata is extra information stored inside an image file describing how it was made or how it should be read. Blender can write metadata into supported formats when enabled in the Output Properties.
Limitations — not every format supports metadata, and some support only a limited subset of fields; with formats that don't support it, render information isn't preserved in the saved file.
Orientation Metadata — EXIF orientation metadata (common in JPEG images) is ignored when loading into Blender, so images display from their stored pixel data without automatic rotation; if one looks wrongly rotated, fix it by hand with Rotate 90° Clockwise.

[Related references](INDEX.md).
