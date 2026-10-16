# bmesh.ops: bmesh.ops. reverse_faces ( bm , faces =  , flip_multires = False )

bmesh.ops. reverse_faces ( bm , faces = [] , flip_multires = False ) 

Reverse Faces.

Inverts the vertex sequence of faces.
This reverses the face normal direction.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input faces.

- flip_multires ( bool ) – Maintain multi-res offset.

[Related references](INDEX.md).
