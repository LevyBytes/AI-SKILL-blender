# Introduction

### Introduction

EEVEE functions as Blender's real-time rendering engine, optimized for rapid, responsive output while achieving PBR material goals. Simultaneously interactive in the 3D Viewport and capable of generating refined final renders.

EEVEE materials employ identical shader nodes as Cycles, streamlining scene porting. For Cycles artists, EEVEE accelerates material prototyping in real-time.

EEVEE rests on rasterization rather than path tracing. Instead of computing every light ray, rasterization identifies camera-visible surfaces, then approximates light interactions using various algorithms. While EEVEE embraces PBR ideas, Cycles remains more physically faithful. Consequently, EEVEE carries specific constraints.

EEVEE final render – "Temple" by Dominik Graf.

Introduction: Freestyle NPR Engine

Freestyle is an edge/line-based non-photorealistic (NPR) rendering system. It leverages mesh data and Z-depth to draw lines on chosen edge types. Varied line styling produces artistic (hand-drawn, painted, etc.) or technical (hard-line) visuals.

Freestyle supports rich stylization diversity. Two methods define line appearance. First: parameter-based Line Style creation, allowing intuitive editing of dotted lines and straightforward multi-line type setup. Style modifiers expand possibilities limitlessly. Second: Python scripting for advanced stylization. Blender includes pre-made styles like Japanese big brush, cartoon, blueprint, and thickness-with-depth.

| ATV buggy by Rylan Wright (RONIN). . (File:AtvBuggy.zip) | By mato.sus304. -SA. (File:Mato_sus304_cut02.zip) |
| --- | --- |
| Cartoon scene from OHA Studio © Mechanimotion Entertainment. (blend-file) | Blueprint render of Martin M-130 from 1935 by LightBWK. CC0. Warning: heavy file; stress tests Blender and may crash. Designed for limits testing. (File:M-130Blueprint.zip) |

### The Big Picture

- Toggle Freestyle via Properties ‣ Render ‣ Freestyle checkbox.
- Freestyle options reside in View Layer properties.
- Each view layer has one view map. A view map holds edge detection parameters (Crease Angle, Culling toggle, Face Smoothness toggle, Material Boundaries toggle, Sphere Radius, Kr Derivative Epsilon advanced options).
- A view map can hold multiple Line Sets.
- A line set determines which line types and selections render from your scene.
- Each line set links to one line style (shareable across multiple Line Sets).
- A line style tells Freestyle how to render linked Line Sets regarding color, alpha, thickness, and other traits.

Block diagram of Freestyle view map and processes.

### Known Limitations

- Memory intensive: All view layer mesh objects load simultaneously.
- Only faced mesh objects are supported.
- Mesh intersection edges are not yet detected.
- Freestyle rendering lacks Z depth information.
- Panoramic cameras are unsupported.

[Related references](INDEX.md).
