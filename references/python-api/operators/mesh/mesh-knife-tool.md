# bpy.ops.mesh.knife_tool

bpy.ops.mesh. knife_tool ( * , use_occlude_geometry = True , only_selected = False , xray = True , visible_measurements = 'NONE' , angle_snapping = 'NONE' , angle_snapping_increment = 0.523599 , wait_for_input = True )

Score contemporary topology

Parameters :

- use_occlude_geometry ( bool ) – Occlude Geometry, Only cut the front most geometry (optional)

- only_selected ( bool ) – Only Selected, Only cut selected geometry (optional)

- xray ( bool ) – X-Ray, Show cuts hidden by geometry (optional)

- visible_measurements ( Literal [ 'NONE' , 'BOTH' , 'DISTANCE' , 'ANGLE' ] ) – Measurements, Visible distance and angle measurements (optional)

- NONE
None – Show no measurements.

- BOTH
Both – Show both distances and angles.

- DISTANCE
Distance – Show just distance measurements.

- ANGLE
Angle – Show just angle measurements.

- angle_snapping ( Literal [ 'NONE' , 'SCREEN' , 'RELATIVE' ] ) – Angle Snapping, Angle snapping mode (optional)

- NONE
None – No angle snapping.

- SCREEN
Screen – Screen space angle snapping.

- RELATIVE
Relative – Angle snapping relative to the previous cut edge.

- angle_snapping_increment ( float ) – Angle Snap Increment, The angle snap increment used when in constrained angle mode (in [0, 3.14159], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
