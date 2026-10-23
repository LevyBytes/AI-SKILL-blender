# bpy.types.CopyLocationConstraint: properties

## CopyLocationConstraint(Constraint)

### CopyLocationConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. CopyLocationConstraint ( Constraint )

Mirror the target's location onto the owner.
head_tail

Where along the bone the target sits, with 0 at the Head and 1 at the Tail (in [0, 1], default 0.0)

Type :

float
invert_x

Flip the sign of the X location (default False)

Type :

bool
invert_y

Flip the sign of the Y location (default False)

Type :

bool
invert_z

Flip the sign of the Z location (default False)

Type :

bool
subtarget

Names a vertex group on a mesh or lattice, or a bone on an armature, … (default "", never None)

Type :

str
target

The object pointed at as a target

Type :

Object
use_bbone_shape

Trace the curve of the B-Bone segments when working out the Head/Tail position (default False)

Type :

bool
use_offset

Stack the copied location on top of the owner's own location (default False)

Type :

bool
use_x

Pull in the target's X location (default False)

Type :

bool
use_y

Pull in the target's Y location (default False)

Type :

bool
use_z

Pull in the target's Z location (default False)

Type :

bool

[Related references](INDEX.md).
