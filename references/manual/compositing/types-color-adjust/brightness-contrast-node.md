# Brightness/Contrast Node

## Brightness/Contrast Node

Brightness/Contrast node — Inputs: Image (standard color input); Brightness (an additive factor that raises overall brightness, negative to darken); and Contrast (a scaling factor that brightens bright pixels while keeping dark ones dark, higher values making details stand out, negative to reduce overall contrast). Output: Image (standard color output). Notes: this node can output values beyond the normal range (above one or below zero), so if you'll mix the output with normal-range images, clamp the values with the Map Value node (Min and Max enabled) or pass them through a Color Ramp node (with normal defaults) — either rescales them to normal range. In the example, intensifying the specular pass without clamping makes the specular pass's sub-one dark areas turn black when added to medium gray, while passing the brightened image through Map Value or Color Ramp gives the desired effect.

### Brightness/Contrast Node 

### Inputs 

Image
Standard color input.

Brightness
An additive adjustment to boost overall image luminance. Use negative values to reduce brightness.

Contrast
A scaling adjustment making bright areas brighter while preserving dark areas dark. Higher values emphasize detail. Use negative values to reduce overall contrast.

### Outputs 

Image
Standard color output.

### Notes 

Output may produce values outside standard range—exceeding 1.0 or below 0.0. For mixing with normal-range images, clamp values using the Map Value node (with Min and Max active) or pass through a Color Ramp node (standard defaults).

Clamp the values to normal range. 

Both approaches rescale values to standard boundaries. In our example, we isolate and intensify the specular pass. Without clamping (bottom path), the specular contribution falls below 1.0 in dark regions, turning dark gray when combined with medium gray. Applying either Map Value or Color Ramp recovers the desired effect.

### Example 

A basic example.

[Related references](INDEX.md).
