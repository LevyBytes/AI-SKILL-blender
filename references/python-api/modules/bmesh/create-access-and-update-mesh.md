# bmesh creation, edit-mode access and updates

bmesh. from_edit_mesh ( mesh ) 

Return a BMesh from this mesh, currently the mesh must already be in editmode.

Parameters :

mesh (bpy.types.Mesh) – The editmode mesh.

Returns :

the BMesh associated with this mesh.

Return type :

bmesh.types.BMesh

bmesh. new ( * , use_operators = True ) 

Parameters :

use_operators ( bool ) – Support calling operators in bmesh.ops (uses some extra memory per vert/edge/face).

Returns :

Return a new, empty BMesh.

Return type :

bmesh.types.BMesh

bmesh. update_edit_mesh ( mesh , * , loop_triangles = True , destructive = True ) 

Update the mesh after changes to the BMesh in editmode,
optionally recalculating n-gon tessellation.

Parameters :

- mesh (bpy.types.Mesh) – The editmode mesh.

- loop_triangles ( bool ) – Option to recalculate n-gon tessellation.

- destructive ( bool ) – Use when geometry has been added or removed.

[Related references](INDEX.md).
