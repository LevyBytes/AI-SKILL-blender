# bmesh.types.BMesh: methods

### BMesh Types (bmesh.types)
### Base Mesh Type
calc_loop_triangles ( )
Computes a triangle tessellation from quads/ngons.
Returns: The triangulated faces.
Return type: list[tuple[bmesh.types.BMLoop, bmesh.types.BMLoop, bmesh.types.BMLoop]]
calc_volume ( * , signed = False )
Computes the mesh volume from the face normals.
Parameters: signed ( bool ) – when signed is true, negative values may be returned.
Returns: The volume of the mesh.
Return type: float
clear ( )
Clears all mesh data.
copy ( )
Returns: A copy of this BMesh.
Return type: bmesh.types.BMesh
free ( )
Explicitly frees the BMesh data from memory, so any further access raises exceptions.
Note: the BMesh is freed automatically, usually when the script finishes executing; but since that moment is sometimes hard to predict, freeing the data explicitly can be useful.
from_mesh ( mesh , * , face_normals = True , vertex_normals = True , use_shape_key = False , shape_key_index = 0 )
Initializes this bmesh from an existing mesh data-block.
Parameters:
- mesh (bpy.types.Mesh) – The mesh data to load.
- face_normals ( bool ) – Calculate face normals.
- vertex_normals ( bool ) – Calculate vertex normals.
- use_shape_key ( bool ) – Use the locations from a shape key.
- shape_key_index ( int ) – The shape key index to use.
Note: call it multiple times to join multiple meshes. Custom-data layers are only copied from mesh on initialization; later calls copy custom-data to matching layers, and layers missing on the target mesh aren't added.
from_object ( object , depsgraph , * , cage = False , face_normals = True , vertex_normals = True )
Initializes this bmesh from an existing object data-block (only meshes are currently supported).
Parameters:
- object (bpy.types.Object) – The object data to load.
- depsgraph (bpy.types.Depsgraph) – The dependency graph for evaluated data.
- cage ( bool ) – Get the mesh as a deformed cage.
- face_normals ( bool ) – Calculate face normals.
- vertex_normals ( bool ) – Calculate vertex normals.
normal_update ( )
Updates the normals of the mesh's faces and verts.
Note: a vertex whose is_wire is True gets a zero-vector normal.
select_flush ( select )
Flushes selection from vertices, regardless of the current selection mode.
Parameters: select ( bool ) – flush selection or de-selected elements.
select_flush_mode ( * , flush_down = False )
Flushes selection according to the current mode, bmesh.types.BMesh.select_mode.
Parameters: flush_down ( bool ) – Flush selection down from faces to edges & verts or from edges to verts. This option is ignored when vertex selection mode is enabled.
to_mesh ( mesh )
Writes this BMesh's data into an existing Mesh data-block.
Parameters: mesh (bpy.types.Mesh) – The mesh data to write into.
transform ( matrix , * , filter = None )
Transforms the mesh, optionally filtering to flagged data only.
Parameters:
- matrix (mathutils.Matrix) – 4x4 transform matrix.
- filter ( set [ Literal [ 'SELECT' , 'HIDE' , 'SEAM' , 'SMOOTH' , 'TAG' ] ] | None ) – Flag to filter vertices.
uv_select_flush ( select )
Flushes selection from UV vertices to edges & faces, regardless of the selection mode.
Parameters: select ( bool ) – Flush selection or de-selected elements.
Note: this doesn't flush the selection to the mesh; typically call bmesh.types.BMesh.uv_select_sync_to_mesh() afterwards.
uv_select_flush_mode ( * , flush_down = False )
Flushes UV selection according to the current mode, bmesh.types.BMesh.select_mode.
Parameters: flush_down ( bool ) – Flush selection down from faces to edges & verts or from edges to verts. This option is ignored when vertex selection mode is enabled.
uv_select_flush_shared ( select )
Flushes selection from UV vertices to contiguous UVs, regardless of the selection mode.
Parameters: select ( bool ) – Flush selection or de-selected elements.
Note: this doesn't flush the selection to the mesh; typically call bmesh.types.BMesh.uv_select_sync_to_mesh() afterwards.
uv_select_foreach_set ( select , / , * , loop_verts = () , loop_edges = () , faces = () , sticky_select_mode = '`SHARED_LOCATION`' )
Sets the UV selection state for loop-vertices, loop-edges & faces — a close equivalent to selecting in the UV editor.
Parameters:
- select ( bool ) – The selection state to set.
- loop_verts (Iterable[bmesh.types.BMLoop]) – Loop verts to operate on.
- loop_edges (Iterable[bmesh.types.BMLoop]) – Loop edges to operate on.
- faces (Iterable[bmesh.types.BMFace]) – Faces to operate on.
- sticky_select_mode (Literal['`SHARED_LOCATION`', 'DISABLED', '`SHARED_VERTEX`']) – See bpy.types.ToolSettings.uv_sticky_select_mode, which may be passed in directly.
Note: this function is selection-mode independent; typically call bmesh.types.BMesh.uv_select_flush_mode() afterwards. It also doesn't flush the selection to the mesh; typically call bmesh.types.BMesh.uv_select_sync_to_mesh() afterwards.
uv_select_foreach_set_from_mesh ( select , / , * , verts = () , edges = () , faces = () , sticky_select_mode = '`SHARED_LOCATION`' )
Selects or de-selects mesh elements while updating the UV selection — an equivalent to selecting from the 3D viewport for operations that keep a synchronized UV selection.
Parameters:
- select ( bool ) – The selection state to set.
- verts (Iterable[bmesh.types.BMVert]) – Verts to operate on.
- edges (Iterable[bmesh.types.BMEdge]) – Edges to operate on.
- faces (Iterable[bmesh.types.BMFace]) – Faces to operate on.
- sticky_select_mode (Literal['`SHARED_LOCATION`', 'DISABLED', '`SHARED_VERTEX`']) – See bpy.types.ToolSettings.uv_sticky_select_mode, which may be passed in directly.
uv_select_sync_from_mesh ( * , sticky_select_mode = '`SHARED_LOCATION`' )
Syncs selection from the mesh to UVs.
Parameters: sticky_select_mode (Literal['`SHARED_LOCATION`', 'DISABLED', '`SHARED_VERTEX`']) – Behavior when flushing from the mesh to the UV selection (bpy.types.ToolSettings.uv_sticky_select_mode, which may be passed in directly); use this only when preparing to create a UV selection.
Note: this doesn't flush the selection to the mesh; typically call bmesh.types.BMesh.uv_select_sync_to_mesh() afterwards.
uv_select_sync_to_mesh ( )
Syncs selection from UVs to the mesh.

[Related references](INDEX.md).
