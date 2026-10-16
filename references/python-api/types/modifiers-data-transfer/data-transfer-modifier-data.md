# bpy.types.DataTransferModifier: data_types_edges, data_types_loops, data_types_polys, data_types_verts

data_types_edges

Selects which edge layers get copied over (default set())

- `SHARP_EDGE`
Sharp – Carry across the sharp-edge marking.

- SEAM
UV Seam – Carry across the UV seam marking.

- CREASE
Crease – Carry across subdivision crease values.

- `BEVEL_WEIGHT_EDGE`
Bevel Weight – Carry across bevel weighting.

- `FREESTYLE_EDGE`
Freestyle – Carry across the Freestyle edge marking.

Type :

set[Literal[‘`SHARP_EDGE`’, ‘SEAM’, ‘CREASE’, ‘`BEVEL_WEIGHT_EDGE`’, ‘`FREESTYLE_EDGE`’]]
data_types_loops

Selects which face-corner layers get copied over (default set())

- `CUSTOM_NORMAL`
Custom Normals – Carry across the custom normals.

- `COLOR_CORNER`
Colors – Carry across color attributes.

- UV
UVs – Carry across UV layers.

Type :

set[Literal[‘`CUSTOM_NORMAL`’, ‘`COLOR_CORNER`’, ‘UV’]]
data_types_polys

Selects which face layers get copied over (default set())

- SMOOTH
Smooth – Carry across the flat/smooth marking.

- `FREESTYLE_FACE`
Freestyle Mark – Carry across the Freestyle face marking.

Type :

set[Literal[‘SMOOTH’, ‘`FREESTYLE_FACE`’]]
data_types_verts

Selects which vertex layers get copied over (default set())

- `VGROUP_WEIGHTS`
Vertex Groups – Carry across the active vertex group or all of them.

- `BEVEL_WEIGHT_VERT`
Bevel Weight – Carry across bevel weighting.

- `COLOR_VERTEX`
Colors – Carry across color attributes.

Type :

set[Literal[‘`VGROUP_WEIGHTS`’, ‘`BEVEL_WEIGHT_VERT`’, ‘`COLOR_VERTEX`’]]

[Related references](INDEX.md).
