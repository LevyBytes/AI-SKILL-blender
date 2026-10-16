# Bokeh Blur Node

## Bokeh Blur Node

The Bokeh Blur node makes a bokeh-type blur similar to Defocus, but with an in-focus region defined in the Compositor and more flexibility in the blur type via the Bokeh Image node, plus performance optimizations like restricting the calculation area and masking. Inputs: Image (standard color input); Bokeh (an input for the Bokeh Image node); Size (the blur amount in pixels, either a single value over the whole image or a variable value from an input image); and Bounding Box (use a Box Mask matte node or a Mask input node to limit where the blur applies, handy for saving composite time while developing a node system by filtering only a small area per adjustment). Output: Image (standard color output). Examples: an ID-masked alpha image can blur a background while foreground objects stay in focus (use the Dilate Node to avoid strange edges); the Z pass can be visualized via a Map Range node and a Color Ramp node (then a multiply Math node so a blur value above one applies to objects outside the focal range); and a manually made grayscale image can define sharp and blurry areas of an existing image (again with a Multiply Node for a blur value above one).

[Related references](INDEX.md).
