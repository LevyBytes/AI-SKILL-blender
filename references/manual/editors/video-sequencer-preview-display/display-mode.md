# Display Mode

## Display Mode

This pop-up lets you switch between showing the preview image and showing a scope that visualizes its color distribution.

Image Preview: previews the final video's look and lets you change the image layout with the various tools.

Luma Waveform: this scope plots the image's luminosity (brightness) distribution, so you can tell at a glance whether there's enough contrast and whether any areas are under- or overexposed. It works by drawing a curve for each scanline of the current video frame; put another way, each pixel column of the luma waveform is a brightness histogram of the matching pixel column in the frame. Specifically:
- A waveform pixel's horizontal position refers to a pixel column in the frame.
- A waveform pixel's vertical position refers to a brightness value, 0 at the bottom up to 1 at the top.
- A waveform pixel's brightness shows how many pixels in that frame column carry that brightness; with none, the waveform pixel is black, and with at least three, it's white.
When this scope is active, you get one option under Sidebar ‣ View ‣ View Settings. The examples show two images and their luma waveforms: in the first, the waveform's horizontal lines line up with the picture's uniform-colored lines (the one-pixel "gray 20%" line inside the yellow strip reads as a gray line, the two lines forming an "X" come from the two monochrome gradients, and the broken line matches the colored gradient at the bottom); in the second the curves are clear, with a luma of 80–100% for the sky, around 40% for the sea, and 10–20% for the mountains, rising near 40% on the sunny part.

RGB Parade: shows three waveforms, one each for the red, green, and blue channels, instead of a single one for overall brightness.

Chroma Vectorscope: plots the image's color distribution, each point carrying an angle for its hue, a distance-from-center for its saturation, and a brightness for how many frame pixels share that hue and saturation.

Histogram — shows three overlapping graphs, one per channel; within each, the X axis runs from 0 at the left (black) to 1 at the right (fully red/green/blue) for color intensity, and the Y axis is the pixel count. Use it to balance an image's tonal range — a well-balanced image shows a nice smooth spread of color values.

[Related references](INDEX.md).
