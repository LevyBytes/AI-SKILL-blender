# bpy.ops.curve.draw

**bpy.ops.curve.draw**( * , error_threshold = 0.0 , fit_method = 'REFIT' , corner_angle = 1.22173 , use_cyclic = True , stroke = None , wait_for_input = True )

Create a spline by sketching freehand strokes.

Parameters:
- error_threshold ( float ) – Error, Maximum distance allowed from the drawn path (in object units) (in [0, 10], optional)
- fit_method (Literal[Curve Fit Method Items]) – Fit Method, (optional)
- corner_angle ( float ) – Corner Angle, (in [0, 3.14159], optional)
- use_cyclic ( bool ) – Cyclic, (optional)
- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)
- wait_for_input ( bool ) – Wait for Input, (optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
