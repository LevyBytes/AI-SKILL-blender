# bpy.types.Bone: use_scale_easing

use_scale_easing

Scale the final easing values by the Scale In/Out Y factors (default False)

Type:
bool

basename

The name of this bone before any . character.

(readonly)

center

The midpoint between the head and the tail.

(readonly)

children_recursive

A list of all children from this bone.

Note

Takes O(len(bones)**2) time.

(readonly)

children_recursive_basename

Returns a chain of children with the same base name as this bone.
Only direct chains are supported, forks caused by multiple children
with matching base names will terminate the function
and not be returned.

Note

Takes O(len(bones)**2) time.

(readonly)

parent_recursive

A list of parents, starting with the immediate parent.

(readonly)

vector

The direction this bone is pointing.
Utility function for (tail - head)

(readonly)

x_axis

Vector pointing down the x-axis of the bone.

(readonly)

y_axis

Vector pointing down the y-axis of the bone.

(readonly)

z_axis

Vector pointing down the z-axis of the bone.

(readonly)

[Related references](INDEX.md).
