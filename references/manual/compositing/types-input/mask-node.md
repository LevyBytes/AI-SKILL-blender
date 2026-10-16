# Mask Node

## Mask Node

The Mask node selects a Mask data-block, usable with other nodes (to Invert, Multiply, or Mix, or as a factor input). Inputs: Feather (use or ignore the feather points defined for splines; see Mask Feathers) and Size Source (where the mask gets its aspect/size — Scene Size, giving the scene render resolution and scaling with it; Fixed, a fixed pixel size; or Fixed/Scene, a pixel size that still scales with the render-resolution percentage). Motion Blur (for animated masks, built from surrounding frames): Samples (the motion-blur sample count, higher being smoother and more accurate but slower) and Shutter (the motion-blur duration in seconds, matching the per-frame exposure). Properties: Masks (the selectable mask data-block — if its label is blank, the mask name is used). Output: Mask (the black-and-white mask output). Example: the Mask node isolates an object from the background to keep it from being corrected.

[Related references](INDEX.md).
