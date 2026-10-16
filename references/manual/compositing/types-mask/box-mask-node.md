# Box Mask Node

## Box Mask Node

The Box Mask node makes an image suitable for a simple matte. Inputs: Mask Type, the operation against the input mask — Add (the union: the generated mask's area is set to the given Value, while the rest of the input mask passes through unchanged, or black if there's no input mask), Subtract (the given Value is taken away from the input mask's values), Multiply (the intersection: the input mask is multiplied by Value within the generated area, and everything else becomes black), or Not (areas in both masks become black; generated-mask areas that are black on the input become Value; areas the generated mask doesn't cover stay unchanged); Mask (an optional base mask for the operations); Value (the generated mask's intensity); Position (the box center as a fraction of width or height — 0.5, 0.5 centers it, 0.0, 0.0 puts it lower-left); Size (the box's width/height as a fraction of the total image width); and Rotation (the box's rotation about its center). Output: Mask (a rectangular mask merged with the input mask, at the current scene render dimensions). Tip: for soft edges, pass the output through a slight Blur node.

[Related references](INDEX.md).
