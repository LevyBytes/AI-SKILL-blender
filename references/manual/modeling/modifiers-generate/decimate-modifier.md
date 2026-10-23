# Decimate Modifier

## Decimate Modifier

The Decimate modifier reduces a mesh's vertex/face count with minimal change to its shape. It's not usually used on carefully, economically modeled meshes (where every vertex and face is needed to define the shape), but it's useful when a mesh results from complex modeling, sculpting, and/or applied Subdivision Surface/Multiresolution modifiers — to cut the polygon count for a performance gain or simply remove unnecessary vertices and edges. Unlike most modifiers, this one doesn't let you visualize the changes in Edit Mode, and it displays the number of faces remaining as a result.

Options:
Collapse: merges vertices together progressively, taking the mesh's shape into account.
Ratio: the ratio of faces to keep after decimation. At 1.0 the mesh is unchanged; at 0.5 edges are collapsed so half the faces remain (see note below); at 0.0 all faces are removed.
Note: although Ratio is directly proportional to the number of remaining faces, triangles are used when calculating the ratio, so if your mesh contains quads or other polygons the remaining face count will be larger than expected, because those stay unchanged if their edges aren't collapsed — this is only true when the Triangulate option is disabled.
Symmetry: maintain symmetry on a single axis.
Triangulate: keep any triangulated geometry resulting from the decimation process.
Vertex Group: a vertex group controlling which parts of the mesh are decimated.
Factor: how much influence the Vertex Group has on the decimation.

Un-Subdivide: think of it as the reverse of subdivide: it attempts to remove edges that were the result of a subdivide operation. It's intended for meshes with mainly grid-based topology (to avoid uneven geometry); if additional editing was done after the subdivide, the results may be unexpected.
Iterations: the number of times to run the un-subdivide; two iterations equal one subdivide operation, so you'll usually want even numbers.

Planar: reduces detail on forms made up of mainly flat surfaces.
Angle Limit: dissolve geometry forming angles (between surfaces) higher than this setting.
Delimit: prevent dissolving geometry in certain places.
- Normal: don't dissolve edges on the borders of areas where the face normals are reversed.
- Material: don't dissolve edges on the borders between different assigned materials.
- Seam: don't dissolve edges marked as UV Seams.
- Sharp: don't dissolve edges marked as Sharp.
- UVs: don't dissolve edges that are part of a UV map.
All Boundaries: when enabled, all vertices along the boundaries of faces are dissolved; this can give better results when using a high Angle Limit.

[Related references](INDEX.md).
