# bpy.types.CopyScaleConstraint: properties

## CopyScaleConstraint(Constraint)

### CopyScaleConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. CopyScaleConstraint ( Constraint )

Mirror the target's scale onto the owner.
power

Take the target's scale and raise it to the given exponent (in [-inf, inf], default 1.0)

Type :

float
subtarget

Names a vertex group on a mesh or lattice, or a bone on an armature, … (default "", never None)

Type :

str
target

The object pointed at as a target

Type :

Object
use_add

Blend scale by adding rather than multiplying (kept for 2.7 compatibility) (default True)

Type :

bool
use_make_uniform

Spread the copied volume change evenly over the owner's three axes (default False)

Type :

bool
use_offset

Fold the owner's own scale together with the copied scale (default False)

Type :

bool
use_x

Pull in the target's X scale (default False)

Type :

bool
use_y

Pull in the target's Y scale (default False)

Type :

bool
use_z

Pull in the target's Z scale (default False)

Type :

bool

[Related references](INDEX.md).
