# bmesh.types.BMFaceSeq

class bmesh.types. BMFaceSeq
ensure_lookup_table ( )
Ensures the internal data needed for int subscript access is initialized for verts/edges/faces, e.g. bm.verts[index]. Call it again after adding/removing data in this sequence.
get ( verts , fallback = None )
Returns a face that uses the verts passed.
Parameters:
- verts (Sequence[bmesh.types.BMVert]) – Sequence of verts.
- fallback ( Any ) – Return this value if nothing is found.
Returns: The face found or the fallback value.
Return type: bmesh.types.BMFace | None
index_update ( )
Initializes the index values of this sequence — the equivalent of looping over all elements and assigning their index values:
```python
for index, ele in enumerate(sequence):
    ele.index = index
```
Note: running this on sequences other than bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces works but won't give each element a valid index — instead its order in the sequence is set.
new ( verts , source = None )
Creates a new face from a given set of verts.
Parameters:
- verts (Sequence[bmesh.types.BMVert]) – Sequence of 3 or more verts.
- source (bmesh.types.BMFace | None) – Existing face to initialize settings (optional argument).
Returns: The newly created face.
Return type: bmesh.types.BMFace
remove ( face )
Removes a face.
Parameters: face (bmesh.types.BMFace) – The face to remove.
sort ( * , key = None , reverse = False )
Sorts the elements of this sequence, using an optional custom sort key. Element indices aren't changed; use bmesh.types.BMElemSeq.index_update() for that.
Parameters:
- key (Callable[[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace], int] | None) – The key that sets the ordering of the elements.
- reverse ( bool ) – Reverse the order of the elements
Note: when the 'key' argument isn't provided, the elements are reordered following their current index value — so you can set indices manually before calling this method.
Warning: existing references to the N'th element will keep pointing at the data at that index.
active
active face.
Type: bmesh.types.BMFace | None
layers
custom-data layers (read-only).
Type: bmesh.types.BMLayerAccessFace

[Related references](INDEX.md).
