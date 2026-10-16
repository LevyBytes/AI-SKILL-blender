# bpy.types.ToolSettings: uv_sculpt, uv_sculpt_all_islands, uv_sculpt_lock_borders, uv_select_mode, uv_sticky_select_mode

uv_sculpt 

(readonly)

Type :

UvSculpt
uv_sculpt_all_islands 

Have the brush act on every island (default False)

Type :

bool
uv_sculpt_lock_borders 

Stop boundary edges from being edited (default False)

Type :

bool
uv_select_mode 

Selection and display mode for UVs (default 'VERTEX' )

Type :

Literal[Mesh Select Mode Uv Items]
uv_sticky_select_mode 

How UV vertex selection is extended (default '`SHARED_LOCATION`' )

- DISABLED
Disabled – Sticky vertex selection disabled.

- `SHARED_LOCATION`
Shared Location – Select UVs that are at the same location and share a mesh vertex.

- `SHARED_VERTEX`
Shared Vertex – Select UVs that share a mesh vertex, whether or not they are at the same location.

Type :

Literal[‘DISABLED’, ‘`SHARED_LOCATION`’, ‘`SHARED_VERTEX`’]

[Related references](INDEX.md).
