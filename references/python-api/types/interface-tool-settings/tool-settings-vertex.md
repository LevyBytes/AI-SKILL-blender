# bpy.types.ToolSettings: vertex_group_subset, vertex_group_user, vertex_group_weight, vertex_paint

vertex_group_subset 

Restrict which Vertex groups are shown (default 'ALL' )

- ALL
All – All Vertex Groups.

- `BONE_DEFORM`
Deform – Vertex Groups assigned to Deform Bones.

- `OTHER_DEFORM`
Other – Vertex Groups assigned to non Deform Bones.

Type :

Literal[‘ALL’, ‘`BONE_DEFORM`’, ‘`OTHER_DEFORM`’]
vertex_group_user 

Show vertices that carry no weight (default 'ACTIVE' )

- NONE
None.

- ACTIVE
Active – Show vertices with no weights in the active group.

- ALL
All – Show vertices with no weights in any group.

Type :

Literal[‘NONE’, ‘ACTIVE’, ‘ALL’]
vertex_group_weight 

Weight given when assigning to vertex groups (in [0, 1], default 1.0)

Type :

float
vertex_paint 

(readonly)

Type :

VertexPaint

[Related references](INDEX.md).
