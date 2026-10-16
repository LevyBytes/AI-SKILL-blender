# bpy.ops.grease_pencil.interpolate

bpy.ops.grease_pencil.interpolate ( * , shift = 0.0 , layers = 'ACTIVE' , exclude_breakdowns = False , use_selection = False , flip = 'AUTO' , smooth_steps = 1 , smooth_factor = 0.0 )
Generate in-between strokes bridging two keyframes

Parameters:
- shift ( float ) – Shift, Balance which frame influences the intermediate strokes more (in [-1, 1], optional)
- layers ( Literal [ 'ACTIVE' , 'ALL' ] ) – Layer, Which layers participate in interpolation (optional)
- exclude_breakdowns ( bool ) – Exclude Breakdowns, Ignore existing breakdown keyframes when determining range (optional)
- use_selection ( bool ) – Use Selection, Interpolate only highlighted strokes (optional)
- flip ( Literal [ 'NONE' , 'FLIP' , 'AUTO' ] ) – Flip Mode, Reverse target strokes to align start/end with source (optional)
- smooth_steps ( int ) – Iterations, How many times to smooth the generated strokes (in [1, 3], optional)
- smooth_factor ( float ) – Smooth, Strength of noise reduction applied to intermediate strokes (in [0, 2], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
