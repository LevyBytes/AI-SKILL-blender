# Texture Slots

## Texture Slots

### Texture Slots

Texture Slots settings.

A "slot" represents the grouping of images paired with UV layers.

Choosing a Paint Slots or Canvas Image will also show the related image in the Image Editor.

Mode
The slot framework provides two painting approaches:

Material
This mode extracts slots from the material composition of the mesh.

In Cycles rendering, every Image Texture node in the material's node architecture is placed in the slots.

Active Paint Texture Index
Shows all available slots. Trigger a slot by LMB clicking for painting.

Single Image
Pick an image and painting applies using the active UV layer.

Image
Pick the image as your painting surface.

New
Establish a fresh image.

UV Map
Pick the UV mapping for painting. (Equivalent to the active UV map in the mesh's UV Maps settings.)

Texture Filter Type
Choose the texture sampling method. Choices: Linear or Closest.

Save All Images
Repack (or write if stored separately) every altered image. Same as in Image Editor.

Add Simple UVs
Creates a cube unwrap and arranges it. Custom unwrapping is still preferable.

This choice is available only when the object doesn't contain a UV Map yet.

[Related references](INDEX.md).
