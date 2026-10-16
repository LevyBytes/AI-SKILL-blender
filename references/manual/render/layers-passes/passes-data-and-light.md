# Passes: Data, Light

## Passes

### Passes

Reference

Panel :

Properties ‣ View Layer ‣ Passes

A Pass is a type of intermediate rendering information that's extracted as a separate image. Examples include the diffuse colors of the objects in the scene, the light distribution, the depth map, and the normal map.

These images can be accessed using the Render Layers Node in the Compositor and combined in a custom way that replaces the standard one.

### Data

Include

Combined Cycles , EEVEE , Workbench
The render output before any compositing is applied.

Depth Cycles , EEVEE , Workbench
Distance to the nearest visible surface. Can be used with the Defocus Node for a fake Depth of Field effect.

Note

This pass produces noisy results if the render itself uses Depth of Field or motion blur. Use the Mist pass for a cleaner image.

Mist Cycles , EEVEE
Distance to the nearest visible surface, mapped to the 0.0 - 1.0 range. When enabled, settings become available in the World tab.

This pass can be used to fade out objects that are farther away. An alternative is using the Volume slot of the World Output shading node.

Position Cycles , EEVEE
Positions in world space.

Normal Cycles , EEVEE
Surface normals in world space.

Vector Cycles , EEVEE
Motion vectors for the Vector Blur Node. The four components consist of 2D vectors giving the screen-space motion based on the next and previous frames.

This pass is disabled when Motion Blur is enabled.

UV Cycles
The UV coordinates within each object's active UV map, represented through the red and green channels of the image. (The blue channel stores a constant value of 1 and does not hold any information.) Can be used with the Map UV Node.

Grease Pencil Cycles , EEVEE , Workbench
Outputs only the visible (non-occluded) strokes and fills from the Grease Pencil engine into a separate image layer.

This pass is useful for compositing workflows where you want to isolate, enhance, or apply effects to Grease Pencil elements separately from the rest of the render.

Note

For most scenes, blending this pass over the rest of the image using an Alpha Over node will reproduce the Combined render result. However, some blending modes in Grease Pencil can modify the chromaticity of the alpha channel. In these cases, compositing the Grease Pencil pass separately can produce different results.

Denoising Data Cycles
Includes Denoising Albedo , Denoising Normal , and the combined image before denoising. Can be used with the Denoise Node as a replacement for automatic denoising.

Indexes

Object Index Cycles
A map where each pixel stores the user-defined ID of the object at that pixel. This map can be converted into a mask for a particular object using the ID Mask Node.

Material Index Cycles
A map where each pixel stores the user-defined ID of the material at that pixel. This map can be converted into a mask for a particular material using the ID Mask Node.

Note

The Depth, Position, Object Index, and Material Index passes are not anti-aliased.

Debug

Render Time Cycles
An estimate for how long in milliseconds each pixel took to render. Note, this pass is not supported on GPU rendering.

Sample Count Cycles
Number of samples calculated for each pixel, divided by the maximum number of samples. Used to analyze adaptive sampling.

Alpha Threshold Cycles
The Depth, Position, Normal, Vector, UV, and Index passes are only affected by surfaces with an opacity equal to or higher than this threshold. With value 0.0, the first surface hit will always write to these passes regardless of opacity. With higher values, surfaces that are mostly transparent will be skipped until an opaque surface is encountered.

### Light

[Related references](INDEX.md).
