# ID Mask Node

## ID Mask Node

The ID Mask node makes a mask for a particular object or material in the render, relying on the Object Index or Material Index render pass available only with Cycles. (It's superseded by the Cryptomatte Node, which is more versatile and works in both Cycles and EEVEE.) Inputs: ID Value (the Object Index or Material Index pass — once enabled, reached via the IndexOB or IndexMA slot of the Render Layers Node) and Index (the index to mask, configured for objects at Properties ‣ Object ‣ Relations ‣ Pass Index and for materials at Properties ‣ Material ‣ Settings ‣ Pass Index), plus Anti-Aliasing (smooth the mask edges). Output: Alpha (a grayscale image, white where the object exists and black where it doesn't). Limitation: Volume Objects aren't supported.

[Related references](INDEX.md).
