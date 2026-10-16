# bmesh.types.BMFace: methods

calc_area ( )
Returns the area of the face.
Returns: The area of the face.
Return type: float
calc_center_bounds ( )
Returns the bounds center of the face.
Returns: a 3D vector.
Return type: mathutils.Vector
calc_center_median ( )
Returns the median center of the face.
Returns: a 3D vector.
Return type: mathutils.Vector
calc_center_median_weighted ( )
Returns the median center of the face weighted by edge lengths.
Returns: a 3D vector.
Return type: mathutils.Vector
calc_perimeter ( )
Returns the perimeter of the face.
Returns: The perimeter of the face.
Return type: float
calc_tangent_edge ( )
Returns the face tangent based on the longest edge.
Returns: a normalized vector.
Return type: mathutils.Vector
calc_tangent_edge_diagonal ( )
Returns the face tangent based on the edge farthest from any vertex.
Returns: a normalized vector.
Return type: mathutils.Vector
calc_tangent_edge_pair ( )
Returns the face tangent based on the two longest disconnected edges.
- Tris: Use the edge pair with the most similar lengths.
- Quads: Use the longest edge pair.
- NGons: Use the two longest disconnected edges.
Returns: a normalized vector.
Return type: mathutils.Vector
calc_tangent_vert_diagonal ( )
Returns the face tangent based on the two most distant vertices.
Returns: a normalized vector.
Return type: mathutils.Vector
copy ( * , verts = True , edges = True )
Makes a copy of this face.
Parameters:
- verts ( bool ) – When set, the faces verts will be duplicated too.
- edges ( bool ) – When set, the faces edges will be duplicated too.
Returns: The newly created face.
Return type: bmesh.types.BMFace
copy_from ( other )
Copies values from another element of matching type.
Parameters: other ( Self ) – Another element of the same type to copy from.
copy_from_face_interp ( face , vert = True )
Interpolates the customdata from another face onto this one (the faces should overlap).
Parameters:
- face (bmesh.types.BMFace) – The face to interpolate data from.
- vert ( bool ) – When True, also copy vertex data.
hide_set ( hide )
Sets the hide state. Unlike the hide attribute, this also updates the selection and hide state of associated geometry.
Parameters: hide ( bool ) – Hidden or visible.
normal_flip ( )
Reverses the winding of a face, which flips its normal.
normal_update ( )
Updates the face normal from the positions of the face verts; it doesn't update the normals of the face verts.
select_set ( select )
Sets the selection. Unlike the select attribute, this also updates the selection state of associated geometry.
Parameters: select ( bool ) – Select or de-select.
Note: this flushes selection down (e.g. selecting a face also selects its edges and vertices) but not up (e.g. de-selecting a vertex won't de-select faces that use it); flushing is typically still needed before finishing with a mesh.
uv_select_set ( select )
Sets the UV face selection state.
Parameters: select ( bool ) – Select or de-select.
Note: this flushes selection down (selecting a face also selects its edges and vertices) but not up; flushing with bmesh.types.BMesh.uv_select_flush_mode() is still needed before finishing with a mesh.

[Related references](INDEX.md).
