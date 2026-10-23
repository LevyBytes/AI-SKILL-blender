# RGB Curves Node: The RGB Curves Node adjusts levels on each color channel., Inputs

## RGB Curves Node

The RGB Curves node makes level adjustments on each color channel. Inputs: Image/Color (standard color input); Factor (how much the node influences the image); Black Level (Compositor only — the input color mapped to black); and White Level (Compositor only — the input color mapped to white) — and to set the black and white levels, use the eyedropper to sample a color from a displayed image. Properties: Tone (Compositor only) — Standard (the Combined curve applied to each channel individually, which can shift hue) or Filmlike (keeps hue constant); Channel (which curve to show — C Combined, R Red, G Green, B Blue); and Curve (a Bézier curve mapping each input level on X to an output level on Y; see the Curve widget). Output: Image/Color (standard color output). Examples: common curves include lightening shadows, negative, decreasing contrast, and posterize. Color correction with curves: for an image with too much red, run it through RGB Curves and reduce the Red channel (the Mix Color Node docs have an example about fixing overexposure). Color correction with Black/White Levels: since manually adjusting the curves can be hard, the Black and White Levels are another option (really their main purpose) — set the White Level to a bright sand spot in the background and the Black Level to the center of the fish's eye, ideally with the Image Editor showing the original input so you can use the levels' color picker (zooming to pixel level if needed), then fine-tune with the R, G, B curves, using the C curve to compensate for the contrast increase that setting Black and White Levels causes. Effects: change colors by inverting the red channel.

The RGB Curves Node adjusts levels on each color channel.

Inputs:
Image/Color: the usual color input.
Factor: how much sway the node has over the image.
Black Level (Compositor Only): sets the input color that should map to black.
White Level (Compositor Only): sets the input color that should map to white.
Tip: to set the black and white levels, use the eyedropper to grab a color sample from a displayed image.

Properties:
Tone (Compositor Only): Standard (the Combined curve hits each channel on its own, which may shift hue) or Filmlike (holds the hue steady).
Channel - which curve to show: C (Combined), R (Red), G (Green), B (Blue).
Curve: a Bézier curve mapping each input level (X axis) to an output level (Y axis); for the controls, see Curve widget.

Outputs:
Image/Color: the usual color output.

Examples: below are some common curves for desired effects, from left to right: 1. Lighten shadows, 2. Negative, 3. Decrease contrast, 4. Posterize.
Color Correction using Curves: in this example the image is too red, so we run it through an RGB Curves node and pull the Red channel down. The Mix Color Node's docs have an extra example on fixing overexposure.
Color Correction using Black/White Levels: adjusting the RGB curves by hand for color correction can be fiddly; another route is the Black and White Levels, which may well be their real purpose. Here the White Level is set to a bright spot of sand in the background and the Black Level to the center of the fish's eye. To do this efficiently, bring up the Image Editor showing the original input image and use the levels' color picker to grab the right colors, zooming to pixel level if needed; fine-tune with the R, G, and B curves as before. The C curve compensates for the extra contrast that setting Black and White Levels brings.
Effects: changing colors by inverting the red channel.

The RGB Curves node adjusts each color channel independently.

Image/Color: Standard input.
Factor: Blend strength.

Black Level (Compositor only): Input color mapped to black.
White Level (Compositor only): Input color mapped to white.

Tip: Use the eyedropper on displayed images to set levels.

Tone (Compositor only):

Standard: Combined curve applied per-channel (may shift hue).
Filmlike: Hue stays constant.

Channel: Which curve to display (C = Combined, R = Red, G = Green, B = Blue).

Curve: Bézier curve mapping input (X) to output (Y). See Curve widget for controls.

Image/Color: Standard output.

Common curve shapes, left to right: Lighten shadows, Negate, Reduce contrast, Posterize. 

Color correction by reducing red:

The image has excess red. Run it through RGB Curves and dial back the Red channel.

The Mix Color Node documentation covers fixing overexposure.

Alternative approach: Black/White Level.

Manually tweaking RGB curves is tricky. Black and White Levels offer another route. Set White Level to a bright reference (e.g., sand), Black Level to a dark one (e.g., an eye). Using the level pickers on the input image makes this efficient. Fine-tune afterward with R, G, B curves. Use the C curve to offset contrast changes from the level adjustments.

Curve Color correction with Black/White Levels. 

Effect: Inverting the red channel.

### RGB Curves Node 

The RGB Curves Node adjusts tonal levels within each color channel.

[Related references](INDEX.md).
