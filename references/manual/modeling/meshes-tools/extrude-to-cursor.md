# Extrude to Cursor

## Extrude to Cursor

Extrude to Cursor

Mode: Edit Mode
Shortcut: Ctrl - RMB

Ctrl - RMB creates new vertices interactively at the mouse cursor position. This fundamental operation lets you build connected geometry by placing vertices and edges.

A single vertex is created by Ctrl - RMB when no vertices are selected. Since the 2D screen cannot convey full 3D position from a click alone, the new vertex is placed at the 3D cursor's depth.

Building connected sequences: after placing one vertex, keep the most recent vertex selected and repeat Ctrl - RMB to add subsequent vertices. Each new click creates a vertex at the cursor and links it to the previous vertex with an edge. This workflow builds open chains and networks quickly.

Creating Planar Faces with Two Vertices

Two connected vertices with an existing edge allow Ctrl - RMB to create a planar quad. Blender follows your mouse and constructs the quad in your current viewport plane.

By default, Blender automatically rotates the source edge (the last selected one) to smooth angles between the new edge and existing neighbors. This automatic rotation uses the X and Y displacement of the new and previous edges. If the angle exceeds a threshold, Blender wraps the faces. To prevent automatic rotation, use Shift - Ctrl - RMB instead.

Three or more selected vertices with Ctrl - RMB create planar faces along the selection, following cursor direction — an operation similar to extrusion.

Extrusions are viewport-dependent: the extrusion direction changes when you switch viewports (top, side, front), aligning the geometry to your current orthographic view.

[Related references](INDEX.md).
