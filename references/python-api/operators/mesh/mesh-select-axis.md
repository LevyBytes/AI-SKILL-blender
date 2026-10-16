# bpy.ops.mesh.select_axis

bpy.ops.mesh. select_axis ( * , orientation = 'LOCAL' , sign = 'POS' , axis = 'X' , threshold = 0.0001 ) 

Pick all mesh data along a single orientation

Parameters :

- orientation (Literal[Transform Orientation Items]) – Axis Mode, Which reference frame to use (optional)

- sign ( Literal [ 'POS' , 'NEG' , 'ALIGN' ] ) – Axis Sign, Which half to pick (optional)

- axis (Literal[Axis Xyz Items]) – Axis, Which dimension to measure against (optional)

- threshold ( float ) – Threshold, (in [1e-06, 50], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
