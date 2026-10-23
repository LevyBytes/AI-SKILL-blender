# Color Ramp Node

## Color Ramp Node

The Color Ramp node maps values to colors through a gradient. Input: Factor (the value to map — 0.0 gives the leftmost color, 1.0 the rightmost). Properties: Color Ramp (see the Color Ramp Widget). Outputs: Image/Color (standard color output) and Alpha (standard alpha output). Examples — Creating an alpha mask: an overlooked use is turning a black-and-white image into a colored one with transparency — feed a black-and-white swirl (lacking alpha) into Color Ramp as the Factor, set the left end fully transparent and the right fully red, and the node outputs an image transparent where the input is black and opaque where it's white. Colorizing an image: add several colors to the gradient to turn a black-and-white image into a flaming swirl — gray shades map to blue, yellow, and red (all opaque), so black becomes blue (the first stop), grays become corresponding gradient colors, and white becomes red.

The Color Ramp Node maps values to colors through a gradient.

Inputs:
Factor: the value to map; 0.0 gives the leftmost color, 1.0 the rightmost.

Properties:
Color Ramp: see Color Ramp Widget.

Outputs:
Image/Color: the usual color output.
Alpha: the usual alpha output.

Examples:
Creating an Alpha Mask: an easily missed use of the Color Ramp is turning a black-and-white image into a colored, partly transparent one. In the example a black-and-white swirl lacking an alpha channel feeds the Color Ramp as a Factor; the ramp is fully transparent at its left end and fully red at its right, so (as the Viewer node shows) it outputs an image transparent where the input is black and opaque where it's white.
Colorizing an Image — here several colors are added to the gradient, turning a black-and-white image into a flaming swirl. The input's grays map to three fully opaque colors — blue, yellow, red: black areas become blue (the first stop), gray areas become a matching gradient color (bluish through yellow to reddish), and white areas become red.

The Color Ramp node maps scalar values to colors via a gradient.

Factor: The value to translate (0.0 = left color, 1.0 = right).

Color Ramp: See Color Ramp Widget.

Image/Color: Color output.
Alpha: Alpha output.

A common technique: convert a black-and-white image (without alpha) to a colored, transparent result.

In this case, a grayscale swirl (lacking alpha) feeds the Color Ramp as Factor. The gradient runs from transparent (left) to opaque red (right). The Viewer output shows: transparent where black, opaque where white.

Another approach: layer multiple colors onto a grayscale image.

Here, blue-yellow-red span the gradient, converting grayscale to color. Black maps to blue (first stop), gray to intermediate tones, white to red (last stop).

### Color Ramp Node 

The Color Ramp Node maps numeric values to colors utilizing a gradient.

### Inputs 

Factor
The numeric input to map. Zero yields the gradient's left color; 1.0 yields the right.

### Properties 

Color Ramp
See Color Ramp Widget.

### Outputs 

Image/Color
Standard color output.

Alpha
Standard alpha output.

### Examples 

### Creating an Alpha Mask 

A common, underutilized application of Color Ramp converts monochrome imagery into colored, transparent output.

Our example begins with a black-and-white swirl, lacking an alpha channel. The Color Ramp accepts this as input Factor.

The gradient spans from transparent (left edge) to opaque red (right edge). The Viewer node shows the result: transparent in black regions and fully visible where the input is white.

### Colorizing an Image 

A second example assigns multiple gradient colors, converting grayscale into vibrant flames.

Input gray levels map to three hues—blue, yellow, red—all completely opaque. The Color Ramp substitutes blue at black input, progresses through the gradient for gray tones, and outputs red at white.

[Related references](INDEX.md).
