# Supported Nodes: Input Nodes, Texture Nodes, Other Nodes

### Input Nodes

Ambient Occlusion
The Only Local option is unavailable.

Geometry
Pointiness is unavailable.

Random per Island
This feature is unavailable.

Attribute
Defaults to the active UV layer. Only density, color, flame, and temperature built-in attributes are supported. UVs and Color Attributes work. Up to 8 Object or Instancer attributes per material (combined), and 512 View Layer attributes per scene.

Bevel
Unsupported.

Curves Info
The Random output employs a different RNG algorithm. Ranges and statistical patterns match, but values differ.

Light Path
EEVEE lacks true ray concepts. To ease Cycles-to-EEVEE workflow transitions, certain outputs are supported in limited cases.

- Is Camera: Supported.
- Is Shadow: Supported.
- Is Diffuse: Set to 1.0 when baking light probe volumes; otherwise 0.0.
- Is Glossy: Set to 1.0 when baking light probe spheres or planes; otherwise 0.0.
- Is Singular: Not supported. Same behavior as Is Glossy.
- Is Reflection: Not supported. Same behavior as Is Glossy.
- Is Transmission: Not supported. Same behavior as Is Glossy.
- Ray Length: Not supported. Defaults to 1.0.
- Ray Depth: Not supported. Defaults to 0.0.
- Diffuse Depth: Partially supported. Set to 1.0 when baking light probe volumes; otherwise 0.0.
- Glossy Depth: Partially supported. Set to 1.0 when baking light probe spheres or planes; otherwise 0.0.
- Transparent Depth: Not supported. Defaults to 0.
- Transmission Depth: Not supported. Same as Glossy Depth.

Note
Is Glossy does not work with Screen Space Reflections/Refractions but works with reflection planes.

Particle Info
Unsupported.

Texture Coordinate
From Instancer is not supported.

UV Map
From Instancer is not supported.

Wireframe
Pixel size output differs slightly from Cycles; line width may vary due to hardware rasterization.

### Texture Nodes

Most texture nodes are supported except as follows:

IES Texture
Unsupported.

Image Texture
Smart Interpolation always applies Cubic mode. Artifacts occur using Tube or Sphere projection with linear interpolation due to hardware mip-mapping and anisotropic filtering. Tube/Sphere artifacts also appear when texture coordinates lack continuity. Box projection with Clip or Extend modes is unsupported and reverts to Repeat.

Point Density
Unsupported.

Sky Texture
Nishita mode does not support the Sun Disc property.

### Other Nodes

Light Falloff
Unsupported.

[Related references](INDEX.md).
