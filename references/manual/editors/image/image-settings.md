# Image Settings

## Image Settings

Source — pick the kind of image to use; for file-based images, see Supported Graphics Formats.
Single Image — one static image.
Image Sequence — an animation with each frame in its own file (see Opening an Image Sequence; for options, see Movie below).
Movie — a video file. If your aim is motion tracking and video compositing rather than just using the footage as a texture, load it into the Movie Clip Editor instead.
  Note: the options below only affect the preview, not the 3D Viewport or the render — for those, see the Image Texture Node.
  Note: Blender plays every video at the scene frame rate rather than the clip's own, so a mismatch makes them run faster or slower than intended; the Image Texture Node's Offset field (linked above) is the workaround.
  Frames — how many of the video's frames to play; past that point it pauses unless Cyclic is on.
  Match Movie Length — sets Frames to the count in the video file.
  Start — the scene frame at which the video begins playing.
  Offset — how many frames to shift the video earlier in time (equivalently, how many frames to skip at its start).
  Cyclic — loops back to the beginning after the last frame for a continuous cycle.
  Auto Refresh — plays the video in the Image Editor while the scene animation runs (the pointer must be over the Image Editor or the Timeline when you start playback).
  Deinterlace — applies deinterlacing to interlaced (analog) video.
Generated — an image Blender creates.
  X, Y — the image's pixel width and height.
  Float Buffer — makes a 32-bit image; it's larger but holds far more color information than the standard 8-bit one, which can help for close-ups and broad gradients.
  Type — Blank (a single specified color), UV Grid (a checkerboard with a colored cross in each square), or Color Grid (a busier colored grid lettered and numbered by location, useful for spotting stretching or distortion in the UV mapping).
  Color — the fill color for a Blank image.

Common Options:
File — used to replace or pack files.
Pack — embeds the resource into the current blend-file (see Packed Data).
Path — the path to the linked file.
Open — opens the File Browser to choose a file from a drive.
Reload — reloads the file, handy after it's been reworked in another application.
Use Multi-View — see Multi-View.
Color Space — names the Color Space the file was saved in, which Blender uses to convert the image correctly into its internal linear color space (used for all color math and rendering). Textures and final renders are often sRGB, while OpenEXR images are linear; images that don't really hold "colors" — normal, bump, or stencil maps — should never be color-converted, so set those to Non-Color. The available color spaces depend on the active OCIO config; the defaults are detailed under Default OpenColorIO Configuration.
Alpha — how the image treats its Alpha Channel; shown only when the format supports transparency.
  Straight — stores RGB and alpha separately with alpha acting as a mask (unassociated alpha), common in image editors and formats like PNG; it preserves color where alpha is zero.
  Premultiplied — stores RGB with alpha multiplied in (associated alpha), the natural format for renders and formats like OpenEXR; unlike straight alpha it can represent purely emissive effects such as fire correctly.
  Channel Packed — different images occupy the RGB and alpha channels and shouldn't affect each other; game engines often channel-pack to save memory.
  None — ignores the file's alpha and treats the image as fully opaque.
Half Float Precision — loads the image at 16 bits per channel instead of 32 to save memory.
View as Render — applies the color-management settings when showing this image on screen.
Seam Margin — the width of the margin around UV islands for texture painting to bleed into, ensuring no unpainted pixels are left at an island's border. A stroke crossing a seam in 3D extends past the UV island edges in the texture until it's cut off at the margin. Higher values give a thicker margin, useful if you'll make mipmaps of the texture, though it can slow painting. Note: this affects only Sculpt Mode, where texture painting is still experimental; Texture Paint Mode uses a fixed margin.

[Related references](INDEX.md).
