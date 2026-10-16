# bmesh.types.BMDeformVert

class bmesh.types. BMDeformVert
clear ( )
Clears all weights.
get ( key , default = None )
Returns the deform weight matching the key, or default when not found (matching Python's dictionary function of the same name).
Parameters:
- key ( int ) – The vertex group index.
- default ( Any ) – Optional argument for the value to return if key is not found.
Returns: The deform weight, or the default when not found.
Return type: float | Any
items ( )
Returns (group, weight) pairs for this vertex (matching Python's dict.items() functionality).
Returns: (key, value) pairs for each deform weight of this vertex.
Return type: list[tuple[int, float]]
keys ( )
Returns the group indices used by this vertex (matching Python's dict.keys() functionality).
Returns: The deform group indices this vertex uses.
Return type: list[int]
values ( )
Returns the weights of the deform vertex (matching Python's dict.values() functionality).
Returns: The weights that influence this vertex.
Return type: list[float]

[Related references](INDEX.md).
