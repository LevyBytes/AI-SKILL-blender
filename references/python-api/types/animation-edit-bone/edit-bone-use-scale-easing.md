# bpy.types.EditBone: use_scale_easing

use_scale_easing

Scale the final easing values by the Scale In/Out Y factors (default False)

Type :

bool

basename

This bone’s name up to its first . character.

(readonly)

center

The point halfway between the head and the tail.

(readonly)

children

A list holding every one of this bone’s children.

Note

Takes O(len(bones)) time.

(readonly)

children_recursive

A list of every descendant of this bone.

Note

Takes O(len(bones)**2) time.

(readonly)

children_recursive_basename

Walks down a chain of children sharing this bone’s base name.
Only straight chains work; where multiple children share matching
base names the fork ends the walk and nothing further is returned.

Note

Takes O(len(bones)**2) time.

(readonly)

parent_recursive

A list of ancestors, beginning with the direct parent.

(readonly)

vector

The direction in which this bone points.
A convenience for (tail - head)

(readonly)

x_axis

A vector running along the bone’s x-axis.

(readonly)

y_axis

A vector running along the bone’s y-axis.

(readonly)

z_axis

A vector running along the bone’s z-axis.

(readonly)

[Related references](INDEX.md).
