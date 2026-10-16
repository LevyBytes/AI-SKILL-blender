# bmesh.types.BMEditSelSeq

class bmesh.types. BMEditSelSeq
add ( element )
Adds an element to the selection history (does nothing if it's already added).
Parameters: element (BMVert | BMEdge | BMFace) – The element to add.
clear ( )
Empties the selection history.
discard ( element )
Discards an element from the selection history. Like remove, but doesn't raise an error when the element isn't in the selection list.
Parameters: element (BMVert | BMEdge | BMFace) – The element to discard.
remove ( element )
Removes an element from the selection history.
Parameters: element (BMVert | BMEdge | BMFace) – The element to remove.
validate ( )
Ensures all elements in the selection history are selected.
active
The last selected element, or None (read-only).
Type: bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace | None

[Related references](INDEX.md).
