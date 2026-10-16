# bpy.ops.view3d.interactive_add

bpy.ops.view3d. interactive_add ( * , primitive_type = 'CUBE' , plane_origin_base = 'EDGE' , plane_origin_depth = 'EDGE' , plane_aspect_base = 'FREE' , plane_aspect_depth = 'FREE' , wait_for_input = True ) 

Adds an object interactively

Parameters :

- primitive_type ( Literal [ 'CUBE' , 'CYLINDER' , 'CONE' , '`SPHERE_UV`' , '`SPHERE_ICO`' ] ) – Primitive, (optional)

- plane_origin_base ( Literal [ 'EDGE' , 'CENTER' ] ) – Origin, The initial position for placement (optional)

- EDGE
Edge – Begin placement from the edge position.

- CENTER
Center – Begin placement from the center position.

- plane_origin_depth ( Literal [ 'EDGE' , 'CENTER' ] ) – Origin, The initial position for placement (optional)

- EDGE
Edge – Begin placement from the edge position.

- CENTER
Center - Initiates placement of the center position.

- plane_aspect_base ( Literal [ 'FREE' , 'FIXED' ] ) - Aspect, Initial aspect ratio preference (optional)

- FREE
Free - Permits unrestricted aspect ratios.

- FIXED
Fixed - Enforces a 1:1 aspect ratio.

- plane_aspect_depth ( Literal [ 'FREE' , 'FIXED' ] ) - Aspect, Initial aspect ratio preference (optional)

- FREE
Free - Permits unrestricted aspect ratios.

- FIXED
Fixed - Enforces a 1:1 aspect ratio.

- wait_for_input ( bool ) - Wait for Input, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
