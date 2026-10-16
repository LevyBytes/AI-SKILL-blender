# bmesh.types.BMVertSeq

class bmesh.types. BMVertSeq
ensure_lookup_table ( )
Ensures the internal data needed for int subscript access is initialized for verts/edges/faces, e.g. bm.verts[index]. Call it again after adding/removing data in this sequence.
index_update ( )
Initializes the index values of this sequence — the equivalent of looping over all elements and assigning their index values:
```python
for index, ele in enumerate(sequence):
    ele.index = index
```
Note: running this on sequences other than bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces works but won't give each element a valid index — instead its order in the sequence is set.
new ( co = (0.0, 0.0, 0.0) , source = None )
Creates a new vertex.
Parameters:
- co ( tuple [ float , float , float ] | Sequence [ float ] ) – The initial location of the vertex (optional argument).
- source (bmesh.types.BMVert | None) – Existing vert to initialize settings.
Returns: The newly created vertex.
Return type: bmesh.types.BMVert
remove ( vert )
Removes a vert.
Parameters: vert (bmesh.types.BMVert) – The vert to remove.
sort ( * , key = None , reverse = False )
Sorts the elements of this sequence, using an optional custom sort key. Element indices aren't changed; use bmesh.types.BMElemSeq.index_update() for that.
Parameters:
- key (Callable[[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace], int] | None) – The key that sets the ordering of the elements.
- reverse ( bool ) – Reverse the order of the elements
Note: when the 'key' argument isn't provided, the elements are reordered following their current index value — so you can set indices manually before calling this method.
Warning: existing references to the N'th element will keep pointing at the data at that index.
layers
custom-data layers (read-only).
Type: bmesh.types.BMLayerAccessVert

[Related references](INDEX.md).
