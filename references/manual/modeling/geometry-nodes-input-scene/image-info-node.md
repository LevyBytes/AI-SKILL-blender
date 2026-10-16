# Image Info Node

### Image Info Node

The Image Info node outputs image and animation parameters. Useful for generating geometry-node parameters from arbitrary image data. Information is either general (whole image) or frame-specific.

### Inputs

Image
Source image to query.

Frame
Frame index (for frame-specific outputs).

### Outputs

Width
Pixel count along X axis. Frame-specific.

Height
Pixel count along Y axis. Frame-specific.

Has Alpha
Boolean: true if the transparency channel differs from 1 for any pixel in this frame. Frame-specific.

Frame Count
Total frames in the image or sequence (always 1 for static images).

FPS
Frames per second (always 0 for static images).

[Related references](INDEX.md).
