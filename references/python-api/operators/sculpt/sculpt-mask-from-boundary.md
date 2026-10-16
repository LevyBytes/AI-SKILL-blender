# bpy.ops.sculpt.mask_from_boundary

bpy.ops.sculpt. mask_from_boundary ( * , mix_mode = 'MIX' , mix_factor = 1.0 , settings_source = 'OPERATOR' , boundary_mode = 'MESH' , propagation_steps = 1 )

Form a mask determined by the perimeter of the geometry

Parameters :

- mix_mode ( Literal [ 'MIX' , 'MULTIPLY' , 'DIVIDE' , 'ADD' , 'SUBTRACT' ] ) – Mode, Blend approach (optional)

- mix_factor ( float ) – Mix Factor, (in [0, 5], optional)

- settings_source ( Literal [ 'OPERATOR' , 'BRUSH' , 'SCENE' ] ) – Settings, Source for parameter values (optional)

- OPERATOR
Operator – Use settings from operator properties.

- BRUSH
Brush – Use settings from brush.

- SCENE
Scene – Use settings from scene.

- boundary_mode ( Literal [ 'MESH' , '`FACE_SETS`' ] ) – Mode, Which boundary style to mask (optional)

- MESH
Mesh – Calculate the boundary mask based on disconnected mesh topology islands.

- `FACE_SETS`
Face Sets – Calculate the boundary mask between face sets.

- propagation_steps ( int ) – Propagation Steps, (in [1, 20], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
