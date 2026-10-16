# Strip Properties: Compositing, Transform

## Strip Properties

### Strip Properties

Type
Strip classification, shown via icon.

Name
Text field for adjusting the strip identifier, displayed on the timeline.

Color Tag
Strips receive a Type-based default color; use the color tag to apply a custom color for organizational purposes.

Mute
Turn off to silence strip output.

### Compositing

Reference

Panel: Sidebar ‣ Strip ‣ Compositing

Blend
Blending strategy for combining the strip with lower-channel content. See Blend Modes for details.

Opacity
The transparency (alpha) value of the strip.

When animated, opacity displays as an overlay on the strip—a dark section following the animation curve. The F-Curves overlay can be hidden to remove this visualization.

### Transform

Reference

Panel: Sidebar ‣ Strip ‣ Transform

Filter
Method for calculating pixel values at non-integer image coordinates.

Auto:
Filter selection adapts to scaling factors.

- No scale/rotation/integer coords: Nearest

- Upscaling over 2x: Cubic Mitchell

- Downscaling over 2x: Box

- All else: Bilinear

Nearest:
Direct pixel matching without interpolation (lowest processing).

Bilinear:
Interpolates across a 2×2 grid.

Cubic Mitchell:
Cubic Mitchell on a 4×4 grid.

Cubic B-Spline:
Cubic B-Spline (smooth, minimal artifacts) on a 4×4 grid.

Box:
Averages source samples within destination pixels.

Position X, Y
Shifts the frames along horizontal and vertical axes.

Scale X, Y
Resizes along horizontal and vertical axes.

Rotation
Applies 2D rotation about the Z axis.

Mirror
Flips along the X (left-right) or Y (top-bottom) axis.

[Related references](INDEX.md).
