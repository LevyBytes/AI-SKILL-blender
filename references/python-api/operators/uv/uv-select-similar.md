# bpy.ops.uv.select_similar

bpy.ops.uv. select_similar ( * , type = 'PIN' , compare = 'EQUAL' , threshold = 0.0 ) 

Selects UVs that share a property type

Parameters :

- type ( Literal [ 'PIN' , 'LENGTH' , '`LENGTH_3D`' , 'AREA' , '`AREA_3D`' , 'MATERIAL' , 'OBJECT' , 'SIDES' , 'WINDING' , 'FACE' ] ) – Type, (optional)

- PIN
Pinned.

- LENGTH
Length – Edge length in UV space.

- `LENGTH_3D`
Length 3D – Length of edge in 3D space.

- AREA
Area – Face area in UV space.

- `AREA_3D`
Area 3D – Area of face in 3D space.

- MATERIAL
Material.

- OBJECT
Object.

- SIDES
Polygon Sides.

- WINDING
Winding – Face direction defined by clockwise or anti-clockwise winding (facing up or facing down).

- FACE
Amount of Faces in Island.

- compare ( Literal [ 'EQUAL' , 'GREATER' , 'LESS' ] ) – Compare, (optional)

- threshold ( float ) – Threshold, (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
