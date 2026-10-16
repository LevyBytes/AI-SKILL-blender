# Bokeh Image Node

## Bokeh Image Node

The Bokeh Image node makes a special input image for the Bokeh Blur filter node — a reference image simulating optical parameters like aperture shape and lens distortions that strongly affect real-camera bokeh. Inputs (the first three simulate the camera aperture): Flaps (an integer number of iris-diaphragm blades), Angle (an angular offset for those blades relative to the image plane), Roundness (the blade curvature from 0, straight, to 1, a perfect circle), Catadioptric Size (a mirror-lens/telescope distortion useful for visually complex bokeh), and Color Shift (chromatic aberration in the blur, as from a tilt-shift lens). Output: Image (the generated bokeh image).

[Related references](INDEX.md).
