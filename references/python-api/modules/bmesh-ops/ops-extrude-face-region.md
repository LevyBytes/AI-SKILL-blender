# bmesh.ops: bmesh.ops. extrude_face_region ( bm , geom =  , edges_exclude = set() , use_keep_orig = False , use_normal_flip = False , use_normal_from_adjacent = False , use_dissolve_ortho_edges = False , use_select_history = False , skip_input_flip = False )

bmesh.ops. extrude_face_region ( bm , geom = [] , edges_exclude = set() , use_keep_orig = False , use_normal_flip = False , use_normal_from_adjacent = False , use_dissolve_ortho_edges = False , use_select_history = False , skip_input_flip = False ) 

Extrude Faces.

Extrude operator (does not transform)

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Edges and faces.

- edges_exclude (set[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input edges to explicitly exclude from extrusion.

- use_keep_orig ( bool ) – Keep original geometry (requires geom to include edges).

- use_normal_flip ( bool ) – Create faces with reversed direction.

- use_normal_from_adjacent ( bool ) – Use winding from surrounding faces instead of this region.

- use_dissolve_ortho_edges ( bool ) – Dissolve edges whose faces form a flat surface.

- use_select_history ( bool ) – Preserve the selection history in the extruded geometry.

- skip_input_flip ( bool ) – Skip flipping of input faces to preserve original orientation.

Returns :

- geom :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
