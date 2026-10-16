# bpy.types.VertexWeightProximityModifier: proximity_geometry, proximity_mode

proximity_geometry 

Take the smallest computed distance to the target object's geometry as the weight (default { 'FACE' })

- VERTEX
Vertex – Compute distance to nearest vertex.

- EDGE
Edge – Compute distance to nearest edge.

- FACE
Face – Compute distance to nearest face.

Type :

set[Literal['VERTEX', 'EDGE', 'FACE']]
proximity_mode 

Which distances to the target object to rely on (default 'GEOMETRY' )

- OBJECT
Object – Use distance between affected and target objects.

- GEOMETRY
Geometry – Use distance between affected object's vertices and target object, or target object's geometry.

Type :

Literal['OBJECT', 'GEOMETRY']

[Related references](INDEX.md).
