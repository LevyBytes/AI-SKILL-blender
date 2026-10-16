# RGB Curves Node: Inputs, Properties, Outputs, Examples, Color Correction using Curves, Color Correction using Black/White Levels, Effects

### Inputs 

Image/Color
Standard color input.

Factor
The degree of node influence on the image.

Black Level Compositor Only
The input color mapped to black.

White Level Compositor Only
The input color mapped to white.

Tip

Use the eyedropper when identifying black and white levels. Sample colors from displayed image output.

### Properties 

Tone Compositor Only

Standard :

The shared curve applies independently to each channel, potentially causing hue shifts.

Filmlike :

Maintains hue consistency.

Channel
The curve to display.

C :

Combined

R :

Red

G :

Green

B :

Blue

Curve
A Bézier path mapping input (X axis) to output (Y axis). See Curve widget for controls.

### Outputs 

Image/Color
Standard color output.

### Examples 

Common curves achieving frequent outcomes follow.

From left to right: 1. Lighten shadows 2. Negative 3. Decrease contrast 4. Posterize. 

### Color Correction using Curves 

Color correction with curves. 

In this example, an image has excessive red. We employ an RGB Curves node to reduce the Red channel.

The Mix Color Node documentation features another overexposure-correction example.

### Color Correction using Black/White Levels 

Color correction with Black/White Levels. 

Manual curve adjustment for correction presents challenges. Black and White Levels offer an alternative approach, potentially their primary utility.

Here, the White Level is calibrated to a bright sand area, and the Black Level to the fish eye interior. For efficiency, display the input image in the Image Editor. Use the levels' picker to select directly from displayed content, zooming to pixel precision as needed.

Fine-tuning proceeds with R, G, B curves as in the prior example.

The C curve compensates for heightened contrast from Black/White Level adjustments.

### Effects 

Changing colors by inverting the red channel.

[Related references](INDEX.md).
