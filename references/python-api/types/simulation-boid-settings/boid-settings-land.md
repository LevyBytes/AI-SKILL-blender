# bpy.types.BoidSettings: land_acc_max, land_ave_max, land_jump_speed, land_personal_space, land_smooth, land_speed_max, land_stick_force

land_acc_max

Top acceleration while grounded, expressed relative to peak speed (in [0, 1], default 0.0)

Type:
float
land_ave_max

Top angular velocity while grounded, expressed relative to 180 degrees (in [0, 1], default 0.0)

Type:
float
land_jump_speed

Highest speed allowed for a jump (in [0, 100], default 0.0)

Type:
float
land_personal_space

Personal-space radius on land, given as a percentage of particle size (in [0, 10], default 0.0)

Type:
float
land_smooth

Degree of smoothing applied as boids touch down (in [0, 10], default 0.0)

Type:
float
land_speed_max

Top speed while grounded (in [0, 100], default 0.0)

Type:
float
land_stick_force

Minimum force needed before it begins influencing a grounded boid (in [0, 1000], default 0.0)

Type:
float

[Related references](INDEX.md).
