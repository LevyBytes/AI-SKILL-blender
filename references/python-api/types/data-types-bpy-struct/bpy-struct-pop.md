# bpy.types.bpy_struct: pop

pop ( key , default = None , / )

Removes the custom property at key and hands back its value, or default if absent
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
