# bmesh.ops: bmesh.ops. bisect_plane ( bm , geom =  , dist = 0 , plane_co = mathutils.Vector() , plane_no = mathutils.Vector() , use_snap_center = False , clear_outer = False , clear_inner = False )

bmesh.ops. bisect_plane ( bm , geom = [] , dist = 0 , plane_co = mathutils.Vector() , plane_no = mathutils.Vector() , use_snap_center = False , clear_outer = False , clear_inner = False ) 

Bisect Plane.

Bisects the mesh by a plane (cut the mesh in half).

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- dist ( float ) – Minimum distance when testing if a vert is exactly on the plane.

- plane_co ( Sequence [ float ] ) – Point on the plane.

- plane_no ( Sequence [ float ] ) – Normal of the plane.

- use_snap_center ( bool ) – Snap axis aligned verts to the center.

- clear_outer ( bool ) – When enabled, remove all geometry on the positive side of the plane.

- clear_inner ( bool ) – When enabled, remove all geometry on the negative side of the plane.

Returns :

- geom_cut :
Output geometry aligned with the plane (new and existing).

type list[bmesh.types.BMVert | bmesh.types.BMEdge]

- geom :
Input and output geometry (result of cut).

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
