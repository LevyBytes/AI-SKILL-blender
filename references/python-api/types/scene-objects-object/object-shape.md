# bpy.types.Object: shape_key_add, shape_key_remove, shape_key_clear, shape_keys_selected

shape_key_add ( * , name = 'Key' , from_mix = True ) 

Attach a shape key to this object

Parameters :

- name ( str ) – Unique name for the new key-block (optional, never None)

- from_mix ( bool ) – Create new shape from existing mix of shapes (optional)

Returns :

New shape key-block

Return type :

ShapeKey
shape_key_remove ( key ) 

Detach one Shape Key from this object

Parameters :

key (ShapeKey) – Key-block to be removed (never None)
shape_key_clear ( ) 

Detach every Shape Key from this object
shape_keys_selected ( ) 

Give back the selected shape keys

Returns :

keyblocks

Return type :

bpy_prop_collection[ShapeKey]

[Related references](INDEX.md).
