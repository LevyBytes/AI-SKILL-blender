# bpy.types.Sculpt: automasking_boundary_edges_propagation_steps, automasking_cavity_blur_steps, automasking_cavity_curve, automasking_cavity_curve_op, automasking_cavity_factor, automasking_start_normal_falloff, automasking_start_normal_limit, automasking_view_normal_falloff, automasking_view_normal_limit

automasking_boundary_edges_propagation_steps

How far inward from a fully masked edge the boundary-edge automask keeps shielding vertices (in [1, 20], default 1)

Type :

int
automasking_cavity_blur_steps

How many blur passes are run over the cavity mask (in [0, 25], default 0)

Type :

int
automasking_cavity_curve

Curve that drives the sensitivity (readonly)

Type :

CurveMapping
automasking_cavity_curve_op

Curve that drives the sensitivity (readonly)

Type :

CurveMapping
automasking_cavity_factor

Contrast applied to the cavity mask (in [0, 5], default 1.0)

Type :

float
automasking_start_normal_falloff

Widen the angular band with a graded falloff (in [0.0001, 1], default 0.25)

Type :

float
automasking_start_normal_limit

Span of angles that gets affected (in [0.0001, 3.14159], default 0.349066)

Type :

float
automasking_view_normal_falloff

Widen the angular band with a graded falloff (in [0.0001, 1], default 0.25)

Type :

float
automasking_view_normal_limit

Span of angles that gets affected (in [0.0001, 3.14159], default 1.5708)

Type :

float

[Related references](INDEX.md).
