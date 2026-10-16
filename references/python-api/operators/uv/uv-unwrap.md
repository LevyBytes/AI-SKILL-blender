# bpy.ops.uv.unwrap

bpy.ops.uv. unwrap ( * , method = 'CONFORMAL' , fill_holes = False , correct_aspect = True , use_subsurf_data = False , margin_method = 'SCALED' , margin = 0.001 , no_flip = False , iterations = 10 , use_weights = False , weight_group = 'uv_importance' , weight_factor = 1.0 ) 

Unwraps the mesh belonging to the object under edit

Parameters :

- method ( Literal [ '`ANGLE_BASED`' , 'CONFORMAL' , '`MINIMUM_STRETCH`' ] ) – Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower) (optional)

- fill_holes ( bool ) – Fill Holes, Virtually fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry (optional)

- correct_aspect ( bool ) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)

- use_subsurf_data ( bool ) – Use Subdivision Surface, Map UVs taking vertex position after Subdivision Surface modifier has been applied (optional)

- margin_method ( Literal [ 'SCALED' , 'ADD' , 'FRACTION' ] ) – Margin Method, (optional)

- SCALED
Scaled – Multiply the margin by the existing UV scale.

- ADD
Add – Apply the margin straight, disregarding UV scale.

- FRACTION
Fraction – Give an exact fraction of the final UV output.

- margin ( float ) – Margin, Space between islands (in [0, 1], optional)

- no_flip ( bool ) – No Flip, Prevent flipping UV’s, flipping may lower distortion depending on the position of pins (optional)

- iterations ( int ) – Iterations, Number of iterations when “Minimum Stretch” method is used (in [0, 10000], optional)

- use_weights ( bool ) – Importance Weights, Whether to take into account per-vertex importance weights (optional)

- weight_group ( str ) – Weight Group, Vertex group name for importance weights (modulating the deform) (optional, never None)

- weight_factor ( float ) – Weight Factor, How much influence the weightmap has for weighted parameterization, 0 being no influence (in [-10000, 10000], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
