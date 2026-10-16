# bpy.ops.rigidbody.connect

bpy.ops.rigidbody. connect ( * , con_type = 'FIXED' , pivot_type = 'CENTER' , connection_pattern = '`SELECTED_TO_ACTIVE`' )

Establish constraints linking multiple selected rigid bodies

Parameters :

- con_type ( Literal [ 'FIXED' , 'POINT' , 'HINGE' , 'SLIDER' , 'PISTON' , 'GENERIC' , '`GENERIC_SPRING`' , 'MOTOR' ] ) – Type, Relationship style between constrained bodies (optional)

- FIXED
Fixed – Glue rigid bodies together.

- POINT
Point – Constrain rigid bodies to move around common pivot point.

- HINGE
Hinge – Restrict rigid body rotation to one axis.

- SLIDER
Slider – Restrict rigid body translation to one axis.

- PISTON
Piston – Restrict rigid body translation and rotation to one axis.

- GENERIC
Generic – Restrict translation and rotation to specified axes.

- `GENERIC_SPRING`
Generic Spring – Restrict translation and rotation to specified axes with springs.

- MOTOR
Motor – Drive rigid body around or along an axis.

- pivot_type ( Literal [ 'CENTER' , 'ACTIVE' , 'SELECTED' ] ) – Location, Where the constraint pivot sits (optional)

- CENTER
Center – Pivot location is between the constrained rigid bodies.

- ACTIVE
Active – Pivot location is at the active object position.

- SELECTED
Selected – Pivot location is at the selected object position.

- connection_pattern ( Literal [ '`SELECTED_TO_ACTIVE`' , '`CHAIN_DISTANCE`' ] ) – Connection Pattern, How objects are linked to form the constraint structure (optional)

- `SELECTED_TO_ACTIVE`
Selected to Active – Connect selected objects to the active object.

- `CHAIN_DISTANCE`
Chain by Distance – Connect objects as a chain based on distance, starting at the active object.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/rigidbody.py:277

[Related references](INDEX.md).
