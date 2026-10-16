# bpy.types.ClothCollisionSettings: properties

collection

Restrict colliders to objects in this Collection

Type :

Collection
collision_quality

Solver iterations (higher = more accurate but slower) (in [1, 32767], default 2)

Type :

int
damping

Velocity reduction on collision (in [0, 1], default 1.0)

Type :

float
distance_min

Minimum gap before collision kicks in (in [0.001, 1], default 0.015)

Type :

float
friction

Sliding resistance on contact (higher = more resistance) (in [0, 80], default 5.0)

Type :

float
impulse_clamp

Impulse limit to stabilize (0 disables) (in [0, 100], default 0.0)

Type :

float
self_distance_min

Minimum gap for self-collision response (in [0.001, 0.1], default 0.015)

Type :

float
self_friction

Self-contact sliding resistance (in [0, 80], default 5.0)

Type :

float
self_impulse_clamp

Self-collision impulse limit (0 disables) (in [0, 100], default 0.0)

Type :

float
use_collision

Enable object collisions (default True)

Type :

bool
use_self_collision

Enable self-intersections (default False)

Type :

bool
vertex_group_object_collisions

Exclude triangles where all vertices belong to this group from object collisions (default "", never None)

Type :

str
vertex_group_self_collisions

Exclude triangles where all vertices belong to this group from self-collisions (default "", never None)

Type :

str

[Related references](INDEX.md).
