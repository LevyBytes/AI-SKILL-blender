# bmesh.types.BMesh: properties

edges
The mesh's edge sequence (read-only).
Type: bmesh.types.BMEdgeSeq
faces
The mesh's face sequence (read-only).
Type: bmesh.types.BMFaceSeq
is_valid
True when this element is valid (hasn't been freed or removed).
Type: bool
is_wrapped
True when this mesh is owned by Blender (typically the editmode BMesh).
Type: bool
loops
The mesh's loops (read-only).
Type: bmesh.types.BMLoopSeq
Note: loops must be accessed via faces; this is exposed only for layer access.
select_history
A sequence of selected items (the last is shown as active).
Type: bmesh.types.BMEditSelSeq
select_mode
The selection mode; it can't be assigned an empty set.
Type: set[Literal['VERT', 'EDGE', 'FACE']]
uv_select_sync_valid
True when the UV selection has been synchronized. Setting it to False makes the UV selection be ignored; setting it to True is supported, but it's up to the script author to ensure a correct selection state first.
Type: bool
verts
The mesh's vert sequence (read-only).
Type: bmesh.types.BMVertSeq

### Mesh Elements

[Related references](INDEX.md).
