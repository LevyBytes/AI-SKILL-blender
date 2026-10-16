# bmesh.types.BMLayerCollection

class bmesh.types. BMLayerCollection
Gives access to a collection of custom-data layers of the same type; behaves like a Python dictionary, except it also supports list-like index access.
get ( key , default = None )
Returns the value of the layer matching the key, or default when not found (matching Python's dictionary function of the same name).
Parameters:
- key ( str ) – The key associated with the layer.
- default ( Any ) – Optional argument for the value to return if key is not found.
Returns: The layer matching the key or the default value.
Return type: bmesh.types.BMLayerItem | Any
items ( )
Returns the (key, value) pairs of collection members (matching Python's dict.items() functionality).
Returns: (key, value) pairs for each member of this collection.
Return type: list[tuple[str, bmesh.types.BMLayerItem]]
keys ( )
Returns the identifiers of collection members (matching Python's dict.keys() functionality).
Returns: the identifiers for each member of this collection.
Return type: list[str]
new ( name = '' )
Creates a new layer.
Parameters: name ( str ) – Optional name argument (will be made unique).
Returns: The newly created layer.
Return type: bmesh.types.BMLayerItem
remove ( layer )
Removes a layer.
Parameters: layer (bmesh.types.BMLayerItem) – The layer to remove.
values ( )
Returns the values of the collection (matching Python's dict.values() functionality).
Returns: the members of this collection.
Return type: list[bmesh.types.BMLayerItem]
verify ( )
Creates a new layer or returns an existing active layer.
Returns: The newly created layer, or the existing active layer.
Return type: bmesh.types.BMLayerItem
active
The active layer of this type (read-only).
Type: bmesh.types.BMLayerItem | None
is_singleton
True if there can exist only one layer of this type (read-only).
Type: bool

[Related references](INDEX.md).
