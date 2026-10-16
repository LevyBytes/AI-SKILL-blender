# Introduction

### Introduction

The act of rendering converts a three-dimensional scene representation into a two-dimensional image.
Blender supplies three distinct rendering engines, each optimized for particular use cases:

- EEVEE provides a physically accurate real-time rendering solution.

- Cycles implements a physically accurate path-tracing renderer.

- Workbench focuses on tasks involving spatial arrangement, surface geometry, and display preview.

Third-party suppliers make additional renderers available through add-ons.
Each engine offers its own set of configuration options to govern output fidelity and speed.

Cameras, lights, and material definitions set the visual characteristics of a render.
These fundamental elements are shared by both EEVEE and Cycles, though specific capabilities exist only on one or the other platform.

Rendering can be segmented into component layers and intermediate data streams that compose individually for artistic variation or blending with external imagery. Non-photorealistic edge stylization can be added via freestyle.

Blender enables real-time 3D display rendering through all engine variants, supporting fast experimentation with illumination and surface properties. Following interactive refinement, final-quality output or animation can be rendered and stored.

[Related references](INDEX.md).
