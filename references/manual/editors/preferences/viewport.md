# Viewport

## Viewport

Display — Text Info Overlay:
Object Info — shows the active Object's name and the frame number at the 3D Viewport's top-left.
View Name — shows the current view's name and type at the 3D Viewport's top-left, e.g. "User Perspective" or "Top Orthographic".
Playback Frame Rate (FPS) — shows the frames-per-second refresh rate during playback, at the 3D Viewport's top-left, turning red when the set frame rate can't be met.
Frame Rate Samples — computes the displayed FPS from an average of the current and recent frames; zero uses the number of frames in 1.0 second. More samples average over a longer span, so sudden performance shifts ramp more gradually; fewer samples track actual performance more closely but may jitter, making the FPS harder to read.
Gizmo Size — the gizmo's diameter.
HDRI Preview Size — the diameter of the HDRI sphere overlay.
3D Viewport Axes — Interactive Navigation (draws the axis as an interactive gizmo: click to view along it, drag to orbit), Simple Axes (a simpler, less intrusive axis, with Brightness for how vivid its colors are), or Off (no viewport axis). Size — the diameter of the 3D Viewport Axis widget.
Fresnel – Edit Mode — adds a fresnel effect to edit-mesh overlays, improving readability on very dense meshes but tiring the eyes when modeling lower-poly.

Quality:
Viewport Anti-Aliasing — sets the anti-aliasing for higher-quality rendering.
Smooth Wires — Overlay (draws overlays with smooth wire; without it, wires render aliased — you can disable it for Edit Mode separately since edges don't blend into shaded regions) and Edit Mode (smooth wire in Edit Mode; without it, wires render aliased).

Textures:
Limit Size — caps the maximum resolution of pictures used in textured display to save memory, given as a square of pixels (256 means a 256×256 texture); useful for game work, where the texture limit matches the target card's texture paging blocks.
Anisotropic Filtering — sets the anisotropic-filtering level, improving rendered-texture quality at a performance cost.
Clip Alpha — clips alpha below this threshold in the 3D Viewport; the default is deliberately low to avoid issues on some GPUs.
Image Display Method — how images are rendered. Automatic (uses GLSL on the GPU for speed but falls back to the CPU for large images, which can be slow on the GPU), 2D Texture (uses the CPU for display transform and renders images as a 2D texture), or GLSL (the fastest, using GLSL for display transform and rendering images as a 2D texture).

Subdivision:
GPU Subdivision — in some cases the GPU subdivides a mesh carrying a Subdivision Surface modifier, usually boosting subdivision performance. Note: when on, normals and tangents are interpolated rather than recomputed after smoothing, which can shade differently from the CPU path. Note: unsupported on Qualcomm GPUs on Windows.

[Related references](INDEX.md).
