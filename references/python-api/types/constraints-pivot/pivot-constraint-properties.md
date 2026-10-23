# bpy.types.PivotConstraint: properties

## PivotConstraint(Constraint)

### PivotConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. PivotConstraint ( Constraint )

Pivots the rotation about an alternate point
head_tail

Target along length of bone: Head is 0, Tail is 1 (in [0, 1], default 0.0)

Type :

float
offset

Where the pivot sits relative to the target (when one is set), or relative to the owner's location (when Fixed Position is off), or the absolute pivot point itself (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
rotation_range

Range of rotation over which pivoting takes place (default 'NX' )

- `ALWAYS_ACTIVE`
Always – Pivot on every rotation, no matter the direction.

- NX
-X Rotation – Pivot only while rotating into the X-axis negative range.

- NY
-Y Rotation – Pivot only while rotating into the Y-axis negative range.

- NZ
-Z Rotation – Pivot only while rotating into the Z-axis negative range.

- X
X Rotation – Pivot only while rotating into the X-axis positive range.

- Y
Y Rotation – Pivot only while rotating into the Y-axis positive range.

- Z
Z Rotation – Pivot only while rotating into the Z-axis positive range.

Type :

Literal[‘`ALWAYS_ACTIVE`’, ‘NX’, ‘NY’, ‘NZ’, ‘X’, ‘Y’, ‘Z’]
subtarget

(default “”, never None)

Type :

str
target

Target Object, defining the position of the pivot when defined

Type :

Object
use_bbone_shape

Trace the B-Bone segment shape when working out the Head/Tail position (default False)

Type :

bool
use_relative_location

Treat the offset as an absolute point in space rather than relative to the target (default True)

Type :

bool

[Related references](INDEX.md).
