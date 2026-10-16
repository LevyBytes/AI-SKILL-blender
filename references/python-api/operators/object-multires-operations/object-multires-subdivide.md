# bpy.ops.object.multires_subdivide

bpy.ops.object. multires_subdivide ( * , modifier = '' , mode = '`CATMULL_CLARK`' ) 

Introduce an additional subdivision level

Parameters :

- modifier ( str ) – Modifier, Name of the modifier to edit (optional, never None)

- mode ( Literal [ '`CATMULL_CLARK`' , 'SIMPLE' , 'LINEAR' ] ) – Subdivision Mode, Strategy for splitting the mesh into a finer tier (optional)

- `CATMULL_CLARK`
Catmull-Clark – Split using Catmull-Clark algorithm.

- SIMPLE
Simple – Split using simple neighbor averaging.

- LINEAR
Linear – Split using linear interpolation of manual sculpting.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
