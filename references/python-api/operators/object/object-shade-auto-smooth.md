# bpy.ops.object.shade_auto_smooth

bpy.ops.object. shade_auto_smooth ( * , use_auto_smooth = True , angle = 0.523599 ) 

Insert a modifier that automatically tags mesh edges based on the angle between bordering faces

Parameters :

- use_auto_smooth ( bool ) – Auto Smooth, Insert modifier to mark edge sharpness mechanically (optional)

- angle ( float ) – Angle, Upper threshold for face normal divergence that is still treated as smooth (in [0, 3.14159], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
