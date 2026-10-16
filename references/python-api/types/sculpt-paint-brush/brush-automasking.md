# bpy.types.Brush: automasking_boundary_edges_propagation_steps, automasking_cavity_blur_steps, automasking_cavity_curve, automasking_cavity_factor, automasking_start_normal_falloff, automasking_start_normal_limit, automasking_view_normal_falloff, automasking_view_normal_limit

automasking_boundary_edges_propagation_steps

How far boundary-edge automasking reaches when shielding vertices from a fully masked edge (in [1, 20], default 1)

Type :

int
automasking_cavity_blur_steps

How many passes of blur are applied to the cavity mask (in [0, 25], default 0)

Type :

int
automasking_cavity_curve

Curve driving the sensitivity (readonly)

Type :

CurveMapping
automasking_cavity_factor

Strength of the cavity mask's contrast (in [0, 5], default 1.0)

Type :

float
automasking_start_normal_falloff

Widen the angular band with a gradient that fades off (in [0.0001, 1], default 0.25)

Type :

float
automasking_start_normal_limit

How wide a span of angles gets affected (in [0.0001, 3.14159], default 0.349066)

Type :

float
automasking_view_normal_falloff

Widen the angular band with a gradient that fades off (in [0.0001, 1], default 0.25)

Type :

float
automasking_view_normal_limit

How wide a span of angles gets affected (in [0.0001, 3.14159], default 1.5708)

Type :

float

[Related references](INDEX.md).
