# bpy.ops.mesh.average_normals

bpy.ops.mesh. average_normals ( * , average_type = '`CUSTOM_NORMAL`' , weight = 50 , threshold = 0.01 )

Smooth custom normals on picked vertices via the chosen method

Parameters :

- average_type ( Literal [ '`CUSTOM_NORMAL`' , '`FACE_AREA`' , '`CORNER_ANGLE`' ] ) – Type, Averaging method (optional)

- `CUSTOM_NORMAL`
Custom Normal – Take average of vertex normals.

- `FACE_AREA`
Face Area – Set all vertex normals by face area.

- `CORNER_ANGLE`
Corner Angle – Set all vertex normals by corner angle.

- weight ( int ) – Weight, Weight applied per face (in [1, 100], optional)

- threshold ( float ) – Threshold, Threshold value for different weights to be considered equal (in [0, 10], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
