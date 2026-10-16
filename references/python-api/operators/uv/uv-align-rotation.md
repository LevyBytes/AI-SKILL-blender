# bpy.ops.uv.align_rotation

bpy.ops.uv. align_rotation ( * , method = 'AUTO' , axis = 'X' , correct_aspect = False ) 

Sets the rotation of the UV island

Parameters :

- method ( Literal [ 'AUTO' , 'EDGE' , 'GEOMETRY' ] ) – Method, Method to calculate rotation angle (optional)

- AUTO
Auto – Derive the angle from every edge.

- EDGE
Edge – Use only the edges that are selected.

- GEOMETRY
Geometry – Align against the Geometry axis.

- axis ( Literal [ 'X' , 'Y' , 'Z' ] ) – Axis, Axis to align to (optional)

- X
X – X axis.

- Y
Y – Y axis.

- Z
Z – Z axis.

- correct_aspect ( bool ) – Correct Aspect, Take image aspect ratio into account (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/uvcalc_transform.py:360

[Related references](INDEX.md).
