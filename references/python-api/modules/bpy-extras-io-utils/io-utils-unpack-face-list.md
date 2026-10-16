# bpy_extras.io_utils: bpy_extras.io_utils. unpack_face_list ( list_of_tuples )

bpy_extras.io_utils. unpack_face_list ( list_of_tuples ) 

Flatten a list of faces (triangles or quads), padding each triangle
with a trailing zero so every group has four entries.

Parameters :

list_of_tuples ( Sequence [ tuple [ int , ... ] ] ) – A sequence of face index tuples (3 or 4 elements each).

Returns :

A flat list of face indices, padded with zeros.

Return type :

list[int]

[Related references](INDEX.md).
