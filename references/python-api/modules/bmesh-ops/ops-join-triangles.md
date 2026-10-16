# bmesh.ops: bmesh.ops. join_triangles ( bm , faces =  , cmp_seam = False , cmp_sharp = False , cmp_uvs = False , cmp_vcols = False , cmp_materials = False , angle_face_threshold = 0 , angle_shape_threshold = 0 , topology_influence = 0 , deselect_joined = False , merge_limit = 0 , neighbor_debug = 0 )

bmesh.ops. join_triangles ( bm , faces = [] , cmp_seam = False , cmp_sharp = False , cmp_uvs = False , cmp_vcols = False , cmp_materials = False , angle_face_threshold = 0 , angle_shape_threshold = 0 , topology_influence = 0 , deselect_joined = False , merge_limit = 0 , neighbor_debug = 0 ) 

Join Triangles.

Intelligently merges triangles based on
angle thresholds and edge properties.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input geometry.

- cmp_seam ( bool ) – Compare seam

- cmp_sharp ( bool ) – Compare sharp

- cmp_uvs ( bool ) – Compare UVs

- cmp_vcols ( bool ) – Compare VCols.

- cmp_materials ( bool ) – Compare materials.

- angle_face_threshold ( float ) – Undocumented.

- angle_shape_threshold ( float ) – Undocumented.

- topology_influence ( float ) – Undocumented.

- deselect_joined ( bool ) – Undocumented.

- merge_limit ( int ) – Undocumented.

- neighbor_debug ( int ) – Undocumented.

Returns :

- faces :
Joined faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
