# bpy.types.Mesh: vertex_colors, vertex_normals, vertex_creases, vertex_paint_mask

vertex_colors

Legacy vertex color layers. Deprecated, use color attributes instead. (default None, readonly)

Type :

LoopColors[MeshLoopColorLayer]
vertex_normals

Each vertex's normal direction, taken as the average of the faces surrounding it (default None, readonly)

Type :

bpy_prop_collection[MeshNormalValue]
vertex_creases

Per-vertex crease weights for the subdivision surface; these map onto the "crease_vert" attribute.

(readonly)
vertex_paint_mask

Per-vertex mask weights used in sculpting and painting; these map onto the ".sculpt_mask" attribute.

(readonly)

[Related references](INDEX.md).
