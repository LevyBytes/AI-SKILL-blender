# Bump Node

## Bump Node

### Bump Node 

The Bump node generates perturbed surface normals from height data for bump mapping. Height is sampled at the shading location and adjacent surface points to compute local normal direction.

### Inputs 

Strength
Bump effect magnitude, interpolating between no effect and full effect.

Distance
Scalar multiplier applied to height values, controlling the overall bump scale.

Filter Width
Pixel-sized filter width applied when calculating bump direction. Default 0.1 enables subpixel stability for most textures. Larger filter widths on stepped textures simulate edge bevels.

This input accepts only constant values and does not spatially vary.

Height
Scalar height displacement at the shading location; link textures here.

Normal
Standard normal input.

### Properties 

Invert
Reverses bump direction to displace inward rather than outward.

### Outputs 

Normal
Standard normal output.

Tip

When Height is unconnected, the node passes through its Normal input unchanged, or defaults to geometric normal if unlinked. Feeding a node group input via a no-op Bump node before calculations defaults it to normal.

### Examples 

The setup above applies bump only to diffuse shading, creating the impression of a bumpy base finished with a smooth glossy layer.

[Related references](INDEX.md).
