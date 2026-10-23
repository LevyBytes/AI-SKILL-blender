# Transfer Mesh Data: One-To-One Mappings, Interpolated Mappings

### One-To-One Mappings

These mappings select only one source component for each destination one.

Vertex Data

Nearest Vertex
Applies the nearest source vertex.

Nearest Edge Vertex
Applies the nearest source vertex on the nearest (by center point distance) source edge.

Nearest Face Vertex
Applies the nearest source vertex on the nearest (by center point distance) source face.

Edge Data

Nearest Vertices
Applies the source edge whose vertices are nearest to the destination edge's.

Nearest Edge
Applies the source edge whose center is nearest to the destination edge's center.

Nearest Face Edge
Applies the nearest source edge on the nearest face (both by center distance).

Face Corner Data
A face corner represents a vertex within a face context. This idea is frequently used in UV maps: each face corner can have distinct UV coordinates, or equivalently, one 3D vertex can map to numerous UV vertices (one per face).

Selection Options for Corner Data
Nearest Corner and Best Matching Normal: identifies the source corner nearest to the destination, prioritizing those whose split normals align most closely.
Nearest Corner and Best Matching Face Normal — selects the source corner nearest to the target corner, preferring one whose face normal closely resembles the target's face normal.
Nearest Corner of Nearest Face: takes the closest source corner residing on the nearest source face.

Face Data

Nearest Face: targets the nearest source face, measured from its midpoint.

Best Normal-Matching: projects a ray from the center of the destination face along its normal direction to find intersecting source faces.

### Interpolated Mappings 

These methods can combine multiple source elements and blend their values.

Vertex Data

Nearest Edge Interpolated: locates the closest point on the nearest source edge and blends the vertices of that edge.

Nearest Face Interpolated: finds the closest position on the nearest source face and interpolates across its vertex values.

Projected Face Interpolated: casts a ray from the destination vertex along its normal to strike a source face, then interpolates the face's vertex values.

Edge Data

Projected Edge Interpolated: projects multiple points along the destination edge (each using the interpolated normal of adjacent vertices) onto source edges, then blends their values.

Face Corner Data

Nearest Face Interpolated: locates the nearest point on the closest source face and blends the corner values of that face.

Projected Face Interpolated: projects the destination corner along its normal onto a source face and interpolates corner values at the projected location.

Face Data

Projected Face Interpolated: casts rays from multiple points on the destination face along its normal to locate source faces, then blends their values.

[Related references](INDEX.md).
