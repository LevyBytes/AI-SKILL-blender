# bpy.ops.uv.stitch

bpy.ops.uv. stitch ( * , use_limit = False , snap_islands = True , limit = 0.01 , static_island = 0 , active_object_index = 0 , midpoint_snap = False , clear_seams = True , mode = 'VERTEX' , stored_mode = 'VERTEX' , selection = None , objects_selection_count = (0, 0, 0, 0, 0, 0) ) 

Joins selected UV vertices that are close together

Parameters :

- use_limit ( bool ) – Use Limit, Stitch UVs within a specified limit distance (optional)

- snap_islands ( bool ) – Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too) (optional)

- limit ( float ) – Limit, Limit distance in normalized coordinates (in [0, inf], optional)

- static_island ( int ) – Static Island, Island that stays in place when stitching islands (in [0, inf], optional)

- active_object_index ( int ) – Active Object, Index of the active object (in [0, inf], optional)

- midpoint_snap ( bool ) – Snap at Midpoint, UVs are stitched at midpoint instead of at static island (optional)

- clear_seams ( bool ) – Clear Seams, Clear seams of stitched edges (optional)

- mode ( Literal [ 'VERTEX' , 'EDGE' ] ) – Operation Mode, Use vertex or edge stitching (optional)

- stored_mode ( Literal [ 'VERTEX' , 'EDGE' ] ) – Stored Operation Mode, Use vertex or edge stitching (optional)

- selection ( bpy_prop_collection [ SelectedUvElement ]) – Selection, (optional)

- objects_selection_count ( Sequence [ int ] ) – Objects Selection Count, (array of 6 items, in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
