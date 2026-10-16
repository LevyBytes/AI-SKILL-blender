# bmesh.types.BMFace: properties

edges
Edges of this face (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMEdge]
hide
Hidden state of this element.
Type: bool
index
Index of this element.
Type: int
Note: this value isn't necessarily valid — while editing the mesh it can become dirty — and you can assign any number to it for a script's own logic. To ensure it's up to date, see bmesh.types.BMElemSeq.index_update().
is_valid
True when this element is valid (hasn't been freed or removed).
Type: bool
loops
Loops of this face (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMLoop]
material_index
The face's material index.
Type: int
normal

The normal for this face, as a 3D wrapped vector.
Type: mathutils.Vector
select
Selected state of this element.
Type: bool
smooth
Smooth state of this element.
Type: bool
tag
A generic attribute scripts can use for their own logic.
Type: bool
uv_select
UV selected state of this element.
Type: bool
verts
Verts of this face (read-only).
Type: bmesh.types.BMElemSeq[bmesh.types.BMVert]

[Related references](INDEX.md).
