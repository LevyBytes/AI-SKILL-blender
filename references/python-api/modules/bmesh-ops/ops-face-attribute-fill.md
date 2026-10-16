# bmesh.ops: bmesh.ops. face_attribute_fill ( bm , faces =  , use_normals = False , use_data = False )

bmesh.ops. face_attribute_fill ( bm , faces = [] , use_normals = False , use_data = False ) 

Face Attribute Fill.

Fill in faces with data from adjacent faces.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input faces.

- use_normals ( bool ) – Copy face winding.

- use_data ( bool ) – Copy face data.

Returns :

- faces_fail :
Faces that could not be handled.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
