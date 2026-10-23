# bpy.types.bpy_prop_collection_idprop

add ( )

Appends a brand-new item onto the collection.

Returns :

A newly created item.

Return type :

Any
clear ( )

Empties the collection by stripping out every item.
move ( src_index , dst_index )

Relocates one item to a different slot within the collection.

Parameters :

- src_index ( int ) – Source item index.

- dst_index ( int ) – Destination item index.
remove ( index )

Deletes a single item from the collection.

Parameters :

index ( int ) – Index of the item to be removed.
## bpy_prop_collection_idprop

### bpy_prop_collection_idprop

base classes: bpy_prop_collection
class bpy.types. bpy_prop_collection_idprop ( bpy_prop_collection )

The built-in class behind user-defined collections.

[Related references](INDEX.md).
