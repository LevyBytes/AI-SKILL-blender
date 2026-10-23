# bpy.types.XrActionMapItems: methods

## XrActionMapItems(bpy_prop_collection)

### XrActionMapItems(bpy_prop_collection) 

base classes: bpy_prop, bpy_prop_collection
class bpy.types. XrActionMapItems ( bpy_prop_collection ) 

A grouping of XR action map items
new ( name , replace_existing ) 

new

Parameters :

- name ( str ) – Name of the action map item, (never None)

- replace_existing ( bool ) – Replace Existing, Swap out any item that already carries this name

Returns :

Item, Added action map item

Return type :

XrActionMapItem
new_from_item ( item ) 

new_from_item

Parameters :

item (XrActionMapItem) – Item, An item to copy as a template (never None)

Returns :

Item, Added action map item

Return type :

XrActionMapItem
remove ( item ) 

remove

Parameters :

item (XrActionMapItem) – Item, (never None)
find ( name ) 

find

Parameters :

name ( str ) – Name, (never None)

Returns :

Item, The action map item with the given name

Return type :

XrActionMapItem
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
