# bpy.ops.uv.smart_project

bpy.ops.uv. smart_project ( * , angle_limit = 1.15192 , margin_method = 'SCALED' , rotate_method = '`AXIS_ALIGNED_Y`' , island_margin = 0.0 , area_weight = 0.0 , correct_aspect = True , scale_to_bounds = False ) 

Unwraps the chosen faces of mesh objects by projection

Parameters :

- angle_limit ( float ) – Angle Limit, Lower for more projection groups, higher for less distortion (in [0, 1.5708], optional)

- margin_method ( Literal [ 'SCALED' , 'ADD' , 'FRACTION' ] ) – Margin Method, (optional)

- SCALED
Scaled – Multiply the margin by the existing UV scale.

- ADD
Add – Apply the margin straight, disregarding UV scale.

- FRACTION
Fraction – Give an exact fraction of the final UV output.

- rotate_method ( Literal [ '`AXIS_ALIGNED`' , '`AXIS_ALIGNED_X`' , '`AXIS_ALIGNED_Y`' ] ) – Rotation Method, (optional)

- `AXIS_ALIGNED`
Axis-aligned – Turned to its tightest rectangle, vertical or horizontal.

- `AXIS_ALIGNED_X`
Axis-aligned (Horizontal) – Turn islands so they line up horizontally.

- `AXIS_ALIGNED_Y`
Axis-aligned (Vertical) – Turn islands so they line up vertically.

- island_margin ( float ) – Island Margin, Margin to reduce bleed from adjacent islands (in [0, 1], optional)

- area_weight ( float ) – Area Weight, Weight projection’s vector by faces with larger areas (in [0, 1], optional)

- correct_aspect ( bool ) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)

- scale_to_bounds ( bool ) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
