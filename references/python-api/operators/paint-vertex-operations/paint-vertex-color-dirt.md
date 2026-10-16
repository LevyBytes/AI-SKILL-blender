# bpy.ops.paint.vertex_color_dirt

bpy.ops.paint. vertex_color_dirt ( * , blur_strength = 1.0 , blur_iterations = 1 , clean_angle = 3.14159 , dirt_angle = 0.0 , dirt_only = False , normalize = True ) 

Manufacture a grime mapping progression dependent on concavity

Parameters :

- blur_strength ( float ) – Blur Strength, Blur vigor per single iteration (in [0.01, 1], optional)

- blur_iterations ( int ) – Blur Iterations, Quantity of instances to blur the pigments (amplified blurs more) (in [0, 40], optional)

- clean_angle ( float ) – Highlight Angle, Below 90 restricts the span utilized in the shadowy assortment (in [0, 3.14159], optional)

- dirt_angle ( float ) – Dirt Angle, Below 90 restricts the span utilized in the shadowy assortment (in [0, 3.14159], optional)

- dirt_only ( bool ) – Dirt Only, Do not calculate shines for bulging zones (optional)

- normalize ( bool ) – Normalize, Proportion the pigments, magnifying the distinction (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/vertexpaint_dirt.py:179

[Related references](INDEX.md).
