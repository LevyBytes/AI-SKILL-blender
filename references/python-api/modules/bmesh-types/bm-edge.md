# bmesh.types.BMEdge

class bmesh.types. BMEdge
The BMesh edge connecting 2 verts.
calc_face_angle ( fallback = None )
Returns the angle between this edge's two connected faces.
Parameters: fallback ( Any ) – return this when the edge doesn't have 2 faces (instead of raising a ValueError).
Returns: The angle between 2 connected faces in radians.
Return type: float
calc_face_angle_signed ( fallback = None )
Returns the signed angle between this edge's two connected faces.
Parameters: fallback ( Any ) – return this when the edge doesn't have 2 faces (instead of raising a ValueError).
Returns: The angle between 2 connected faces in radians (negative for a concave join).
Return type: float
calc_length ( )
Returns the length of the edge.
Returns: The length between both verts.
Return type: float
calc_tangent ( loop )
Returns the tangent at this edge relative to a face (pointing inward into the face), using the face normal for the calculation.
Parameters: loop (bmesh.types.BMLoop) – The loop used for tangent calculation.
Returns: a normalized vector.
Return type: mathutils.Vector
copy_from ( other )
Copies values from another element of matching type.
Parameters: other ( Self ) – Another element of the same type to copy from.
hide_set ( hide )
Sets the hide state. Unlike the hide attribute, this also updates the selection and hide state of associated geometry.
Parameters: hide ( bool ) – Hidden or visible.
normal_update ( )
Updates the normals of all connected faces and the edge's verts.
Note: an edge vertex's normal will be a zero vector if the vertex's is_wire is True.
other_vert ( vert )
Returns the other vertex on this edge, or None if the vertex isn't used by this edge.

Parameters: vert (bmesh.types.BMVert) – a vert in this edge.
Returns: The edge's other vert.
Return type: bmesh.types.BMVert | None
select_set ( select )
Sets the selection. Unlike the select attribute, this also updates the selection state of associated geometry.
Parameters: select ( bool ) – Select or de-select.
Note: this flushes selection down (e.g. selecting a face also selects its edges and vertices) but not up (e.g. de-selecting a vertex won't de-select faces that use it); flushing is typically still needed before finishing with a mesh.
hide
Hidden state of this element.
Type: bool
index
Index of this element.
Type: int
Note: this value isn't necessarily valid — while editing the mesh it can become dirty — and you can assign any number to it for a script's own logic. To ensure it's up to date, see bmesh.types.BMElemSeq.index_update().
is_boundary
True when this edge is at the boundary of a face (read-only).
Type: bool
is_contiguous
True when this edge is manifold, between two faces with the same winding (read-only).
Type: bool
is_convex
True when this edge joins two convex faces, depends on a valid face normal (read-only).
Type: bool
is_manifold
True when this edge is manifold (read-only).
Type: bool
is_valid
True when this element is valid (hasn't been freed or removed).
Type: bool
is_wire
True when this edge is not connected to any faces (read-only).
Type: bool
link_faces
Faces connected to this edge (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMFace]
link_loops
Loops connected to this edge (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMLoop]
seam
Seam for UV unwrapping.
Type: bool
select
Selected state of this element.
Type: bool
smooth
Smooth state of this element.
Type: bool
tag
A generic attribute scripts can use for their own logic.
Type: bool
verts
Verts this edge uses (always 2) (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMVert]

[Related references](INDEX.md).
