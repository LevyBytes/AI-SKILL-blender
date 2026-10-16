# bmesh.ops: bmesh.ops. dissolve_verts ( bm , verts =  , use_face_split = False , use_boundary_tear = False )

bmesh.ops. dissolve_verts ( bm , verts = [] , use_face_split = False , use_boundary_tear = False ) 

Dissolve Verts.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- use_face_split ( bool ) – Split off face corners to maintain surrounding geometry.

- use_boundary_tear ( bool ) – Split off face corners instead of merging faces.

[Related references](INDEX.md).
