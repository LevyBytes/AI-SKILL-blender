# Format

## Format

### Format 

Format panel. 

Many render presets provide common resolutions and frame rates for different displays and broadcast standards, available in the panel header.

Resolution X, Y
Horizontal and vertical pixel dimensions of the output.

Percentage
Adjustment slider for reducing or expanding rendered size relative to the Resolution settings. Useful for quick test renders at the same aspect ratio as the final output.

Aspect X, Y
Legacy televisions utilized non-square pixels, so this parameter adjusts pixel shape along each axis. Images are pre-distorted to appear stretched on computer displays but display correctly on TV sets. Using the correct pixel aspect ratio prevents re-scaling and associated quality loss.

Render Region
Restricts output to a portion of the view rather than the complete frame. See the Render Region documentation for defining region boundaries.

Crop to Render Region
Trims rendered output to match the render region size instead of rendering a transparent area around it.

Frame Rate
Frequency at which frames display per second, relevant for Animation. The menu includes standard frame rates, and custom rates can be set by selecting Custom to access these properties:

FPS
The frame rate expressed as frames per second.

Base
Certain standards require fractional frame rates, particularly NTSC. These are expressed as a fraction where the Base value becomes the denominator and the FPS becomes the numerator: \\(\\frac{FPS}{Base}\\) .

See also

Viewport Playback Frame Rate Limited

[Related references](INDEX.md).
