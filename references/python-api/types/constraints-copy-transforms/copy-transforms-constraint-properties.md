# bpy.types.CopyTransformsConstraint: properties

## CopyTransformsConstraint(Constraint)

### CopyTransformsConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. CopyTransformsConstraint ( Constraint )

Mirror every transform of the target onto the owner.
head_tail

Where along the bone the target sits, with 0 at the Head and 1 at the Tail (in [0, 1], default 0.0)

Type :

float
mix_mode

Choose the way the copied transform blends with the one already present (default 'REPLACE' )

- REPLACE
Replace – Swap the copied transformation in for the original.

- `BEFORE_FULL`
Before Original (Full) – Put the copied transformation first via plain matrix multiplication, as though the target were a parent under Full Inherit Scale. Combining rotation with non-uniform scale here introduces shear..

- BEFORE
Before Original (Aligned) – Put the copied transformation first, as though the target were a parent under Aligned Inherit Scale. In practice that means Full for location and Split Channels for rotation and scale..

- `BEFORE_SPLIT`
Before Original (Split Channels) – Put the copied transformation first while treating location, rotation, and scale on their own, much like chaining three Copy constraints.

- `AFTER_FULL`
After Original (Full) – Put the copied transformation last via plain matrix multiplication, as though the target were a child under Full Inherit Scale. Combining rotation with non-uniform scale here introduces shear..

- AFTER
After Original (Aligned) – Put the copied transformation last, as though the target were a child under Aligned Inherit Scale. In practice that means Full for location and Split Channels for rotation and scale..

- `AFTER_SPLIT`
After Original (Split Channels) – Put the copied transformation last while treating location, rotation, and scale on their own, much like chaining three Copy constraints.

Type :

Literal['REPLACE', '`BEFORE_FULL`', 'BEFORE', '`BEFORE_SPLIT`', '`AFTER_FULL`', 'AFTER', '`AFTER_SPLIT`']
remove_target_shear

Strip shear out of the target transform before it is blended in (default False)

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

[Related references](INDEX.md).
