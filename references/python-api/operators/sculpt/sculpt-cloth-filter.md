# bpy.ops.sculpt.cloth_filter

bpy.ops.sculpt. cloth_filter ( * , start_mouse = (0, 0) , area_normal_radius = 0.25 , strength = 1.0 , iteration_count = 1 , event_history = None , type = 'GRAVITY' , force_axis = {'X', 'Y', 'Z'} , orientation = 'LOCAL' , cloth_mass = 1.0 , cloth_damping = 0.0 , use_face_sets = False , use_collisions = False )

Enact a fabric simulation deformation across the entire surface

Parameters :

- start_mouse ( Sequence [ int ] ) – Starting Mouse, (array of 2 items, in [0, 16384], optional)

- area_normal_radius ( float ) – Normal Radius, Span for computing surface orientation when clicked, measured as a share of brush radius(in [0.001, 5], optional)

- strength ( float ) – Strength, How much the filter affects the surface (in [-10, 10], optional)

- iteration_count ( int ) – Repeat, How many times to execute the filter (in [1, 10000], optional)

- event_history ( bpy_prop_collection [ OperatorStrokeElement ]) – (optional)

- type ( Literal [ 'GRAVITY' , 'INFLATE' , 'EXPAND' , 'PINCH' , 'SCALE' ] ) – Filter Type, Transformation that will be applied to the surface (optional)

- GRAVITY
Gravity – Applies gravity to the simulation.

- INFLATE
Inflate – Inflates the cloth.

- EXPAND
Expand – Expands the cloth's dimensions.

- PINCH
Pinch – Pulls the cloth to the cursor's start position.

- SCALE
Scale – Scales the mesh as a soft body using the origin of the object as scale.

- force_axis ( set [ Literal [ 'X' , 'Y' , 'Z' ] ] ) – Force Axis, Which axis receives the force (optional)

- X
X – Apply force in the X axis.

- Y
Y – Apply force in the Y axis.

- Z
Z – Apply force in the Z axis.

- orientation ( Literal [ 'LOCAL' , 'WORLD' , 'VIEW' ] ) – Orientation, Frame of reference used to constrain the filter force (optional)

- LOCAL
Local – Use the local axis to limit the force and set the gravity direction.

- WORLD
World – Use the global axis to limit the force and set the gravity direction.

- VIEW
View – Use the view axis to limit the force and set the gravity direction.

- cloth_mass ( float ) – Cloth Mass, Weight of every simulation particle (in [0, 2], optional)

- cloth_damping ( float ) – Cloth Damping, How extensively the applied forces diffuse through the fabric (in [0, 1], optional)

- use_face_sets ( bool ) – Use Face Sets, Restrict the filter to the face set beneath the cursor (optional)

- use_collisions ( bool ) – Use Collisions, Contact with other collider objects in the scene (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
