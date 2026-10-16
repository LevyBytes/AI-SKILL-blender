# bmesh.types.BMLoop

class bmesh.types. BMLoop
Normally accessed from bmesh.types.BMFace.loops, where each face loop represents a corner of the face.
calc_angle ( )
Returns the angle at this loop's corner of the face, computed so that sharper corners give lower angles.
Returns: The angle in radians.
Return type: float
calc_normal ( )
Returns the normal at this loop's corner of the face, falling back to the face normal for straight lines.
Returns: a normalized vector.
Return type: mathutils.Vector
calc_tangent ( )
Returns the tangent at this loop's corner of the face (pointing inward into the face), falling back to the face normal for straight lines.
Returns: a normalized vector.
Return type: mathutils.Vector
copy_from ( other )
Copies values from another element of matching type.
Parameters: other ( Self ) – Another element of the same type to copy from.
copy_from_face_interp ( face , vert = True , multires = True )
Interpolates the customdata from a face onto this loop (the loop's vert should overlap the face).
Parameters:
- face (bmesh.types.BMFace) – The face to interpolate data from.
- vert ( bool ) – When enabled, interpolate the loop's vertex data (optional).
- multires ( bool ) – When enabled, interpolate the loop's multires data (optional).
uv_select_edge_set ( select )
Sets the UV edge selection state.
Parameters: select ( bool ) – Select or de-select.
Note: this flushes selection down (selecting an edge also selects its vertices) but not up (de-selecting a vertex won't de-select the edges & faces that use it); flushing with bmesh.types.BMesh.uv_select_flush_mode() is still needed before finishing with a mesh.
uv_select_vert_set ( select )
Sets the UV vertex selection state.
Parameters: select ( bool ) – Select or de-select.
Note: this doesn't flush selection, so selecting a vertex won't select the edges & faces that use it; flushing with bmesh.types.BMesh.uv_select_flush_mode() is still needed before finishing with a mesh.
edge
The loop's edge (between this loop and the next) (read-only).
Type: bmesh.types.BMEdge
face
The face this loop belongs to (read-only).
Type: bmesh.types.BMFace
index
Index of this element.
Type: int
Note: this value isn't necessarily valid — while editing the mesh it can become dirty — and you can assign any number to it for a script's own logic. To ensure it's up to date, see bmesh.types.BMElemSeq.index_update().
is_convex
True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).
Type: bool
is_valid
True when this element is valid (hasn't been freed or removed).
Type: bool
link_loop_next
The next face corner (read-only).
Type: bmesh.types.BMLoop
link_loop_prev
The previous face corner (read-only).
Type: bmesh.types.BMLoop
link_loop_radial_next
The next loop around the edge (read-only).
Type: bmesh.types.BMLoop
link_loop_radial_prev
The previous loop around the edge (read-only).
Type: bmesh.types.BMLoop
link_loops
Loops connected to this loop (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMLoop]
tag
A generic attribute scripts can use for their own logic.
Type: bool
uv_select_edge
UV edge selected state of this loop.
Type: bool
uv_select_vert
UV vertex selected state of this loop.
Type: bool
vert
The loop's vertex (read-only).
Type: bmesh.types.BMVert

### Sequence Accessors

[Related references](INDEX.md).
