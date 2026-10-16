# Shrinkwrap Modifier

The Shrinkwrap modifier draws an object toward another object's surface, relocating each vertex to the nearest point on the target geometry using one of four methods.

It works on meshes, lattices, curves, surfaces, and text.

Wrap Method selects how the nearest surface point is found. Some methods add additional controls.

Snap Mode (available for most methods) determines how the vertex moves to the selected target point. Options differ mainly when Offset is nonzero:

On Surface moves the vertex; offset applies along the line joining original and target positions, toward the original.

Outside Surface matches On Surface but offset goes toward the outside.

Above Surface matches On Surface but offset follows the target's smooth normal.

Inside prevents movement if the vertex already lies within the target. Offset shrinks the allowed interior volume along the projection line.

Outside prevents movement if the vertex is already outside. Offset expands the exterior exclusion zone along the projection line.

Note: Inside and Outside enable crude collision detection, though determining inside vs. outside based on target normals is unreliable near 90-degree and acute angles.

Target specifies the shrink target mesh.

Offset sets how far from the computed target position the vertex stops.

Vertex Group controls displacement per-vertex. Group members displace; others do not (equivalent to weight 0).

Nearest Surface Point selects the closest point anywhere on the target surface.

Project mode shoots vertices along a chosen axis until they contact the target. Vertices missing contact stay in place.

Limit restricts the maximum distance between original and projected position. Exceeding it prevents projection.

Subdivision Levels applies temporary Catmull-Clark subdivision to the modified geometry before wrapping.

Axis selects the projection direction (local). Combinations create median projection axes. If none selected, vertex normal direction is used.

Negative/Positive enables one or both axis directions. Both enabled evaluates both and selects the nearest hit.

Face Cull prevents projection over specified face directions (front or back, determined by normal direction).

Invert Cull, when Face Cull is active and Negative direction is allowed, inverts the Front/Back choice for the Negative direction—useful for two-direction projection.

Auxiliary Target adds a secondary target object for projection.

Nearest Vertex snaps vertices to the closest target vertex. It adds no extra options and does not support Snap Mode.

Target Normal Project, slower but smoother than Nearest Surface Point, seeks the nearest point whose interpolated smooth normal faces or away from the original vertex. Boundary edges are treated as infinitely thin cylinders emitting normals perpendicularly; flat shading is ignored.

[Related references](INDEX.md).
