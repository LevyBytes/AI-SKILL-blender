# Mesh Structure: Vertices, Edges, Faces, Normals, Shading, Custom Split Normals

## Mesh Structure

### Mesh Structure

Every mesh comes down to three building blocks: vertices , edges , and faces .

Example of mesh structure.

### Vertices

A vertex (plural vertices) is the simplest piece of a mesh, just one point or position in 3D space. In Edit Mode the 3D Viewport draws them as small dots, and an object keeps its vertices as an array of coordinates.

Tip

Don't confuse the object origin with a vertex. It looks alike but is larger and can't be selected.

The vertex is labeled as "A"; the object's origin dot is labeled as "B".

### Edges

Every edge is a straight line joining two vertices. These are the "wires" visible in wireframe view, normally absent from the render, and they're what faces are built on.

### Faces

Faces make up the object's actual surface, the part you get when the mesh renders. Where no face covers an area, that spot simply renders as transparent or nothing at all.

A face spans three (triangles), four (quadrangles), or more (n-gons) vertices, bounded by an edge on each side. People shorten these to tris, quads & n-gons .

Triangles, being flat by nature, are cheap to compute. Quads "deform well," so they win out for animating and for subdivision work.

See also

- Why should triangles be avoided for character animation?

- When should N-gons be used, and when shouldn't they?

### Normals

A normal, in geometry, is a direction or line at right angles to something, typically a triangle or surface, though it may also be taken relative to a line, the tangent line at a point on a curve, or the tangent plane at a point on a surface.

Among other roles, normals govern how the mesh is shaded.

A visualization of the face normals of a torus.

Above, every blue line is one face's normal on the torus, each running perpendicular to the face it sits on. You can switch this view on in Edit Mode from the Mesh Display Viewport Overlays panel.

### Shading

How light meets a 3D object hinges on surface normals, so they weigh heavily on its shading. Normals can be shaded smooth or flat.

With flat shading, faces render uniformly, which usually suits flat-surfaced objects like a cube or pyramid.

With smooth shading, normals are interpolated across a polygonal mesh's vertices, smoothing the transitions between adjacent polygons for a more lifelike look.

Face normals default to flat shading, but you can change this for a whole object or face by face.

For the whole object, use:

- Shade Smooth – marks the entire object smooth.

- Shade Auto Smooth – marks only parts of it smooth.

Shade Flat brings it back to flat.

Shading can equally be set on a per-face, per-edge, or per-vertex basis.

### Custom Split Normals

Custom split normals let you tweak or fake shading by aiming normals somewhere other than their default auto-computed direction. They turn up mostly in game development, where they help offset problems from low-poly objects (classic cases being low-poly trees, bushes, grass, and "rounded" corners).

The basis Blender uses is a "smooth fan": neighboring face corners that meet at one vertex and are "linked" through smooth edges. That lets normals be defined per face corner, across a cluster of adjacent face corners, or per vertex.

This data lives as the custom_normal Attribute on the face corner Domain.

Tip

You can turn off computing custom split normals to gain performance. The toggle lives in the Simplify Rendering Settings.

[Related references](INDEX.md).
