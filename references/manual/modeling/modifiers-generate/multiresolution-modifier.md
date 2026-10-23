# Multiresolution Modifier

## Multiresolution Modifier

The Multiresolution modifier (often shortened to "Multires") subdivides a mesh much like the Subdivision Surface modifier, but also lets you edit the new subdivision levels in Sculpt Mode.
Note: Multiresolution is the only modifier that can't be repositioned in the stack after any modifier that changes geometry or other object data (so all Generate, some Modify, and some Simulate modifiers can't come before it). Deform modifiers placed after Multires apply to the Multires subdivision levels rather than the base mesh.
Tip: this is especially handy for re-projecting details from another sculpt with a Shrinkwrap modifier — for the best result, set the wrap method to Project, snap mode to Above Surface, and enable Negative.

Options:
Levels Viewport: the subdivision level shown in the viewport.
Sculpt: the subdivision level used specifically in Sculpt Mode; while sculpting, use Alt-1 to decrease the level or Alt-2 to increase it.
Render: the subdivision level shown when rendering.
Sculpt Base Mesh: deform the unsubdivided base mesh instead of the higher levels while the set level is previewed, so you can make much broader changes in visual context to higher sculpted detail without creating surface noise and artifacts.
Optimal Display: display only the original geometry's edges, so the wireframe render skips the subdivided edges.

Subdivision:
Subdivide: create a smooth subdivision level (using the default Catmull-Clark algorithm).
Simple: create a level with unsmoothed base-mesh edges (a simple interpolation that subdivides edges without smoothing).
Linear: create a completely unsmoothed level (linear interpolation of the current sculpted displacement).
Unsubdivide: rebuild a lower subdivision level of the current base mesh.
Delete Higher: delete all subdivision levels above the current one.

Shape:
Reshape: copy another object's shape onto the multires levels by copying its vertex coordinates; to use it, select a different mesh object with matching topology and vertex indices, Shift-select the object to copy onto, and click Reshape.
Apply Base: modify the original unsubdivided mesh to match the subdivided mesh's form, applying a heuristic to the base-mesh vertices that assumes a Subdivision Surface modifier will be added.
Conform Base: modify the original unsubdivided mesh to match the subdivided mesh's form, with the base-mesh vertices ending at their subdivided positions.

Generate:
Rebuild Subdivisions: rebuild all possible subdivision levels to generate a lower-resolution base mesh, used to make an optimized multiresolution version of a preexisting sculpt; available only when no subdivision level has been created through the modifier.
Save External: save displacements to an external .btx file.

Advanced:
Quality: how precisely vertices are positioned relative to their theoretical position; can be lowered for better performance on high-poly meshes.
UV Smooth: how UVs are handled during subdivision.
- None: UVs stay unchanged.
- Keep Corners: UV islands are smoothed, but their boundary stays unchanged.
- Keep Corners, Junctions: UVs are smoothed, with corners on a discontinuous boundary and junctions of three or more regions kept sharp.
- Keep Corners, Junctions, Concave: UVs are smoothed, with those corners, junctions, and also darts and concave corners kept sharp.
- Keep Boundaries: UVs are smoothed, but boundaries stay sharp.
- All: both UVs and their boundaries are smoothed.
Boundary Smooth: how open boundaries (and corners) are smoothed.
- All: smooth boundaries, including corners.
- Keep Corners: smooth boundaries, but keep corners sharp.
Use Creases: use the Weighted Edge Creases values stored in edges to control how smooth they're made.
Use Custom Normals: interpolate the resulting mesh's existing Custom Split Normals.

Usage — Baking: baking converts high-resolution geometry detail, such as sculpted displacement or surface normals, into 2D texture maps that you then apply to a lower-resolution mesh to reproduce fine surface detail without the performance cost of dense geometry — essential where high-res sculpt data is transferred to low-res meshes for rendering or game engines. To make a normal or displacement map, use the Bake from Multires option in the Render panel, which compares two resolution levels of the Multiresolution modifier: Viewport Levels (used as the low-resolution base mesh) and Render Levels (used as the high-resolution detail mesh); the difference between them is baked into a texture map.
Bake Types: what surface information is extracted from the modifier:
- Normals: bake the surface-normal direction differences between the base and detailed levels; the normal map encodes lighting that reproduces fine sculpted detail in shading without changing the geometry — ideal for normal-mapped materials in Cycles, Eevee, and real-time engines.
- Displacement: bake the height differences between the base and high-resolution mesh as a grayscale image, with lighter areas raised and darker areas recessed; usable for true displacement in render engines or for parallax/height-based shading.
- Vector Displacement: bake 3D displacement vectors for the full spatial offset from the base to the detailed surface; unlike regular displacement it captures overhangs and non-vertical displacements for a more accurate representation, encoding XYZ displacement in the RGB color channels.
Important: for a correct bake, set the modifier's Viewport Levels to 0 so the base mesh is truly low-resolution, and set Render Levels to the highest sculpt level that contains the desired detail.

Ensure proper UV layout and an active Image Texture node in Shader Editor so the baked map can be applied.

Higher Viewport Levels partially apply sculpted displacement beforehand, corrupting bakes.

For best precision with height maps, choose OpenEXR or TIFF at 16 or 32 bits rather than standard formats.

Check that image color space is set to Non-Color (not sRGB) in Image Editor or Shader Editor.

Additional baking options and workflows are documented under Render Baking.

[Related references](INDEX.md).
