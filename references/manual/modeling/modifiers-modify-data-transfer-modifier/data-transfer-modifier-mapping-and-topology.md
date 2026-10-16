# Data Transfer Modifier: Mapping, Topology, One-To-One Mappings

### Mapping

### Topology

Pairs the elements purely by index. For this both meshes have to carry the same
count of elements, ordered the same way. It fits best when
the destination mesh is a deformed copy of the source.

See also

Sort Elements, which lets you give both objects
a matching element order.

### One-To-One Mappings

Each of these mappings picks exactly one source element per destination element.

Vertex Data

Nearest Vertex
Takes the closest source vertex.

Nearest Edge Vertex
Takes the closest source vertex lying on the closest source edge (judged by midpoint distance).

Nearest Face Vertex
Takes the closest source vertex lying on the closest source face (judged by midpoint distance).

Edge Data

Nearest Vertices
Takes the source edge whose vertices come closest to those of the destination edge.

Nearest Edge
Takes the source edge whose midpoint comes closest to the destination edge's.

Nearest Face Edge
Takes the closest source edge on the closest face, both judged by midpoint distance.

Face Corner Data
A face corner means a vertex considered in the setting of a face. UV maps are where you meet
it most: every face corner can hold its own UV coordinate, or put another way, a single 3D vertex
may map to several UV vertices, one for each face.

Nearest Corner and Best Matching Normal
Takes the source corner closest to the destination corner that also has the most alike
split normal.

Nearest Corner and Best Matching Face Normal
Takes the source corner closest to the destination corner that also has the most alike
face normal.

Nearest Corner of Nearest Face
Takes the closest source corner on the closest source face.

Face Data

Nearest Face
Takes the closest source face, judged by midpoint distance.

Best Normal-Matching
Shoot a ray out of the destination face's centerpoint along that face's normal
and take whichever source face it strikes.

[Related references](INDEX.md).
