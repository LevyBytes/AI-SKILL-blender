# bmesh.ops: bmesh.ops. region_extend ( bm , geom =  , use_contract = False , use_faces = False , use_face_step = False )

bmesh.ops. region_extend ( bm , geom = [] , use_contract = False , use_faces = False , use_face_step = False ) 

Region Extend.

Used to implement the select more/less tools.
Puts geometry surrounding regions of geometry in geom into geom.out .

If use_faces is 0 then geom.out spits out verts and edges,
otherwise it spits out faces.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- use_contract ( bool ) – Find boundary inside the regions, not outside.

- use_faces ( bool ) – Extend from faces instead of edges.

- use_face_step ( bool ) – Step over connected faces.

Returns :

- geom :
Output slot, computed boundary geometry.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
