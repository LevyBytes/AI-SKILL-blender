# Normal Map Node

## Normal Map Node

### Normal Map Node 

The Normal Map node generates perturbed normals from RGB-encoded normal map textures. Usually chained with an Image Texture node for the color input specifying the map image. For tangent-space maps, UV coordinates must align with the image, and Non-Color mode is required for correct interpretation.

### Inputs 

Strength
The normal mapping intensity.

Strength is set to 0, 0.5, 1, 2 (from left to right). 

Color
RGB data encoding the normal in the designated space.

### Properties 

Space
Three spaces are available for the RGB data: Tangent, Object, and World. Tangent space is most prevalent, supporting transformations and mesh deformations. Object space maps maintain surface alignment through transformations but shift under object scaling. World space maps ignore both.

Convention
Blender defaults to OpenGL, where the green channel's Y points up. DirectX convention (Y pointing down) accommodates maps from external tools.

Base Cycles Only
Surface serving as the normal map base when displacement is combined.

Original Base :

The smooth, unmodified base normal and tangents, coordinating with aligned displacement.

Displaced Base :

The displaced normal and tangents, applying normal mapping on top.

UV Map
The UV set supplying tangent calculation data. Should match the UV used by any linked Image Texture node.

### Outputs 

Normal
Normal output compatible with BSDF inputs.

### Example 

The Normal Map Strength is set to 1.

[Related references](INDEX.md).
