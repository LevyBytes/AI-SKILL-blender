# bpy.types.LimitDistanceConstraint: properties

## LimitDistanceConstraint(Constraint)

### LimitDistanceConstraint(Constraint) 

base classes: bpy_struct, Constraint
class bpy.types. LimitDistanceConstraint ( Constraint ) 

Limit the distance from target object
distance 

Radius of limiting sphere (in [-inf, inf], default 0.0)

Type :

float
head_tail 

Position along the bone's length, where Head is 0 and Tail is 1 (in [0, 1], default 0.0)

Type :

float
limit_mode 

Which distances relative to the sphere of influence are permitted (default '`LIMITDIST_INSIDE`' )

- `LIMITDIST_INSIDE`
Inside – The object is constrained inside a virtual sphere around the target object, with a radius defined by the limit distance.

- `LIMITDIST_OUTSIDE`
Outside – The object is constrained outside a virtual sphere around the target object, with a radius defined by the limit distance.

- `LIMITDIST_ONSURFACE`
On Surface – The object is constrained on the surface of a virtual sphere around the target object, with a radius defined by the limit distance.

Type :

Literal[‘`LIMITDIST_INSIDE`’, ‘`LIMITDIST_OUTSIDE`’, ‘`LIMITDIST_ONSURFACE`’]
subtarget 

Armature bone, mesh or lattice vertex group, … (default “”, never None)

Type :

str
target 

Target object

Type :

Object
use_bbone_shape 

Trace the B-Bone segment shape when working out the Head/Tail position (default False)

Type :

bool
use_transform_limit 

This constraint affects transforms too (default False)

Type :

bool

[Related references](INDEX.md).
