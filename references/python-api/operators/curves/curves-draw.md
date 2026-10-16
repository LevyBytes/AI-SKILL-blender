# bpy.ops.curves.draw

**bpy.ops.curves.draw**( * , error_threshold = 0.0 , fit_method = 'REFIT' , corner_angle = 1.22173 , use_cyclic = True , stroke = None , wait_for_input = True , is_curve_2d = False , bezier_as_nurbs = False )

Draw a curve by making freehand strokes.

Parameters:
- error_threshold ( float ) – Error, Maximum distance allowed from the drawn path (in object units) (in [0, 10], optional)
- fit_method (Literal[Curve Fit Method Items]) – Fit Method, (optional)
- corner_angle ( float ) – Corner Angle, (in [0, 3.14159], optional)
- use_cyclic ( bool ) – Cyclic, (optional)
- stroke ( bpy_prop_collection [ OperatorStrokeElement ]) – Stroke, (optional)
- wait_for_input ( bool ) – Wait for Input, (optional)
- is_curve_2d ( bool ) – Curve 2D, (optional)
- bezier_as_nurbs ( bool ) – As NURBS, (optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
