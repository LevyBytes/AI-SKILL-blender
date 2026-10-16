# bpy.types.bpy_prop_collection: get

get ( key , default = None )

Hands back the item stored at key, or default when the key isn't present
(mirroring Python's dictionary method of the same name).

Parameters :

- key ( str ) – The identifier for the collection member.

- default ( Any ) – Optional argument for the value to return if
key is not found.

Returns :

The collection member or default.

Return type :

bpy_struct

[Related references](INDEX.md).
