# freestyle.shaders.SmoothingShader

class freestyle.shaders. SmoothingShader 

Class hierarchy: freestyle.types.StrokeShader > SmoothingShader

[Geometry shader]
__init__ ( num_iterations = 100 , factor_point = 0.1 , factor_curvature = 0.0 , factor_curvature_difference = 0.2 , aniso_point = 0.0 , aniso_normal = 0.0 , aniso_curvature = 0.0 , carricature_factor = 1.0 ) 

Builds a SmoothingShader object.

Parameters :

- num_iterations ( int ) – The number of iterations.

- factor_point ( float ) – 0.1

- factor_curvature ( float ) – 0.0

- factor_curvature_difference ( float ) – 0.2

- aniso_point ( float ) – 0.0

- aniso_normal ( float ) – 0.0

- aniso_curvature ( float ) – 0.0

- carricature_factor ( float ) – 1.0
shade ( stroke ) 

Smooths the stroke by nudging its vertices so the line reads more smoothly. Curvature flow drives it toward a curve of constant curvature, and the diffusion is made anisotropic so it does not bleed across corners.

Parameters :

stroke (freestyle.types.Stroke) – A Stroke object.

[Related references](INDEX.md).
