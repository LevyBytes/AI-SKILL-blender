# bmesh.ops: bmesh.ops. extrude_discrete_faces ( bm , faces =  , use_normal_flip = False , use_select_history = False )

bmesh.ops. extrude_discrete_faces ( bm , faces = [] , use_normal_flip = False , use_select_history = False ) 

Individual Face Extrude.

Extrudes faces individually.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input faces.

- use_normal_flip ( bool ) – Create faces with reversed direction.

- use_select_history ( bool ) – Preserve the selection history in the extruded geometry.

Returns :

- faces :
Output faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
