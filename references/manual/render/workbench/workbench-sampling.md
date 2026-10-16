# Sampling

### Sampling

Render quality can be modified via the Anti-Aliasing method. Different configurations apply to the 3D Viewport, viewport rendering, and final rendering.

The 3D Viewport setting is a user preference indicating the antialiasing method performing best on the target system. The viewport rendering and final rendering setting is stored per scene.

Reference

Panel :

Render ‣ Sampling
Preferences ‣ Viewport

No Anti-Aliasing
No antialiasing is applied.

Single Pass Anti-Aliasing
The scene receives a single post-process antialiasing pass.

Multisample
The scene is rendered multiple times with slight offsets. Antialiasing is aggregated from the multiple renders. Sample counts are predefined for optimal distribution.

5, 8, 11, 16, 32

Tip

Multisample antialiasing works well for small detail rendering like hair.

Progressive Viewport Rendering

In the 3D Viewport, one sample renders at a time. When viewport and scene remain unchanged, the next sample renders.

[Related references](INDEX.md).
