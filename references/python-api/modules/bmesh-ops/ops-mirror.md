# bmesh.ops: bmesh.ops. mirror ( bm , geom =  , matrix = mathutils.Matrix.Identity(4) , merge_dist = 0 , axis = 'X' , mirror_u = False , mirror_v = False , mirror_udim = False , use_shapekey = False )

bmesh.ops. mirror ( bm , geom = [] , matrix = mathutils.Matrix.Identity(4) , merge_dist = 0 , axis = 'X' , mirror_u = False , mirror_v = False , mirror_udim = False , use_shapekey = False ) 

Mirror.

Copies geometry in reverse across an axis. Overlapping vertices are fused using
merge_dist . Original and mirrored vertex pairs join when they fall within the merge_dist threshold.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- matrix (mathutils.Matrix) – Matrix defining the mirror transformation.

- merge_dist ( float ) – Maximum distance for merging. does no merging if 0.

- axis ( Literal [ 'X' , 'Y' , 'Z' ] ) – The axis to use.

- mirror_u ( bool ) – Mirror UVs across the u axis.

- mirror_v ( bool ) – Mirror UVs across the v axis.

- mirror_udim ( bool ) – Mirror UVs in each tile.

- use_shapekey ( bool ) – Transform shape keys too.

Returns :

- geom :
Output geometry, mirrored.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
