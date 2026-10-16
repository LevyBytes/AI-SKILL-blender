# Introduction

### Introduction

Define materials, lights and backgrounds using shading node networks. These nodes output values, vectors, colors, and shaders.

### Shaders

The shader socket is a core concept: surface and volume shaders output a shader—a description of lighting interaction—not a surface color. The renderer uses this to compute all light interactions for direct lighting and global illumination.

**Shader types:**

- **BSDF shader** — Describes reflection, refraction and absorption at surfaces.
- **Emission shader** — Describes surface or volumetric light emission.
- **Volume shader** — Describes volumetric light scattering.
- **Background shader** — Describes environmental light emission.

Each shader node has a color input and outputs a shader. Mix and Add Shader nodes combine them; no other operations are allowed. The resulting output feeds the renderer's light computation.

See also: Shaders

### Textures

Blender provides built-in procedural texture nodes. No texture data-blocks are needed; node groups handle texture reuse.

For UV mapping and texture painting in the 3D Viewport, use the Image Texture node. When set as active, it displays in the viewport using Texture color mode—useful for previewing painted textures.

Default coordinates are Generated for most nodes, except Image textures (which default to UV). Each node includes options to modify texture mapping and output color, editable in texture properties.

See also: Textures

### More

Vector Nodes, Color Nodes, and Utilities Nodes cover geometric data, texture coordinates, shader layering, and non-physical tricks.

### Open Shading Language

Cycles supports custom nodes via Open Shading Language.

[Related references](INDEX.md).
