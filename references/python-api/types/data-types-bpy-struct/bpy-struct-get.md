# bpy.types.bpy_struct: get

get ( key , default = None , / )

Hands back the custom property stored at key, or default if it isn't present
(mirroring Python's dictionary method of the same name).

Parameters :

- key ( str ) – The key associated with the custom property.

- default ( Any ) – Optional argument for the value to return if
key is not found.

Returns :

Custom property value or default.

Return type :

Any

Note

Limited to: Types with Custom Property Support.

[Related references](INDEX.md).
