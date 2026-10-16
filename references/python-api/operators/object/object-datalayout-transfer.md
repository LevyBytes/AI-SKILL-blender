# bpy.ops.object.datalayout_transfer

bpy.ops.object. datalayout_transfer ( * , modifier = '' , data_type = '' , use_delete = False , layers_select_src = 'ACTIVE' , layers_select_dst = 'ACTIVE' ) 

Distribute schematic of structure layer(s) from highlighted to chose meshes

Parameters :

- modifier ( str ) – Modifier, Name of the modifier to edit (optional, never None)

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

- use_delete ( bool ) – Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source (optional)

- layers_select_src (Literal[Dt Layers Select Src Items]) – Source Layers Selection, Which layers to transfer, in case of multi-layers types (optional)

- layers_select_dst (Literal[Dt Layers Select Dst Items]) – Destination Layers Matching, How to match source and destination layers (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
