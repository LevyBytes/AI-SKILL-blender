# bpy.types.HookModifier: properties

## HookModifier(Modifier)

### HookModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. HookModifier ( Modifier )

Drives vertex positions from an external object or bone.
center

Center of the hook, used for falloff and display (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
falloff_curve

Custom falloff curve (readonly)

Type :

CurveMapping
falloff_radius

When non-zero, sets how far from the hook the influence reaches before dropping off (in [0, inf], default 0.0)

Type :

float
falloff_type

(default 'SMOOTH' )

Type :

Literal['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', '`INVERSE_SQUARE`', 'SHARP', 'LINEAR', 'CONSTANT']
invert_vertex_group

Invert vertex group influence (default False)

Type :

bool
matrix_inverse

Undoes the transform sitting between this object and its target (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))

Type :

mathutils.Matrix
object

The hook's parent object; setting it also recomputes and resets the offset

Type :

Object
strength

Relative force of the hook (in [0, 1], default 1.0)

Type :

float
subtarget

The parent bone's name for the hook where relevant; assigning it likewise recomputes and resets the offset (default "", never None)

Type :

str
use_falloff_uniform

Compensate for non-uniform object scale (default False)

Type :

bool
vertex_group

Name of the vertex group that sets per-point modifier influence (default "", never None)

Type :

str
vertex_indices

The indices of the vertices the modifier is bound to; on Bézier curves, handles register as extra vertices. (array of 64 items, in [0, inf], default (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), readonly)

Type :

bpy_prop_array[int]

[Related references](INDEX.md).
