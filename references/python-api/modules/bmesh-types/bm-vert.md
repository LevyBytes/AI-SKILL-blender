# bmesh.types.BMVert

class bmesh.types. BMVert
The BMesh vertex type.
calc_edge_angle ( fallback = None )
Returns the angle between this vert's two connected edges.
Parameters: fallback ( Any ) – return this when the vert doesn't have 2 edges (instead of raising a ValueError).
Returns: Angle between edges in radians.
Return type: float
calc_shell_factor ( )
Returns a multiplier based on the vertex's sharpness — a flat surface gives 1.0, and higher values mean sharper edges — used to maintain shell thickness when offsetting verts along their normals.
Returns: offset multiplier
Return type: float
copy_from ( other )
Copies values from another element of matching type.
Parameters: other ( Self ) – Another element of the same type to copy from.
copy_from_face_interp ( face )
Interpolates the customdata from a face onto this vert (the vert should overlap the face).
Parameters: face (bmesh.types.BMFace) – The face to interpolate data from.
copy_from_vert_interp ( vert_pair , fac )
Interpolates the customdata onto this vert from between two other verts.
Parameters:
- vert_pair (Sequence[bmesh.types.BMVert]) – The verts between which to interpolate data from.
- fac ( float ) – The interpolation factor.
hide_set ( hide )
Sets the hide state. Unlike the hide attribute, this also updates the selection and hide state of associated geometry.
Parameters: hide ( bool ) – Hidden or visible.
normal_update ( )
Updates the vertex normal; it doesn't update the normals of adjoining faces.
Note: the vertex normal will be a zero vector if the vertex's is_wire is True.
select_set ( select )
Sets the selection. Unlike the select attribute, this also updates the selection state of associated geometry.
Parameters: select ( bool ) – Select or de-select.
Note: this flushes selection down (e.g. selecting a face also selects its edges and vertices) but not up (e.g. de-selecting a vertex won't de-select faces that use it); flushing is typically still needed before finishing with a mesh.
co
The coordinates for this vertex, as a 3D wrapped vector.
Type: mathutils.Vector
hide
Hidden state of this element.
Type: bool
index
Index of this element.
Type: int
Note: this value isn't necessarily valid — while editing the mesh it can become dirty — and you can assign any number to it for a script's own logic. To ensure it's up to date, see bmesh.types.BMElemSeq.index_update().
is_boundary
True when this vertex is connected to boundary edges (read-only).
Type: bool
is_manifold
True when this vertex is manifold (read-only).
Type: bool
is_valid
True when this element is valid (hasn't been freed or removed).
Type: bool
is_wire
True when this vertex is not connected to any faces (read-only).
Type: bool
link_edges
Edges connected to this vertex (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMEdge]
link_faces
Faces connected to this vertex (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMFace]
link_loops
Loops that use this vertex (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMLoop]
normal
The normal for this vertex, as a 3D wrapped vector.
Type: mathutils.Vector
select
Selected state of this element.
Type: bool
tag
A generic attribute scripts can use for their own logic.
Type: bool

[Related references](INDEX.md).
