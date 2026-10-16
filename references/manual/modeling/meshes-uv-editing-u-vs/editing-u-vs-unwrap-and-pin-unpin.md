# Editing UVs: Unwrap, Pin & Unpin

Unwrap

Mode: Edit Mode
Menu: UV ‣ Unwrap
Shortcut: U

Blender offers several UV mapping methods. Simpler projection methods map 3D space to 2D using formulas that interpolate positions toward a point, axis, or plane. Advanced methods suit complex models with specific applications.

Available unwrap methods include: Unwrap, Smart UV Project, Lightmap Pack, Follow Active Quads, Cube Projection, Cylinder Projection, Sphere Projection.

Pin & Unpin

Mode: Edit Mode
Menu: UV ‣ Pin/Unpin
Shortcut: P, Alt - P

Pinned UVs remain fixed during subsequent unwrap operations. Select a UV and press P to pin it; press Alt - P to unpin.

Pinning is most effective with Unwrap on organic objects. For example, when using a Mirror Modifier on a symmetrical object, pin the UVs along the mirror axis, align them on the X axis, and they stay locked in place.

The Pinch and Relax sculpting tools skip pinned UVs, allowing you to pin borders or interior holes for finer sculpting control.

With Live Unwrap enabled, pinning two or more UVs lets you interactively unwrap by moving or scaling the pinned UVs. You can even use the Grab tool to move pinned UVs, fitting islands to specific shapes or regions.

Invert Pins

Mode: Edit Mode
Menu: UV ‣ Invert Pins

Pin all unpinned selected UVs and unpin all currently pinned ones.

Mark/Clear Seams

Mode: Edit Mode
Menu: UV ‣ Mark/Clear Seam

See Seams.

Seams from Islands

Mode: View mode
Menu: UV ‣ Seams from Islands

Adds seams at the boundaries of existing UV islands, useful when modifying the UVs of already-unwrapped meshes.

[Related references](INDEX.md).
