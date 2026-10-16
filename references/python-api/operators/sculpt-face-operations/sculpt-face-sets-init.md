# bpy.ops.sculpt.face_sets_init

bpy.ops.sculpt. face_sets_init ( * , mode = '`LOOSE_PARTS`' , threshold = 0.5 )

Establish every face set in the surface

Parameters :

- mode ( Literal [ '`LOOSE_PARTS`' , 'MATERIALS' , 'NORMALS' , '`UV_SEAMS`' , 'CREASES' , '`BEVEL_WEIGHT`' , '`SHARP_EDGES`' , '`FACE_SET_BOUNDARIES`' ] ) – Mode, (optional)

- `LOOSE_PARTS`
Face Sets from Loose Parts – Create a face set per loose part in the mesh.

- MATERIALS
Face Sets from Material Slots – Create a face set per material slot.

- NORMALS
Face Sets from Mesh Normals – Create face sets for faces that have similar normal.

- `UV_SEAMS`
Face Sets from UV Seams – Create face sets using UV seams as boundaries.

- CREASES
Face Sets from Edge Creases – Create face sets using edge creases as boundaries.

- `BEVEL_WEIGHT`
Face Sets from Bevel Weight – Create face sets using bevel weights as boundaries.

- `SHARP_EDGES`
Face Sets from Sharp Edges – Create face sets using sharp edges as boundaries.

- `FACE_SET_BOUNDARIES`
Face Sets from Face Set Boundaries – Create a face set per isolated face set.

- threshold ( float ) – Threshold, Lower limit to treat a feature as a boundary when forming face sets (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
