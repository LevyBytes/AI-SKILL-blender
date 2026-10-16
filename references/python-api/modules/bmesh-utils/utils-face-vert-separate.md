# bmesh.utils: bmesh.utils. face_vert_separate ( face , vert )

bmesh.utils. face_vert_separate ( face , vert )
Rips a vertex in a face away and adds a new vertex.
Parameters:
- face (bmesh.types.BMFace) – The face to separate.
- vert (bmesh.types.BMVert) – A vertex in the face to separate.
Returns: The newly created vertex, or None on failure.
Return type: bmesh.types.BMVert | None
Note: this is the same as loop_separate, added only for convenience.

[Related references](INDEX.md).
