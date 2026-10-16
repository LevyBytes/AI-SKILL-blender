# bmesh.utils: bmesh.utils. face_split_edgenet ( face , edgenet )

bmesh.utils. face_split_edgenet ( face , edgenet )
Splits a face into any number of regions defined by an edgenet.
Parameters:
- face (bmesh.types.BMFace) – The face to split.
- edgenet (Sequence[bmesh.types.BMEdge]) – Sequence of edges.
Returns: The newly created faces.
Return type: tuple[bmesh.types.BMFace, …]
Note: regions defined by edges must connect to the face, otherwise they're ignored as loose edges.

[Related references](INDEX.md).
