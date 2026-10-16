# bmesh.utils: bmesh.utils. face_split ( face , vert_a , vert_b , * , coords = () , use_exist = True , source = None )

bmesh.utils. face_split ( face , vert_a , vert_b , * , coords = () , use_exist = True , source = None )
Splits a face, optionally through intermediate points.
Parameters:
- face (bmesh.types.BMFace) – The face to cut.
- vert_a (bmesh.types.BMVert) – First vertex to cut in the face (face must contain the vert).
- vert_b (bmesh.types.BMVert) – Second vertex to cut in the face (face must contain the vert).
- coords ( Sequence [ Sequence [ float ] ] ) – Optional sequence of 3D points in between vert_a and vert_b.
- use_exist ( bool ) – Use an existing edge if it exists (only used when coords argument is empty or omitted)
- source (bmesh.types.BMEdge | None) – Newly created edge will copy settings from this one.
Returns: The newly created face and loop.
Return type: tuple[bmesh.types.BMFace, bmesh.types.BMLoop]

[Related references](INDEX.md).
