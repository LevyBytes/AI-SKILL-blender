# bpy.types.BlendData: batch_remove

batch_remove ( ids ) 

Erase multiple IDs in one operation.

Note that this method is faster than repeated calls to remove() (from bpy.types.BlendData
ID collections), but has lower safety/flexibility (it can destabilize Blender, e.g. by removing all scenes…).

Parameters :

ids (Sequence[bpy.types.ID]) – Sequence of IDs (types can be mixed).

[Related references](INDEX.md).
