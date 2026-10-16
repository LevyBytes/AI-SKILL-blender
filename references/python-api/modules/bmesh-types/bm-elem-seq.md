# bmesh.types.BMElemSeq

class bmesh.types. BMElemSeq
A general sequence type for accessing any sequence of bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace, bmesh.types.BMLoop. When accessed via bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces there are also functions to create/remove items.
index_update ( )
Initializes the index values of this sequence — the equivalent of looping over all elements and assigning their index values:
```python
for index, ele in enumerate(sequence):
    ele.index = index
```
Note: running this on sequences other than bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces works but won't give each element a valid index — instead its order in the sequence is set.

[Related references](INDEX.md).
