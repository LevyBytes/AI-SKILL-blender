# bpy.ops.grease_pencil.interpolate_sequence

bpy.ops.grease_pencil.interpolate_sequence ( * , step = 1 , layers = 'ACTIVE' , exclude_breakdowns = False , use_selection = False , flip = 'AUTO' , smooth_steps = 1 , smooth_factor = 0.0 , type = 'LINEAR' , easing = '`EASE_IN`' , back = 1.702 , amplitude = 0.15 , period = 0.15 )
Populate frames between keyframes with smoothly eased motion

Parameters:
- step ( int ) – Step, Frame count between each newly created interpolation (in [1, 1048574], optional)
- layers ( Literal [ 'ACTIVE' , 'ALL' ] ) – Layer, Which layers participate in interpolation (optional)
- exclude_breakdowns ( bool ) – Exclude Breakdowns, Ignore existing breakdown keyframes when determining range (optional)
- use_selection ( bool ) – Use Selection, Interpolate only highlighted strokes (optional)
- flip ( Literal [ 'NONE' , 'FLIP' , 'AUTO' ] ) – Flip Mode, Reverse target strokes to align start/end with source (optional)

- smooth_steps ( int ) – Iterations, How many times to smooth the generated strokes (in [1, 3], optional)
- smooth_factor ( float ) – Smooth, Strength of noise reduction applied to intermediate strokes (in [0, 2], optional)
- type ( Literal [ 'LINEAR' , 'CUSTOM' , 'SINE' , 'QUAD' , 'CUBIC' , 'QUART' , 'QUINT' , 'EXPO' , 'CIRC' , 'BACK' , 'BOUNCE' , 'ELASTIC' ] ) – Type, Easing curve used for next interpolation run (optional)
- LINEAR: Direct progression with no smoothing applied
- CUSTOM: User-defined easing from a curve editor
- SINE: Smooth ease (minimal, almost linear with slight arc)
- QUAD: Squared acceleration/deceleration curve
- CUBIC: Cubic acceleration/deceleration curve
- QUART: Fourth-degree polynomial curve
- QUINT: Fifth-degree polynomial curve
- EXPO: Steep acceleration curve (pronounced effect)
- CIRC: High-curvature circular arc (most dramatic effect)
- BACK: Cubic with anticipation and rebound
- BOUNCE: Decaying bounce-like motion similar to impact
- ELASTIC: Decaying sine wave resembling a stretched spring
- easing (Literal[Beztriple Interpolation Easing Items]) – Easing, Which segment endpoints receive easing interpolation (optional)
- back ( float ) – Back, Magnitude of anticipatory overshoot for back easing (in [0, inf], optional)
- amplitude ( float ) – Amplitude, Magnitude multiplier for elastic bounces (in [0, inf], optional)
- period ( float ) – Period, Interval between elastic oscillations (in [-inf, inf], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
