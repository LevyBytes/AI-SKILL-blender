# Mesh Structure: Free Normals, Editing Custom Split Normals, Importing Custom Split Normals

#### Free Normals

Free normals are a kind of custom normal kept straight as direction vectors in object space. Where ordinary custom normals are defined against the surrounding geometry (so-called tangent or corner fan space), free normals owe nothing to mesh topology and lean on neither smooth groups nor edge connectivity.

Being plain vectors, free normals are:

- Efficient: quick to evaluate, so the viewport runs noticeably faster than with tangent-space normals.

- Lightweight: lighter on memory, a real win for dense or heavily instanced meshes.

- Static: they hold still as the mesh deforms (under modifiers or animation), making them best for static geometry or wherever speed is paramount.

Assign them through the Set Mesh Normal Node in Free mode; whichever granularity you want decides whether they land on the vertex, face, or face corner domain.

#### Editing Custom Split Normals

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals

Shortcut :

Alt - N

Several tools exist for editing custom split normals. By default the custom-normal edit tools touch every normal, but they can be limited to just the selected ones. To select a custom normal tied to a specific vertex and face:

- Turn on Vertex and Face element selection modes together ( Shift - LMB enables the second).

- Pick one or more vertices, then a face, repeating with further vertices and another face as needed. The tools' effect reads most clearly with the Edit Mode Overlays option Display vertex-per-face normals as lines switched on.

See also

Editing Normals.

### Importing Custom Split Normals

Certain tools, CAD ones especially, tend to spit out irregular geometry when they tessellate objects into meshes (long, sliver-thin triangles and the like). Auto-computed normals over such geometry often look wrong, so being able to import and use the normals the CAD tool itself produced matters.

Mesh Structure — Topology and Loops

Only the FBX Importer and Alembic Importer currently support importing custom normals.

Understanding Topology

Edge and face loops form continuous chains across mesh geometry. These loops are essential for mesh organization and character animation.

Continuous loops that don't terminate at poles are cyclic — they start and end at the same vertex, dividing the model into two regions. Loops provide a fast, powerful way to select and work with specific mesh areas and are fundamental for organic character rigging.

Poles are vertices where three, five, or more edges meet. At these points, a loop cannot continue uniquely, so it terminates. Vertices with exactly one, two, or four edges are not poles.

Edge Loops

Edge loops connect vertices such that each vertex on the loop has exactly two neighbors outside the loop (on either side), except at terminal vertices on poles. These loops are critical in organic and subsurface modeling, allowing you to build natural-looking models with fewer vertices that deform smoothly when used with subdivision surfaces and animation.

In character models, edge loops should follow anatomical contours and muscle lines. Areas subject to greater deformation (shoulders, knees) have denser loop placement to ensure smooth movement.

Face Loops

Face loops consist of the faces lying between two adjacent edge loops. For non-circular loops, the faces containing poles are excluded from the loop selection.

Additional topology concepts include N-poles and E-poles, as well as non-manifold topology, which are discussed in their respective sections.

[Related references](INDEX.md).
