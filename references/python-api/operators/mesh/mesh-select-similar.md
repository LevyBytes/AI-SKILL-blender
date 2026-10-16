# bpy.ops.mesh.select_similar

bpy.ops.mesh. select_similar ( * , type = '`VERT_NORMAL`' , compare = 'EQUAL' , threshold = 0.0 ) 

Mark vertices, spines or surfaces that resemble one another by attribute

Parameters :

- type ( Literal [ '`VERT_NORMAL`' , '`VERT_FACES`' , '`VERT_GROUPS`' , '`VERT_EDGES`' , '`VERT_CREASE`' , '`EDGE_LENGTH`' , '`EDGE_DIR`' , '`EDGE_FACES`' , '`EDGE_FACE_ANGLE`' , '`EDGE_CREASE`' , '`EDGE_BEVEL`' , '`EDGE_SEAM`' , '`EDGE_SHARP`' , '`EDGE_FREESTYLE`' , '`FACE_MATERIAL`' , '`FACE_AREA`' , '`FACE_SIDES`' , '`FACE_PERIMETER`' , '`FACE_NORMAL`' , '`FACE_COPLANAR`' , '`FACE_SMOOTH`' , '`FACE_FREESTYLE`' ] ) – Type, (optional)

- compare ( Literal [ 'EQUAL' , 'GREATER' , 'LESS' ] ) – Compare, (optional)

- threshold ( float ) – Threshold, (in [0, 100000], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
