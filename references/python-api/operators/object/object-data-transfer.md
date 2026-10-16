# bpy.ops.object.data_transfer

bpy.ops.object. data_transfer ( * , use_reverse_transfer = False , use_freeze = False , data_type = '`VGROUP_WEIGHTS`' , use_create = True , vert_mapping = 'NEAREST' , edge_mapping = 'NEAREST' , loop_mapping = '`NEAREST_POLYNOR`' , poly_mapping = 'NEAREST' , use_auto_transform = False , use_object_transform = True , use_max_distance = False , max_distance = 1.0 , ray_radius = 0.0 , islands_precision = 0.1 , layers_select_src = 'ACTIVE' , layers_select_dst = 'ACTIVE' , mix_mode = 'REPLACE' , mix_factor = 1.0 ) 

Distribute structure layer(s) (weights, edge boundary, etc.) from highlighted to chose meshes

Parameters :

- use_reverse_transfer ( bool ) – Reverse Transfer, Transfer from selected objects to active one (optional)

- use_freeze ( bool ) – Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry (optional)

- data_type ( Literal [ '`VGROUP_WEIGHTS`' , '`BEVEL_WEIGHT_VERT`' , '`COLOR_VERTEX`' , '`SHARP_EDGE`' , 'SEAM' , 'CREASE' , '`BEVEL_WEIGHT_EDGE`' , '`FREESTYLE_EDGE`' , '`CUSTOM_NORMAL`' , '`COLOR_CORNER`' , 'UV' , 'SMOOTH' , '`FREESTYLE_FACE`' ] ) – Data Type, Which data to transfer (optional)

- `VGROUP_WEIGHTS`
Vertex Group(s) – Transfer active or all vertex groups.

- `BEVEL_WEIGHT_VERT`
Bevel Weight – Transfer bevel weights.

- `COLOR_VERTEX`
Colors – Color Attributes.

- `SHARP_EDGE`
Sharp – Transfer sharp mark.

- SEAM
UV Seam – Transfer UV seam mark.

- CREASE
Subdivision Crease – Transfer crease values.

- `BEVEL_WEIGHT_EDGE`
Bevel Weight – Transfer bevel weights.

- `FREESTYLE_EDGE`
Freestyle Mark – Transfer Freestyle edge mark.

- `CUSTOM_NORMAL`
Custom Normals – Transfer custom normals.

- `COLOR_CORNER`
Colors – Color Attributes.

- UV
UVs – Transfer UV layers.

- SMOOTH
Smooth – Transfer flat/smooth mark.

- `FREESTYLE_FACE`
Freestyle Mark – Transfer Freestyle face mark.

- use_create ( bool ) – Create Data, Add data layers on destination meshes if needed (optional)

- vert_mapping (Literal[Dt Method Vertex Items]) – Vertex Mapping, Method used to map source vertices to destination ones (optional)

- edge_mapping (Literal[Dt Method Edge Items]) – Edge Mapping, Method used to map source edges to destination ones (optional)

- loop_mapping (Literal[Dt Method Loop Items]) – Face Corner Mapping, Method used to map source faces' corners to destination ones (optional)

- poly_mapping (Literal[Dt Method Poly Items]) – Face Mapping, Method used to map source faces to destination ones (optional)

- use_auto_transform ( bool ) – Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes.Warning: Results will never be as good as manual matching of objects(optional)

- use_object_transform ( bool ) – Object Transform, Evaluate source and destination meshes in global space (optional)

- use_max_distance ( bool ) – Only Neighbor Geometry, Source elements must be closer than given distance from destination one (optional)

- max_distance ( float ) – Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings (in [0, inf], optional)

- ray_radius ( float ) – Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges) (in [0, inf], optional)

- islands_precision ( float ) – Islands Precision, Factor controlling precision of islands handling (the higher, the better the results) (in [0, 10], optional)

- layers_select_src (Literal[Dt Layers Select Src Items]) – Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)

- layers_select_dst (Literal[Dt Layers Select Dst Items]) – Destination Layers Matching, How to match source and destination layers (optional)

- mix_mode (Literal[Dt Mix Mode Items]) – Mix Mode, How to affect destination elements with source values (optional)

- mix_factor ( float ) – Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode) (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
