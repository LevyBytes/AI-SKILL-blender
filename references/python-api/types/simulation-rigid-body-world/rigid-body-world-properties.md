# bpy.types.RigidBodyWorld: properties

## RigidBodyWorld(bpy_struct)

### RigidBodyWorld(bpy_struct)

base class: bpy_struct
class bpy.types. RigidBodyWorld ( bpy_struct )

A self-contained environment plus settings for a rigid body simulation
collection

Collection holding the objects that take part in this simulation

Type :

Collection
constraints

Collection holding the rigid body constraint objects

Type :

Collection
effector_weights

(readonly)

Type :

EffectorWeights
enabled

The simulation will be evaluated (default True)

Type :

bool
point_cache

(readonly, never None)

Type :

PointCache
solver_iterations

How many constraint solver iterations run each simulation step; raising it improves accuracy at the expense of speed (in [1, 1000], default 10)

Type :

int
substeps_per_frame

How many simulation steps run per frame; raising it improves accuracy at the expense of speed (in [1, 32767], default 10)

Type :

int
time_scale

Adjust how fast the simulation runs (in [0, 100], default 1.0)

Type :

float
use_split_impulse

Cut down the extra velocity that accumulates when objects collide; use it sparingly since it slightly lowers simulation stability (default False)

Type :

bool

[Related references](INDEX.md).
