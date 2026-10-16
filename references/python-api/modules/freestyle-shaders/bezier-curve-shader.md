# freestyle.shaders.BezierCurveShader

class freestyle.shaders. BezierCurveShader 

Class hierarchy: freestyle.types.StrokeShader > BezierCurveShader

[Geometry shader]
__init__ ( error = 4.0 ) 

Builds a BezierCurveShader object.

Parameters :

error ( float ) – How much error the approximation is permitted, measured as the largest distance tolerated between the new curve and the original geometry.
shade ( stroke ) 

Reshapes the stroke's backbone geometry so it matches a Bezier Curve fit to the backbone it started from.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
