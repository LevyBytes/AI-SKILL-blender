# Subdivision Surface Modifier

## Subdivision Surface Modifier

The Subdivision Surface modifier (slang "Subdiv" or "Subsurf") splits a mesh's faces into smaller faces for a smooth appearance, letting you create complex smooth surfaces while modeling simple, low-vertex meshes — avoiding the need to save and maintain huge amounts of data and giving an "organic" look. As with any modifier, its order of execution (position in the stack) has an important bearing on the results. It's a different operation from its companion Smooth Shading (the manual's grid image shows subdivision levels 0 to 3 without and with Smooth Shading).
Tip: this modifier doesn't let you edit the new subdivided geometry without applying it, but the Multiresolution modifier does (in Sculpt Mode).
Note: this modifier uses the OpenSubdiv library as a backend.

Options:
Catmull-Clark: subdivide and smooth the surfaces for a more pleasant-looking mesh; per its Wikipedia page, the "arbitrary-looking formula was chosen by Catmull and Clark based on the aesthetic appearance of the resulting surfaces rather than on a mathematical derivation."
Simple: only subdivide the surfaces, which usually gives no smoothing unless the surface is non-coplanar (the same as the Subdivide operator in Edit Mode); to work around this for non-coplanar geometry, triangulate so all geometry is coplanar. Simple mode can, for example, raise the base-mesh resolution when using displacement maps.
Levels Viewport, Render: the number of subdivision levels shown in the 3D Viewport or the final render.
Warning: higher subdivision levels produce more vertices and thus higher memory use (both system RAM and display video memory), which can hang or crash Blender without enough memory.
Tip: the right combination keeps a fast, lightweight approximation in the viewport while rendering a higher-quality version — and be careful not to set Viewport subdivisions higher than Render, which would make the viewport quality higher than the render.
Optimal Display: when rendering the wireframe, skip the new subdivided edges (display only the original geometry's edges).

Advanced:
Use Limit Surface: place vertices on the surface that infinite subdivision levels would produce (the smoothest possible shape).
Quality — with Use Limit Surface enabled, how precisely vertices are positioned on the limit surface (relative to their theoretical position on an infinitely subdivided mesh); can be lowered for better performance. Higher values don't necessarily improve quality — ideal results may be reached well before the maximum Quality value. Note: this value can affect Edge Crease accuracy, since a higher Quality allows a wider range of crease values to work accurately.
UV Smooth: how subdivision smoothing is applied to UVs.
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
Use Custom Normals: interpolate the resulting mesh's existing Custom Split Normals; otherwise, new faces take the overall normal orientation of the original face.

Adaptive Subdivision (Cycles Only):
Adaptive Subdivision: subdivide objects by their distance to the camera, automatically adding more or less detail; especially useful for fine displacement detail.
Adaptive Space:
- Pixel: subdivide polygons to reach a specified pixel size on screen.
- Object: subdivide to reach a specified edge length in object space; required to use adaptive subdivision for instanced meshes.
Pixel Size: the target polygon pixel size for adaptive subdivision.
Edge Length: the target object-space edge length.
Limitations: multi-view renders can show some inconsistencies between views; instancing works poorly with Pixel-space subdivision (it's based on the original object's position relative to the camera), so Object space is recommended.

Keyboard Shortcuts: to quickly add a Subdivision Surface modifier to one or more objects, select them and press Ctrl-1, which adds the modifier with Viewport subdivisions set to 1; other numbers work too (Ctrl-2, Ctrl-3, etc.) to add a modifier with that many subdivisions, and adding it this way doesn't change the Render subdivisions. If an object already has one, doing this simply changes its subdivision level instead of adding another modifier.

Control: Catmull-Clark subdivision rounds off edges, which often isn't what you want, and several solutions let you control it.
Weighted Edge Creases: these let you change how the Subdivision Surface modifier subdivides geometry to give edges a smooth or sharp appearance. Change the crease weight of selected edges in the Transform panel of the 3D Viewport's Sidebar, or with the scale-like dedicated tool Shift-E; a higher value makes the edge "stronger" and more resistant to the smoothing effect of subdivision surfaces.

### Edge Loops

Subdivision Level 2 cube, the same with an extra Edge Loop, and the same with six extra Edge Loops.

Why does tidy topology matter so much? The Subdivision Surface modifier puts the answer on display. Drop it onto a stock cube and the change is dramatic: as the figure makes plain, the shape stays almost unreadable as a cube right up until you introduce more loops (using Loop Cut and Slide, say).

When a mesh is built with intent, its edge loops sit where they should, and that careful layout is exactly what gives you the freedom to insert or strip away further loops and tune how crisp or rounded the final mesh ends up.

### Known Limitations

### Non-Contiguous Normals

Anywhere the normals shift sharply, the mesh in that area cannot be subdivided smoothly. Such regions, where the normals are non-contiguous, instead get handled through the "Simple" subdivision method.

| Description | Description |
| --- | --- |
| Comparison of good normals and bad normals. | Side view of image on the left. |

Your quickest fix here is to Recalculate Normals. Should that fail to clear it up, flipping the normals by hand may be necessary.

[Related references](INDEX.md).
